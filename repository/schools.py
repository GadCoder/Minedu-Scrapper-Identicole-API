import json
from typing import Annotated

import httpx
from fastapi import Depends
from sqlmodel import Session

from db.models.school import School
from db.session import   get_session
from db.models.request_data import RequestData


SessionDep = Annotated[Session, Depends(get_session)]


async def save_schools_from_location(number_of_pages: int, request_data: RequestData, session: SessionDep):
    request_dict = request_data.model_dump()
    request_dict["dot-amount"] = request_dict.pop("dot_amount")
    for page in range(number_of_pages):
        await get_schools_from_page(page=page, request_data=request_dict, session=session)


def get_url_for_page(page: int) -> str:
    base_url = "https://identicole.minedu.gob.pe/colegio/busqueda_colegios_detalle"
    return base_url if page == 0 else f"{base_url}/{page}"

async def get_schools_from_page(
        page: int, request_data: dict, session: SessionDep
):
    url = get_url_for_page(page=page)
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=request_data)
    status_code = response.status_code
    if status_code != 200:
        print(f"! Error al obtener colegios  -> {status_code}")
        return
    parts = response.text.split("||")
    if len(parts) < 4:
        print(f"! No se encontraron colegios para page {page}")
        return
    schools = json.loads(parts[3])
    if not schools:
        print(f"! No se encontraron colegios para page {page}")
        return
    save_schools(schools=schools, session=session)



def save_schools(schools: list, session: SessionDep):
    print(f"Saving {len(schools)} schools")
    for school_data in schools:
        school = School(**school_data)
        try:
            save_school_data(school=school, session=session)
        except Exception as e:
            print(f"Error saving school {school} -> {e}")
            continue


def save_school_data(school: School, session: SessionDep, ):
    session.add(school)
    session.commit()
    session.refresh(school)
