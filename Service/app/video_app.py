from fastapi import FastAPI, UploadFile, File, Form, HTTPException, APIRouter
from fastapi.responses import FileResponse
from Service.model.video import generate_video_file

router = APIRouter(
    prefix="/video",
    tags=["video"]
)

@router.post("/generate_video", summary="Generate video from prompt and image")
def generate_video(
    image: UploadFile = File(...),
    prompt: str = Form(...),
    base_seed: int = Form(42)
):
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image")

    try:
        image_bytes = image.file.read()
        output_path = generate_video_file(image_bytes, prompt, base_seed)

        return FileResponse(
            path=output_path,
            media_type="video/mp4",
            filename=output_path.split("/")[-1]
        )

    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("video_app:app", host="0.0.0.0", port=8000, reload=True)
