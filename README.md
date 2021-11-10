# Ex1_oop_ariel

* we import the json file (Building.json), taking the data from the file and create Building object with x Elevator objects (x represente the amount of elevator the building has).
* in each Elevator object we have empty list of calls.
* we import the csv file (calls.csv) and create from each row a new call.
* for every call we will check the total time it takes for each elevator to complete the new call (along side all of the specific elevator current calls).
* after choosing the corect elevator we will insert the call to the specific elevator "calls list" and write the elevator id in the output csv file.


@how we choose the best elevator?
@function to make:
  1. calculate time for moving. (accept two floors number and an elevator. return the time it will take the elevator to reach the dest floor from the src floor). 
  2. go up only (all the calls are up type)
  3. go down only (all the calls are down only)
  4. ......
