# Ex1_oop_ariel

* we import the json file (Building.json), taking the data from the file and create Building object with x Elevator objects (x represente the amount of elevator the building has).
* in each Elevator object we have empty list of calls.
* we import the csv file (calls.csv) and create from each row a new call.
* for every call we will check the total time it takes for each elevator to complete the new call (along side all of the specific elevator current calls).
* after choosing the corect elevator we will insert the call to the specific elevator "calls list" and write the elevator id in the output csv file.


@how we choose the best elevator?
* if all calls are "up" type  then go to lowest src floor and go up.
* if all calls are "down" type  then go to highest src floor and go down.
* if we have both type:
  * if all the calls src floor are above us (above floor 0) then start with the up calls and then move on to the down calls.
  * if all the calls src floor are under us (under floor 0) then start with the down calls and then move on to the up calls.
  * if none of the above is true then find the highest down src floor and the lowest up src floor:
    * if highest down src floor is under 0:
      * go down and then go the lowest up src floor and start go up
    * if lowest up src floor is above 0:
      * go up and then go the highest down src floor and start go down
    * if none of them is true:
      * if highest down src floor is closer:
        * go the that floor and then go down and then go the lowest up src floor and start go up
      * if lowest up src floor is closer:
        * go the that floor and then go up and then go the highest down src floor and start go down


@function to make:
  1. calculate time for moving. (accept two floors number and an elevator. return the time it will take the elevator to reach the dest floor from the src floor). 
  2. go up only (all the calls are up type)
  3. go down only (all the calls are down only)
  4. ......
