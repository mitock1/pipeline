from typing import Any

from pydantic import BaseModel

# here you can add your models to serialize any object you need


def to_camel(string: str) -> str:
    return "".join(
        word.capitalize() if word != "id" else word.upper()
        for word in string.split("_")
    )


class BaseModelCamelAlias(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True
        orm_mode = True
        validate_assignment = True


class Message(BaseModel):
    message: str


class ValidationErrors(BaseModel):
    messages: dict[str, Any]


class NessSchema(BaseModel):
    environment: str
    name: str
    message: str
    version: str
    statusDateTime: str
    startupDateTime: str
