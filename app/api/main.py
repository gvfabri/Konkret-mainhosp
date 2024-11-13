from fastapi import FastAPI
from app.api.routers import user, employee, work, proprietary

app = FastAPI()

app.include_router(user.router)
app.include_router(employee.router)
app.include_router(work.router)
app.include_router(proprietary.router)
