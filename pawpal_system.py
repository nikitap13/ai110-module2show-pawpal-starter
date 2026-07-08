from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def mark_incomplete(self):
        """Mark this task as incomplete."""
        self.completed = False

@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def remove_task(self, task_description: str):
        """Remove a task by description."""
        self.tasks = [task for task in self.tasks if task.description != task_description]

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def remove_pet(self, pet_name: str):
        """Remove a pet by name."""
        self.pets = [pet for pet in self.pets if pet.name != pet_name]

    def get_all_tasks(self):
        """Return all tasks for every pet."""
        all_tasks = []

        for pet in self.pets:
            all_tasks.extend(pet.tasks)

        return all_tasks    


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self, tasks):
        """Sort tasks by time."""
        return sorted(tasks, key=lambda task: task.time)

    def filter_tasks(self, tasks, pet_name=None, completed=None):
        """Filter tasks by pet name or completion status."""

        filtered = tasks

        if pet_name is not None:
            filtered = [
                task for pet in self.owner.pets
                if pet.name == pet_name
                for task in pet.tasks
            ]

        if completed is not None:
            filtered = [task for task in filtered if task.completed == completed]

        return filtered

    def detect_conflicts(self, tasks):
        """Detect tasks that occur at the same time."""

        seen = set()
        conflicts = []

        for task in tasks:
            if task.time in seen:
                conflicts.append(task)
            else:
                seen.add(task.time)

        return conflicts
    
    def complete_task(self, pet: Pet, task: Task):
        """Mark a task complete and create the next recurring task if needed."""
        task.mark_complete()

        if task.frequency == "daily":
            new_task = Task(
                task.description,
                task.time,
                task.frequency,
                False,
                task.due_date + timedelta(days=1)
            )
            pet.add_task(new_task)

        return task