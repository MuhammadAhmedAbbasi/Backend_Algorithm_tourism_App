import os
import uuid
import subprocess
import sys
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from typing import Optional

app = FastAPI()

# Configuration
MODEL_CONFIG = {
    "task": "s2v-1.3B",
    "size": "832*480",
    "ckpt_dir": r"D:\toursim\updated\Backend_Algorithm_tourism_App\Service\Wan2.1-T2V-1.3B",
    "phantom_ckpt": r"D:\toursim\updated\Backend_Algorithm_tourism_App\Service\Phantom-Wan-Models\Phantom-Wan-1.3B.pth",
    "output_dir": "./generated_videos",
    "generate_py": r"D:\toursim\updated\Backend_Algorithm_tourism_App\Service\generate.py",
    "python_executable": r"D:\toursim\updated\Backend_Algorithm_tourism_App\tourist\Scripts\python.exe"
}

# Ensure output directory exists
os.makedirs(MODEL_CONFIG["output_dir"], exist_ok=True)

@app.post("/generate-video")
def generate_video(
    image: UploadFile = File(...),
    prompt: str = Form(...),
    base_seed: Optional[int] = Form(42)
):
    if not image.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image")

    unique_id = str(uuid.uuid4())
    image_path = os.path.join(MODEL_CONFIG["output_dir"], f"temp_{unique_id}.png")
    output_path = os.path.join(MODEL_CONFIG["output_dir"], f"output_{unique_id}.mp4")

    try:
        with open(image_path, "wb") as buffer:
            buffer.write(image.file.read())

        print(f"[INFO] Starting video generation for prompt: '{prompt}'")

        cmd = [
            MODEL_CONFIG["python_executable"],
            os.path.abspath(MODEL_CONFIG["generate_py"]),
            "--task", MODEL_CONFIG['task'],
            "--size", MODEL_CONFIG['size'],
            "--ckpt_dir", os.path.abspath(MODEL_CONFIG['ckpt_dir']),
            "--phantom_ckpt", os.path.abspath(MODEL_CONFIG['phantom_ckpt']),
            "--ref_image", os.path.abspath(image_path),
            "--prompt", prompt,
            "--base_seed", str(base_seed),
            "--save_file", os.path.abspath(output_path)
        ]

        print(f"[CMD] {' '.join(cmd)}")
        print("[MODEL OUTPUT]")

        # Live streaming output
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )

        for line in process.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()

        process.wait()

        if process.returncode != 0:
            raise HTTPException(status_code=500, detail="Video generation failed")

        if not os.path.exists(output_path):
            raise HTTPException(status_code=500, detail="No video output file created")

        print(f"[SUCCESS] Video generation completed: {output_path}")

        return FileResponse(
            output_path,
            media_type="video/mp4",
            filename=f"generated_{unique_id}.mp4"
        )

    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=500, detail="Video generation timed out after 1 hour")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    finally:
        if os.path.exists(image_path):
            try:
                os.remove(image_path)
            except:
                pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
