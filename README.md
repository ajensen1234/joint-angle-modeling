# Joint Angle Modeling (Python)

## Design Philosophy
We want this code to operate in the most intuitive way possible. Rather than spreadsheets full of data and hundreds of lines of code repeating itself, we wanted any function to be self-contained and repeatable for each bone and joint.

Broadly, we break things up into 3 classes: `MarkerSet`, `Bone`, and `Joint`. A markerset is composed of the X,Y,Z values of an indivual marker from the mo-cap system. A bone is made up of all the markersets that allow it to define a coordinate reference frame. A joint is made up of multiple bones.

## To-Do
- [ ] Loading data
  - [ ] Write a script that automatically converts the trc files into `numpy` read-able format.
  - [ ] Write a script that converts that numpy files into dataframes.
  - [ ] (Maybe) try to make the selection of the markerset a little bit easier (ie picking the name instead of number)
- [ ] Defining Bones
  - [ ] Create a script that allows the user to choose the various fiducial markers that are going to be 





- [ ] Change the way that bone coordinate systems are defined.
