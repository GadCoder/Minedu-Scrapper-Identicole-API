from datetime import datetime
from sqlmodel import Field, SQLModel


class School(SQLModel, table=True):
    __tablename__ = "school_info"
    ordering: int | None
    id_codmod: str = Field(primary_key=True)
    anexo: str | None
    estrellitas_count: int | None
    estrellitas: int | None
    cod_local: str | None
    cen_edu: str | None
    dir_cen: str | None
    d_gestion: str | None
    pension: float | None
    anio_pension: int | None
    d_region: str | None
    d_prov: str | None
    d_dist: str | None
    estudiantes_x_aula: int | None
    d_nivel: str | None
    d_turno: str | None
    TIPOSEXO_IE: str | None
    d_alumnado: str | None
    nlat_ie: float | None
    nlong_ie: float | None
    identicole_estado: str | None
    d_estado: int | None
    fecha_creacion: datetime | None
    codigo_ubigeo: str | None
    d_modalidad: str | None
    i_modalidad: str | None
    i_nivel: str | None
    d_nivelDescripcion: str | None
    tiene_vacante: str | None
    participa_vacante: str | None


