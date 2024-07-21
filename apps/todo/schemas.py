from pydantic import BaseModel


class CreateProjectIn(BaseModel):
    title: str


class CreateProjectOut(BaseModel):
    id: int
    title: str
    slug: str


class CreateSectionIn(BaseModel):
    title: str
    project_id: int


class CreateSectionOut(BaseModel):
    id: int
    title: str
    slug: str
