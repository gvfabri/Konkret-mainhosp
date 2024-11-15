from backend.api.core.models import Work
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified

class WorkRepository:
    def __init__(self,db: Session):
        self.db = db

    def create(self, address: str, photos: list, proprietary_id: str, observations: list):
        new_work = Work(address=address,photos=photos,proprietary_id=proprietary_id,observations=observations)
        self.db.add(new_work)
        self.db.commit()
        self.db.refresh(new_work)
        return new_work
    
    def all(self):
        work = self.db.query(Work).all()
        return work
    
    def get(self, id: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            return work
        return None
    
    def proprietary(self, id: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            return work.proprietary
        return None
    
    def workers(self, id: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            return work.workers
        return None
    
    def add_photo(self, id: str, photo: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            
            work.photos.append(photo)
            flag_modified(work, "photos")
            self.db.commit()
            self.db.refresh(work)
            return work
        return None
    
    def remove_photo(self, id: str, photo: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            try:
                work.photos.remove(photo)
                flag_modified(work, "photos")
                self.db.commit()
                self.db.refresh(work)
                return work
            except ValueError:
                return ValueError(f"Foto {photo} não encontrada!")
        return None
    
    def add_observation(self, id: str, observation: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            work.observations.append(observation)
            flag_modified(work, "observations")
            self.db.commit()
            self.db.refresh(work)
            return work
        return None
    
    def remove_observation(self, id: str, observation: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            try:
                work.observations.remove(observation)
                flag_modified(work, "observations")
                self.db.commit()
                self.db.refresh(work)
                return work
            except ValueError:
                return ValueError(f"Observação {observation} não encontrada!")
        return None
    
    def delete(self, id: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            self.db.delete(work)
            self.db.commit()
            return True
        return None