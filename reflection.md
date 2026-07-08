# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

1) Users should be able to add pets to their account, including basic details like the pet’s name and species.

2) Users should be able to schedule care tasks for each pet, such as feedings, walks, medications, and appointments.

3) Users should be able to view an organized daily schedule so they can see what tasks need to be completed and when.

I chose four main classes for my design: Owner, Pet, Task, and Scheduler. The Owner class stores the user's pets, the Pet class stores information and tasks for each pet, the Task class represents individual pet care activities, and the Scheduler class manages scheduling logic such as sorting, filtering, and conflict detection. 

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

I decided to use Python dataclasses for the Task and Pet classes because they mainly store data. I also kept the Scheduler separate from the Owner class so scheduling logic is organized and easier to maintain.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler considers the scheduled time of each task, the pet the task belongs to, whether the task has been completed, and whether tasks occur at the same time. It also supports recurring daily tasks by automatically creating the next day's task when one is completed. I prioritized time because it is the most important factor for organizing a daily pet care schedule, while conflict detection helps identify overlapping tasks.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is that it only checks for tasks scheduled at the exact same time instead of checking for overlapping task durations. This keeps the implementation simple and easy to understand while still providing useful conflict warnings for a basic scheduling application.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI to help brainstorm the system design, generate the UML diagram, create the class skeletons, and write automated tests. The most helpful prompts asked AI to explain how the classes should interact, generate method stubs, and suggest test cases for sorting, recurring tasks, and conflict detection.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I did not simply accept every AI suggestion. For example, I reviewed the generated class structure and kept the scheduling logic inside a separate Scheduler class instead of combining it with the Owner class. I verified each change by running main.py and using pytest to ensure the program behaved correctly.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task completion, adding tasks to pets, sorting tasks by time, creating recurring daily tasks, and detecting scheduling conflicts. These tests verify the core functionality of the scheduler and help ensure that the system behaves correctly as users add and manage pet care tasks.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am very confident that my scheduler works correctly because all automated tests passed successfully and the CLI and Streamlit demonstrations produced the expected results. If I had more time, I would add tests for weekly recurring tasks, pets with no tasks, duplicate pet names, invalid time inputs, and overlapping task durations.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with building the backend classes and connecting them to the Streamlit interface. Seeing the classes, scheduler, tests, and user interface work together made the project feel complete.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the scheduler by supporting task durations, overlapping time detection, editing and deleting tasks through the UI, and saving pet information between sessions using a database or file storage.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

If I had another iteration, I would improve the scheduler by supporting task durations, overlapping time detection, editing and deleting tasks through the UI, and saving pet information between sessions using a database or file storage.
