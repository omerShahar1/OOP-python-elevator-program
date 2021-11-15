# Ex1_oop_ariel

* We import the json file (Building.json), taking the data from the file and create Building object with x Elevator objects (x represente the amount of elevator the building has).
* In each Elevator object we have empty list of calls.
* We import the csv file (calls.csv) and create from each row a new call.
* For every call we will check the total time it takes for each elevator to complete the new call (along side all of the specific elevator current calls).
* After choosing the correct elevator we will insert the call to the specific elevator "calls list" and write the elevator id in the output csv file.

How to choose the best elevator?

* Case 0: The elevator have 0 calls. Return the time it will take to get to the src floor and then to the dest floor.

* Case 1_up: Elevator's sign and call type are both "up". The src floor of the call is above the elevator current floor.
           Insert the two new floors in the elevator journey up.

* Case 1_down: Elevator's sign and call type are both down. The src floor of the call is under the elevator current floor.
           insert the two new floors in the elevator journey down

* Case 2_up: Elevator's sign and call type are both up. The src floor of the call is under the elevator current floor.
           Finish the journey up and then go down to the src floor, and then go up to the dest floor.

* Case 2_down: Elevator's sign and call type are both down. The src floor of the call is above the elevator current floor.
           Finish the journey down and then go up to the src floor, and then go down to the dest floor.

* Case 3_up: Elevator's sign is down and call type is up.
           Finish the journey down and then go to the src floor, and then go up to the dest floor.

* Case 3_down: Elevator's sign is up and call type is down.
           finish the journey up and then go to the src floor, and then go down to the dest floor.


* Best_elevator(): receive the new call and building. Return the id of the elevator with the best time:
    * If the building have only 1 elevator, return the id of the elevator.
    * if the building have more than 1 elevator, go over all the elevators and return the id of the best one.

* Elevator_time(): Receive an elevator and a new call, then return how much time it will take to the elevator to complete all its calls
  including the new call received.

* Case0(): Elevator doesn't have calls yet. Check time from elevator current floor (floor 0) to the new call src and to dest.

* Case1_up(): New call and the elevator are up type. Time stemp on the call allow the elevator to reach its src and dest floors.
  organize the floors in a sorted list of integers and return time it takes the elevator to reach all of them.

* case1_down(): new call and the elevator are down type. time stemp on the call allow the elevator to reach its src and dest floors.
  organize the floors in a sorted list of integers and return time it takes the elevator to reach all of them.
* ........