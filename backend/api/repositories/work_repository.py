from backend.api.core.models import Work
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified
from backend.api.utils import get_coordinates
from backend.api.utils import get_weather

class WorkRepository:
    def __init__(self,db: Session):
        self.db = db

    def create(self, address: str, photos: list, proprietary_id: str, observations: list, activities: list):
        new_work = Work(address=address,photos=photos,proprietary_id=proprietary_id,observations=observations, activities=activities)
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
            if work.photos == None:
                work.photos = []
            work.photos.append(photo)
            flag_modified(work, "photos")
            self.db.commit()
            self.db.refresh(work)
            return work.photos[len(work.photos) - 1]
        return None
    
    def remove_photo(self, id: str, photo: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            try:
                result = None
                if photo in work.photos:
                    result= photo
                work.photos.remove(photo)
                flag_modified(work, "photos")
                self.db.commit()
                self.db.refresh(work)
                return result
            except ValueError:
                return ValueError(f"Foto {photo} não encontrada!")
        return None
    
    def add_observation(self, id: str, observation: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            if work.observations == None:
                work.observations = []
            work.observations.append(observation)
            flag_modified(work, "observations")
            self.db.commit()
            self.db.refresh(work)
            return work.observations[len(work.observations) -1]
        return None
    
    def remove_observation(self, id: str, observation: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            try:
                result = None
                if observation in work.observations:
                    result = observation
                work.observations.remove(observation)
                flag_modified(work, "observations")
                self.db.commit()
                self.db.refresh(work)
                return result
            except ValueError:
                return ValueError(f"Observação {observation} não encontrada!")
        return None
    
    def add_activity(self, id: str, activity: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            if work.activities == None:
                work.activities = []
            work.activities.append(activity)
            flag_modified(work, "activities")
            self.db.commit()
            self.db.refresh(work)
            return work.activities[len(work.activities) - 1]
        return None
    
    def remove_activity(self, id: str, activity: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            try:
                result = None
                if activity in work.activities:
                    result = activity
                work.activities.remove(activity)
                flag_modified(work, "activities")
                self.db.commit()
                self.db.refresh(work)
                return result
            except ValueError:
                return ValueError(f"Atividade {activity} não encontrada!")
        return None
    
    def climate(self, id: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            loc = work.address
            coordinates = get_coordinates(loc)
            weather = get_weather(coordinates[0], coordinates[1])
            #return weather
            return [{
                'descrição': weather["weather"][0]["description"],
                'temperatura': f'{weather["main"]["temp"]:.2f}ºC',
                'pressão': f'{weather["main"]["pressure"]} hPa',
                'umidade': f'{weather["main"]["humidity"]}%',
                'velocidade do vento': f'{weather["wind"]["speed"]}m/s',
                'visibilidade': f'{weather["visibility"]}m'
            }]
        return None
    
    def delete(self, id: str):
        work = self.db.query(Work).filter(Work.id == id).first()
        if work:
            self.db.delete(work)
            self.db.commit()
            return work
        return None