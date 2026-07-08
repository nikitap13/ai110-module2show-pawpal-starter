from pawpal_system import Pet, Task


def test_mark_complete():
    task = Task("Feed Buddy", "08:00")
    task.mark_complete()

    assert task.completed is True


def test_add_task():
    pet = Pet("Buddy", "Dog")
    pet.add_task(Task("Morning Walk", "09:00"))

    assert len(pet.tasks) == 1

def test_sort_tasks():
    from pawpal_system import Owner, Scheduler

    owner = Owner("Nikita")
    pet = Pet("Buddy", "Dog")

    pet.add_task(Task("Dinner", "18:00"))
    pet.add_task(Task("Walk", "08:00"))

    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    tasks = scheduler.sort_by_time(owner.get_all_tasks())

    assert tasks[0].description == "Walk"
    assert tasks[1].description == "Dinner"

def test_daily_recurrence_creates_next_task():
    from datetime import date, timedelta
    from pawpal_system import Scheduler, Owner

    owner = Owner("Nikita")
    pet = Pet("Buddy", "Dog")
    task = Task("Feed Buddy", "08:00", "daily")

    pet.add_task(task)
    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    scheduler.complete_task(pet, task)

    assert task.completed is True
    assert len(pet.tasks) == 2
    assert pet.tasks[1].due_date == date.today() + timedelta(days=1)

def test_detect_conflicts():
    from pawpal_system import Owner, Scheduler

    owner = Owner("Nikita")
    pet = Pet("Buddy", "Dog")

    task1 = Task("Feed Buddy", "08:00")
    task2 = Task("Walk Buddy", "08:00")

    pet.add_task(task1)
    pet.add_task(task2)
    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts(owner.get_all_tasks())

    assert len(conflicts) == 1
    assert conflicts[0].description == "Walk Buddy"