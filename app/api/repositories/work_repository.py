from ..core.models import Work
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified

class WorkRepository:
    def __init__(self,db: Session):
        self.db = db

    def create(self, address: str, photos: list):
        new_work = Work(address=address,photos=photos)
        self.db.add(new_work)
        self.db.commit()
        self.db.refresh(new_work)
        return new_work
    
    def all(self):
        return self.db.query(Work).all()
    
    def get(self, id: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            return work
        return f"Obra {id} não encontrada!"
    
    def add_photo(self, id: str, photo: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            
            work.photos.append(photo)
            flag_modified(work, "photos")
            self.db.commit()
            self.db.refresh(work)
            return "Foto adicionada com sucesso!", work
        return f"Obra {id} não encontrada!"
    
    def remove_photo(self, id: str, photo: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            try:
                work.photos.remove(photo)
                flag_modified(work, "photos")
                self.db.commit()
                self.db.refresh(work)
                return "Foto removida com sucesso!", work
            except ValueError:
                return f"Foto {photo} não encontrada!"
        return f"Obra {id} não encontrada!"
    
    def delete(self, id: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            self.db.delete(work)
            self.db.commit()
            return f"Obra {id} deletada."
        return f"Obra {id} não encontrada!"