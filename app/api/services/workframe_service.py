from ..repositories.workframe_repository import WorkframeRepository
from sqlalchemy.orm import Session

class WorkframeService:
    def __init__(self, db: Session):
        self.workframe_repository = WorkframeRepository(db)

    def create_workframe(self, address: str, photos: list):
        self.workframe_repository.create(address, photos)

    def all(self):
        return self.workframe_repository.all()

    def get(self, id: str):
        return self.workframe_repository.get(id)

    def add_photo(self, id: str, photo: str):
        self.workframe_repository.add_photo(id, photo)

    def remove_photo(self, id: str, photo: str):
        self.workframe_repository.remove_photo(id, photo)
    
    def delete(self, id: str):
        self.workframe_repository.delete(id)