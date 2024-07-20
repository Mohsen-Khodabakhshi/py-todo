from pydantic import BaseModel


class CreateProjectIn(BaseModel):
    title: str


class CreateProjectOut(BaseModel):
    id: int
    title: str
    slug: str
