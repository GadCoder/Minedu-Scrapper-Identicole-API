from typing import Annotated

from sqlmodel import SQLModel, Session
from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks

from db.models.school import School
from db.models.request_data import RequestData
from repository.schools import save_schools_from_location
from db.session import engine, get_session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_app():
    app = FastAPI()
    create_db_and_tables()
    return app


SessionDep = Annotated[Session, Depends(get_session)]

app = create_app()


@app.post("/save-schools-from-location")
def save_schools(
    request_data: RequestData,
    number_of_pages: int,
    session: SessionDep,
    background_tasks: BackgroundTasks,
):
    background_tasks.add_task(
        save_schools_from_location, number_of_pages, request_data, session
    )
    return {"message": "Saving schools"}


@app.get("/get-school-data")
def get_school_data(school_code: str, session: SessionDep) -> School:
    school = session.get(School, school_code)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return school
