from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Annotated
from app.api.core.schemas import PhotoPublic, PhotoSchema, WorkPublic, WorkSchema
from app.api.services.work_service import WorkService
from app.api.dependencies import get_work_service

router = APIRouter(
    prefix="/work",
    tags=["work"]
)


@router.post("", response_model=WorkPublic)
def add_work(
    work: WorkSchema,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.create_work(work.address, work.photos, work.id_proprietary, work.observations)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.put("/{id}/addphoto", response_model=PhotoPublic)
def add_photo(
    photo: PhotoSchema,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        photo_path = work_service.add_photo(photo.id_work, photo.photo)
        result = PhotoPublic(photo = photo_path)
        return result
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.put("/{id}/removephoto")
def remove_photo(
    id: str,
    photo: Annotated[str, Query()],
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.remove_photo(id, photo)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.put("/{id}/addobservation")
def add_observation(
    id: str,
    observation: Annotated[str, Query()],
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.add_observation(id, observation)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.put("/{id}/removeobservation")
def remove_observation(
    id: str,
    observation: Annotated[str, Query()],
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.remove_observation(id, observation)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")

@router.get("")
def getall_works(
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.all()
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}")
def get_work(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}/proprietary")
def get_proprietary(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.proprietary(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}/workers")
def get_workers(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)],
):
    try:
        return work_service.workers(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.delete("/{id}")
def delete_work(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        work_service.delete(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")