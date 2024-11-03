from ..repositories.work_repository import WorkRepository
from sqlalchemy.orm import Session

class WorkService:
    def __init__(self, db: Session):
        self.work_repository = WorkRepository(db)

    def create_work(self, address: str, photos: list):
        self.work_repository.create(address, photos)

    def all(self):
        return self.work_repository.all()

    def get(self, id: str):
        return self.work_repository.get(id)

    def add_photo(self, id: str, photo: str):
        self.work_repository.add_photo(id, photo)

    def remove_photo(self, id: str, photo: str):
        self.work_repository.remove_photo(id, photo)
    
    def delete(self, id: str):
        self.work_repository.delete(id)