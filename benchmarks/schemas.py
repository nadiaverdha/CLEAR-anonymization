from pydantic import BaseModel, Field


class Entity(BaseModel):
    text: str = Field(description="The matched text span")
    start: int = Field(description="Start character offset")
    end: int = Field(description="End character offset")
    type: str = Field(description="Entity label")


class NEROutput(BaseModel):
    entities: list[Entity]


class RelationOutput(BaseModel):
    label: str = Field(
        description="Predicted relation label, e.g. legal_representation_of"
    )
