from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, Form, HTTPException

from Service.model.description import Description
from Service.common.http.description_request import DescriptionRequest
from Service.common.http.description_response import DescriptionResponse

description_model = Description()

router = APIRouter(
    prefix="/description",
    tags=["description"]
)

# ===== Endpoints =====
@router.post("/text", response_model=DescriptionResponse)
async def description_endpoint(data: DescriptionRequest):
    try:
        result = description_model.invoke(data.dict())
        return DescriptionResponse(answer=result, success=True)
    except Exception as e:
        return DescriptionResponse(answer=str(e), success=False)