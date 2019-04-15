# Chinese whispers: L Systems

- Time spent explaining the exercise: 10 mins
- Time spent in the exercise: 40 mins
- Time spent in discussion: 30 mins ( *note* Pizza ought to commence during this period)

## Facilitator's guide

Your role as a facilitator is to conduct the exercise and make sure timings are respected.
You can find more info about L-systems in the [reference document](ref.pdf)

### Introduction

The Sierpinski triangle is an L-system defined as follqows:

- variables : F G
- constants : + -
- start : F-G-G
- rules : (F → F-G+F+G-F), (G → GG)
- angle : 120°
- interpretation: `F` and `G` both mean "draw forward", `-` means "turn left by angle", and `+` means "turn right by angle"

A string of the described symbols, built by applying the described recursive productions and then interpreted
as described by a turtle graphics program, results in a pretty fractal triangle.

If we do a pass over the string, replacing symbols using the productions described, then when we are
finished, we say that this transformation describes a single recursion. 0 recursions therefore, is just
the starting string of symbols, and 1 recursion is where we do a single pass, resulting in
"F−G+F+G−F-GG-GG".

### Task 1: Write a program which draws the Sierpinski triangle for n=0

10 mins, then pass computer left

### Task 2: Write a program which draws the Sierpinski triangle for n=1

10 mins, then pass computer left

### Task 3: Write a program which draws the Sierpinski triangle for n=5

HINT: use the speed method of Turtle library

5mins, then 5mins refactor, then pass left

### Task 4: The business pivots wildly! We need another kind of Sierpinski triangle as well as this one

10mins, Here's the spec for the new kind of Sierpinski triangle:

- variables : A B
- constants : + -
- start : A
- rules : (A → B-A-B), (B → A+B+A)
- angle : 60°
- n = 5
- interpretation: `A` and `B` both mean "draw forward", `-` means "turn left by angle", and `+` means "turn right by angle"

If people haven't finished but they think they'll be able to in the next 5 minutes, then give 5
more minutes. Otherwise, finish the exercise.

After the extra 5 minutes, if used, stop the exercise. You're done! No extra refactoring allowed! We will talk about
the refactoring you _would_ do given the experiences you've had being handed code at short notice over the last hour.

## After-exercise discussion

- Each table is handed sticky notes and pens and told to discuss the exercise.
- They are to write whatever they want, but are offered a prompt of 3 questions:
What did you like? What didn't you like? What would you do differently next time?
- Tables should try to extract their own lessons and not just answer the prompts - that will give more interesting
results!
- After 10 minutes, ask if any table wants more time to keep talking. If they do, give them 5 minutes.
- After the extra 5 minutes, if used, bring the discussions to a close. Ask each table, one at a time,
to offer what they learnt to the whole group. Request that everyone listen to others' experience without commenting,
unless invited to do so.

### Optional Task: I give you images of one L-systme for iteration 1,2,3: guess, instructions, iterations number and angle :)