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
  * if none of the above is true then find closest src floor. then check the call type and do as followed:
    * if type is up then:
      * if the src floor is above us then go to the floor, finish all up floors and then go down to finish all down floors
      * if the src floor is under us then start to go down while compliting every down call with src floor under us (under floor 0) untill we reach the lowest dest floor from the
        selected down calls. then go up, to finish all the up calls and then go down again finishing all down calls.
    * if type is down then:
      * if the src floor is under us then go to the floor, finish all down floors and then go up to finish all up floors
      * if the src floor is above us then start to go up while compliting every up call with src floor above us (above floor 0) untill we reach the highest dest floor from the
        selected up calls. then go down, to finish all the down calls and then go up again finishing all up calls.


@function to make:
  1. calculate time for moving. (accept two floors number and an elevator. return the time it will take the elevator to reach the dest floor from the src floor). 
  2. go up only (all the calls are up type)
  3. go down only (all the calls are down only)
  4. ......
