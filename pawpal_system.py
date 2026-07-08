from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        pass

    def mark_incomplete(self):
        """Mark this task as incomplete."""
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        pass

    def remove_task(self, task_description: str):
        """Remove a task by description."""
        pass

    def get_tasks(self):
        """Return all tasks for this pet."""
        pass


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        pass

    def remove_pet(self, pet_name: str):
        """Remove a pet by name."""
        pass

    def get_all_tasks(self):
        """Return all tasks for all pets."""
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self, tasks):
        """Sort tasks by time."""
        pass

    def filter_tasks(self, tasks, pet_name=None, completed=None):
        """Filter tasks by pet name or completion status."""
        pass

    def detect_conflicts(self, tasks):
        """Detect tasks scheduled at the same time."""
        pass