from fastapi import APIRouter, HTTPException, Depends, Query, Response
from typing import Annotated, List
from backend.api.core.schemas import (PhotoPublic, PhotoSchema, WorkPublic, WorkSchema, ObservationPublic, 
                                  ObservationSchema, ProprietaryPublic, EmployeePublic, ActivityPublic, ActivitySchema, ClimatePublic, ClimateSchema)
from backend.api.services.work_service import WorkService
from backend.api.dependencies import get_work_service
import pandas as pd
from fastapi.responses import StreamingResponse
from fpdf import FPDF


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
        return work_service.create_work(work.address, work.photos, work.id_proprietary, work.observations, work.activities)
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

@router.put("/{id}/addactivity", response_model=ActivityPublic)
def add_activity(
    activity: ActivitySchema,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return ActivityPublic(activity= work_service.add_activity(activity.id_work, activity.activity))
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")

@router.put("/{id}/removeactivity", response_model=ActivityPublic)
def remove_activity(
    activity: ActivitySchema,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return ActivityPublic(activity= work_service.remove_activity(activity.id_work, activity.activity))
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
    
@router.get("/{id}/climate")
def get_climate(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        return work_service.get_climate(id)
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.get("/csv/")
def getall_csv(
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        works = work_service.all()
        data = []
        for work in works:
            workers = work_service.workers(work.id)
            weather = work_service.get_climate(work.id)
            data.append({
                "ID": work.id,
                "Endereço": work.address,
                "Proprietário": work.proprietary.name,
                "Empregados": [worker.name for worker in workers],
                "Observações": work.observations,
                "Atividades": work.activities,
                "Clima": weather
            })
        df = pd.DataFrame(data)
        return StreamingResponse(df.to_csv(index=False), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=works.csv"})
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
@router.get("/{id}/csv")
def get_csv(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        work = work_service.get(id)
        workers = work_service.workers(id)
        weather = work_service.get_climate(id)
        data = [{
            "ID": work.id,
            "Endereço": work.address,
            "Proprietário": work.proprietary.name,
            "Empregados": [worker.name for worker in workers],
            "Observações": work.observations,
            "Atividades": work.activities,
            "Clima": weather
        }]
        df = pd.DataFrame(data)
        return StreamingResponse(
            df.to_csv(index=False), 
            media_type="text/csv", 
            headers={"Content-Disposition": "attachment; filename=work.csv"})
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Deu erro: {str(e)}")
    
    
@router.get("/{id}/pdf")
def get_pdf(
    id: str,
    work_service: Annotated[WorkService, Depends(get_work_service)]
):
    try:
        # Obter os dados
        work = work_service.get(id)
        workers = work_service.workers(id)
        weather = work_service.get_climate(id)

        # Criar os dados estruturados em um DataFrame
        data = [{
            "ID": work.id,
            "Endereço": work.address,
            "Proprietário": work.proprietary.name,
            "Empregados": ", ".join(worker.name for worker in workers),
            "Observações": ", ".join(work.observations),
            "Atividades": ", ".join(work.activities),
            "Clima": weather
        }]
        
        # Criar o PDF
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Adicionar título ao PDF
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt=f"Relatório do Trabalho ID: {id}", ln=True, align="C")
        pdf.ln(10)  # Espaço entre título e conteúdo

        # Adicionar os dados do DataFrame ao PDF
        pdf.set_font("Arial", size=12)
        for col in data[0].keys():
            pdf.cell(0, 10, txt=f"{col}: {data[0][col]}", ln=True)

        # Gerar o PDF em formato de bytes diretamente
        pdf_output = pdf.output(dest='S').encode('latin1')  # 'S' gera o PDF como bytes

        # Retornar o PDF como resposta
        return Response(
            content=pdf_output,
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=work_{id}.pdf"}
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao gerar o PDF: {str(e)}")