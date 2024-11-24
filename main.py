from typing import Annotated

from sqlmodel import SQLModel, Session
from fastapi import Depends, FastAPI, HTTPException, Query

from db.session import  engine, create_engine, get_session
from db.models.school import School

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_app():
    app = FastAPI()
    create_db_and_tables()
    return app

SessionDep = Annotated[Session, Depends(get_session)]

app = create_app()


@app.post("/save-school-data")
def save_school_data(school: School, session: SessionDep) -> School:
    session.add(school)
    session.commit()
    session.refresh(school)
    return school

@app.get("/get-school-data")
def get_school_data(school_code: str, session: SessionDep) -> School:
    school = session.get(School, school_code)
    if not school:
        raise HTTPException(status_code=404, detail="School not found")
    return school