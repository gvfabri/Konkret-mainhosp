from ..core.models import Workframe
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified

class WorkframeRepository:
    def __init__(self,db: Session):
        self.db = db

    def create(self,address: str, photos: list):
        new_workframe = Workframe(address=address,photos=photos)
        self.db.add(new_workframe)
        self.db.commit()
        self.db.refresh(new_workframe)
        return new_workframe
    
    def all(self):
        return self.db.query(Workframe).all()
    
    def get(self, id: str):
        workframe = self.db.query(Workframe).filter(Workframe.id == id).first()
        if workframe:
            return workframe
        return f"Obra {id} não encontrada!"
    
    def add_photo(self, id: str, photo: str):
        workframe = self.db.query(Workframe).filter(Workframe.id == id).first()
        if workframe:
            
            workframe.photos.append(photo)
            flag_modified(workframe, "photos")
            self.db.commit()
            self.db.refresh(workframe)
            return "Foto adicionada com sucesso!", workframe
        return f"Obra {id} não encontrada!"
    
    def remove_photo(self, id: str, photo: str):
        workframe = self.db.query(Workframe).filter(Workframe.id == id).first()
        if workframe:
            try:
                workframe.photos.remove(photo)
                flag_modified(workframe, "photos")
                self.db.commit()
                self.db.refresh(workframe)
                return "Foto removida com sucesso!", workframe
            except ValueError:
                return f"Foto {photo} não encontrada!"
        return f"Obra {id} não encontrada!"
    
    def delete(self, id: str):
        workframe = self.db.query(Workframe).filter(Workframe.id == id).first()
        if workframe:
            self.db.delete(workframe)
            self.db.commit()
            return f"Obra {id} deletada."
        return f"Obra {id} não encontrada!"