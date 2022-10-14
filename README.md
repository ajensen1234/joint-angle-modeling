# Joint Angle Modeling (Python/MATLab)

## Design Philosophy
We want this code to operate in the most intuitive way possible. Rather than spreadsheets full of data and hundreds of lines of code repeating itself, we wanted any function to be self-contained and repeatable for each bone and joint.

Broadly, we break things up into 3 classes: `MarkerSet`, `Bone`, and `Joint`. A markerset is composed of the X,Y,Z values of an indivual marker from the mo-cap system. A bone is made up of all the markersets that allow it to define a coordinate reference frame. A joint is made up of multiple bones.

## To-Do
- [ ] Defining Joint
  - [ ]  Write a reference frame between two bones (using built-in scripts that automatically convert between fiducial and "true")
  - [ ] Decompose angles based on our choice (Grood and Suntay is my vote)
  - [ ] Plot angles using whatever method we want.
