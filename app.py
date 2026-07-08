import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.write("A smart pet care scheduler for feedings, walks, medications, and appointments.")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

owner = st.session_state.owner
owner.name = st.text_input("Owner name", value=owner.name)

st.divider()

st.subheader("Add a Pet")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["Dog", "Cat", "Other"])

if st.button("Add pet"):
    owner.add_pet(Pet(pet_name, species))
    st.success(f"Added {pet_name}!")

if owner.pets:
    st.write("Your pets:")
    st.table([{"Name": pet.name, "Species": pet.species} for pet in owner.pets])
else:
    st.info("No pets added yet.")

st.divider()

st.subheader("Schedule a Task")

if owner.pets:
    selected_pet_name = st.selectbox("Choose pet", [pet.name for pet in owner.pets])
    task_description = st.text_input("Task description", value="Morning walk")
    task_time = st.time_input("Task time")
    frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

    if st.button("Add task"):
        selected_pet = next(pet for pet in owner.pets if pet.name == selected_pet_name)
        selected_pet.add_task(Task(task_description, task_time.strftime("%H:%M"), frequency))
        st.success(f"Added task for {selected_pet_name}!")
else:
    st.warning("Add a pet before scheduling tasks.")

st.divider()

st.subheader("Today's Schedule")

scheduler = Scheduler(owner)
tasks = scheduler.sort_by_time(owner.get_all_tasks())

if tasks:
    schedule_rows = []

    for pet in owner.pets:
        for task in pet.tasks:
            schedule_rows.append(
                {
                    "Pet": pet.name,
                    "Task": task.description,
                    "Time": task.time,
                    "Frequency": task.frequency,
                    "Completed": task.completed,
                }
            )

    st.table(sorted(schedule_rows, key=lambda row: row["Time"]))

    conflicts = scheduler.detect_conflicts(tasks)
    if conflicts:
        st.warning("Schedule conflict detected: two or more tasks are at the same time.")
else:
    st.info("No tasks scheduled yet.")