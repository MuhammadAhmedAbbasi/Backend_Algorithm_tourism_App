import os
import uuid
import subprocess
import sys

from Service.config import TASK, SIZE, CKPT_DIR, PHANTOM_CKPT, OUTPUT_DIR, GENERATE_PY, PYTHON_EXECUTABLE

def generate_video_file(image_bytes: bytes, prompt: str, base_seed: int = 42) -> str:
    unique_id = str(uuid.uuid4())
    image_path = os.path.join(OUTPUT_DIR, f"temp_{unique_id}.png")
    output_path = os.path.join(OUTPUT_DIR, f"output_{unique_id}.mp4")

    with open(image_path, "wb") as f:
        f.write(image_bytes)

    cmd = [
        PYTHON_EXECUTABLE,
        GENERATE_PY,
        "--task", TASK,
        "--size", SIZE,
        "--ckpt_dir", CKPT_DIR,
        "--phantom_ckpt", PHANTOM_CKPT,
        "--ref_image", image_path,
        "--prompt", prompt,
        "--base_seed", str(base_seed),
        "--save_file", output_path
    ]

    print(f"[INFO] Running command: {' '.join(cmd)}")
    print("[MODEL OUTPUT]")

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

    if process.returncode != 0 or not os.path.exists(output_path):
        raise RuntimeError("Video generation failed")

    try:
        os.remove(image_path)
    except:
        pass

    return output_path
