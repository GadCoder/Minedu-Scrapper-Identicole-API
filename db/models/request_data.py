from sqlmodel import Field, SQLModel

class RequestData(SQLModel):
    accion: str
    ubicacion: str
    s_departament_geo: str
    s_province_geo: str
    s_district_geo: str
    txt_cen_edu: str = ""
    modalidad: str
    s_nivel: str
    vacante: str
    participa: str
    dot_amount: str = Field(schema_extra={"validation_alias": "dot-amount"})
    genero: str = ""

