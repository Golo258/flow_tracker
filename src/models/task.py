import uuid
from pydantic import (
    Field,
    model_validator,
    BaseModel
)


class Task(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str = Field(..., 
        min_length=10,
        max_length=60,
        description="Name of task to complete"
    )
    estimate: int = Field(
        gt=5,
        le=40,
        title="Estimating time for task"
    )
    description: str = Field(..., min_length=30)


