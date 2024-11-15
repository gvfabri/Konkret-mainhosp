from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Annotated, List
from app.api.core.schemas import (PhotoPublic, PhotoSchema, WorkPublic, WorkSchema, ObservationPublic, 
                                  ObservationSchema, ProprietaryPublic, EmployeePublic)
from app.api.services.work_service import WorkService
from app.api.dependencies import get_work_service

router = APIRouter(
    prefix="/work",
    tags=["work"]
)

@router.get("", response_model=List[WorkPublic])
def getall_works(
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.all()
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.post("", response_model=WorkPublic)
def add_work(
    work: WorkSchema,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.create_work(work.address, work.photos, work.id_proprietary, work.observations)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.delete("/{id}", response_model=WorkPublic)
def delete_work(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.delete(id)
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
    
@router.put("/{id}/removephoto", response_model= PhotoPublic)
def remove_photo(
    photo: PhotoSchema,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        photo_path = work_service.remove_photo(photo.id_work, photo.photo)
        return PhotoPublic(photo = photo_path)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.put("/{id}/addobservation", response_model=ObservationPublic)
def add_observation(
    observation: ObservationSchema,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        result = work_service.add_observation(observation.id_work, observation.observation)
        return ObservationPublic(observation= result)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.put("/{id}/removeobservation", response_model=ObservationPublic)
def remove_observation(
    observation: ObservationSchema,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return ObservationPublic(observation= work_service.remove_observation(observation.id_work, observation.observation))
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")


@router.get("/{id}", response_model=WorkPublic)
def get_work(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.get(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}/proprietary", response_model=ProprietaryPublic)
def get_proprietary(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.proprietary(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}/workers", response_model=List[EmployeePublic])
def get_workers(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)],
):
    try:
        return work_service.workers(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
