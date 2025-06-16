from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from Service.common.http.caption_response import CaptionResponse, CaptionErrorResponse
from Service.model.caption import default_caption
from Service.config import (
    DEFAULT_MODEL,
    DEFAULT_PROMPT,
    ALLOWED_MIME_TYPES,
    ERROR_MESSAGES
)
import logging

router = APIRouter(
    prefix="/caption",
    tags=["captioning"]
)

@router.post("/generate")
async def generate_caption(files: List[UploadFile] = File(..., media_type="image")):
    """
    Generate captions for multiple uploaded images using the Caption service.
    """
    try:
        # Validate at least one file exists
        if not files or len(files) == 0:
            return JSONResponse(
                status_code=422,
                content={"detail": ERROR_MESSAGES["no_file"]}
            )

        # Validate content types
        for file in files:
            if not any(file.content_type.startswith(mime) for mime in ALLOWED_MIME_TYPES):
                return JSONResponse(
                    status_code=400,
                    content={"detail": ERROR_MESSAGES["invalid_type"]}
                )

        # Read all file contents
        contents_list = []
        for file in files:
            contents = await file.read()
            if len(contents) == 0:
                return JSONResponse(
                    status_code=422,
                    content={"detail": ERROR_MESSAGES["empty_file"]}
                )
            contents_list.append(contents)

        # Prepare data for caption service
        data = {
            "model": DEFAULT_MODEL,
            "prompt": DEFAULT_PROMPT,
            "images": contents_list
        }

        # Invoke caption service
        result = default_caption.invoke(data)
        
        # Return caption response
        if isinstance(result, CaptionResponse):
            return result
        else:
            # Handle error response
            return JSONResponse(
                status_code=500,
                content={"detail": result.details}
            )

    except Exception as e:
        logging.exception("File processing failed")
        return JSONResponse(
            status_code=500,
            content={"detail": ERROR_MESSAGES["server_error"].format(error=str(e))}
        )