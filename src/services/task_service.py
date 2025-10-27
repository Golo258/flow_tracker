

from models.task import Task
from typing import Optional, List

tasks: List[Task] = []
def add_new_task(
    name: str,
    estimate: int,
    description: str
) -> List[Task]:
    task = Task(
        name=name,
        estimate=estimate,
        description=description
    )
    tasks.append(task)

    return tasks

