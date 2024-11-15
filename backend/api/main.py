from fastapi import FastAPI
from backend.api.routers import user, employee, work, proprietary
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    'http://localhost:8000',
    'http://localhost:5173',
    'http://localhost:5434',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(employee.router)
app.include_router(work.router)
app.include_router(proprietary.router)


