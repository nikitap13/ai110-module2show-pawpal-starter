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

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
