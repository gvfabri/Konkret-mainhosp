from app.api.services.work_service import WorkService

class Diary():
    def __init__(self, db):
        self.db = db
        self.work_service = WorkService(self.db)
        works = self.work_service.all()

    def create_work(self, address, photos):
        self.work_service.create_work(address, photos)
    def getall_works(self):
        return self.work_service.all()
    def get_work(self, work_id):
        return self.work_service.get(work_id)
    def add_photo(self, work_id, photo):
        self.work_service.add_photo(work_id, photo)
    def remove_photo(self, work_id, photo):
        self.work_service.remove_photo(work_id, photo)
    def delete_work(self, work_id):
        self.work_service.delete(work_id)
    def add_worker(self, work_id, worker_id):
        self.work_service.add_worker(work_id, worker_id)
    def remove_worker(self, work_id, worker_id):
        self.work_service.remove_worker(work_id, worker_id)
    def get_workers(self, work_id):
        work = self.work_service.get(work_id)
        return work.workers
    def get_weather(self, work_id):
        work = self.work_service.get(work_id)
        work_address = work.address
        #TODO: Chamar a API de clima
        return
    def get_observations(self, work_id):
        work = self.work_service.get(work_id)
        return work.observations
    def get_activities(self, work_id):
        work = self.work_service.get(work_id)
        #TODO: Implementar
    def get_address(self, work_id):
        work = self.work_service.get(work_id)
        return work.address
    def export(self, work_id, str):
        work = self.work_service.get(work_id)
        if str == "pdf":
            #TODO: Implementar exportação para PDF
            return
        if str == "csv":
            #TODO: Implementar exportação para CSV
            return
        else:
            print("Formato inválido")
            return False