from backend.api.repositories.work_repository import WorkRepository
from sqlalchemy.orm import Session

class WorkService:
    def __init__(self, db: Session):
        self.work_repository = WorkRepository(db)

    def create_work(self, address: str, photos: list, proprietary_id: str, observations: list):
        return self.work_repository.create(address, photos, proprietary_id, observations)

    def all(self):
        return self.work_repository.all()

    def get(self, id: str):
        return self.work_repository.get(id)
    
    def proprietary(self, id: str):
        return self.work_repository.proprietary(id)
    
    def workers(self, id: str):
        return self.work_repository.workers(id)

    def add_photo(self, id: str, photo: str):
        return self.work_repository.add_photo(id, photo)

    def remove_photo(self, id: str, photo: str):
        return self.work_repository.remove_photo(id, photo)
    
    def delete(self, id: str):
        return self.work_repository.delete(id)
    
    def add_observation(self, id: str, observation: str):
        return self.work_repository.add_observation(id, observation)
    
    def remove_observation(self, id: str, observation: str):
        return self.work_repository.remove_observation(id, observation)