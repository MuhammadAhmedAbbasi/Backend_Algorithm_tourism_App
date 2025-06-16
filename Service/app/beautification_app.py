from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, Response
from Service.model.beautification import ImageEnhancer
import base64
from io import BytesIO
import zipfile

router = APIRouter(
    prefix="/image",
    tags=["processing"]
)

@router.post("/beautify")
async def beautify_images(
    files: list[UploadFile] = File(...),
    return_json: bool = True  # ← New flag to control response format
):
    """
    Enhance images with two response options:
    - return_json=True (default): Returns base64-encoded JSON
    - return_json=False: Returns raw JPEG/ZIP files
    """
    try:
        enhanced_files = []
        for file in files:
            if not file.content_type.startswith('image/'):
                raise HTTPException(400, detail=f"File {file.filename} is not an image")
            
            enhanced = ImageEnhancer.beautify_image(await file.read())
            enhanced_files.append((file.filename, enhanced))

        # JSON Response (base64 encoded)
        if return_json:
            return JSONResponse(content={
                "images": [{
                    "filename": filename,
                    "content": base64.b64encode(content).decode('utf-8'),
                    "mime_type": "image/jpeg"
                } for filename, content in enhanced_files]
            })

        # Binary Response (direct download)
        if len(enhanced_files) == 1:
            filename, content = enhanced_files[0]
            return Response(
                content=content,
                media_type="image/jpeg",
                headers={"Content-Disposition": f"attachment; filename=enhanced_{filename}"}
            )
        else:
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, "w") as zip_file:
                for filename, content in enhanced_files:
                    zip_file.writestr(f"enhanced_{filename}", content)
            
            return Response(
                content=zip_buffer.getvalue(),
                media_type="application/zip",
                headers={"Content-Disposition": "attachment; filename=enhanced_images.zip"}
            )

    except Exception as e:
        raise HTTPException(500, detail=str(e))