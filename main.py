from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Nikita")

dog = Pet("Buddy", "Dog")
cat = Pet("Luna", "Cat")

owner.add_pet(dog)
owner.add_pet(cat)

dog.add_task(Task("Morning walk", "08:00", "daily"))
dog.add_task(Task("Dinner feeding", "18:00", "daily"))
cat.add_task(Task("Vet appointment", "14:30", "once"))

scheduler = Scheduler(owner)
tasks = scheduler.sort_by_time(owner.get_all_tasks())

print("Today's Schedule")
print("----------------")

for task in tasks:
    status = "Done" if task.completed else "Not Done"
    print(f"{task.time} - {task.description} ({task.frequency}) [{status}]")