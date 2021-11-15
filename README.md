# Ex1_oop_ariel

* we import the json file (Building.json), taking the data from the file and create Building object with x Elevator objects (x represente the amount of elevator the building has).
* in each Elevator object we have empty list of calls.
* we import the csv file (calls.csv) and create from each row a new call.
* for every call we will check the total time it takes for each elevator to complete the new call (along side all of the specific elevator current calls).
* after choosing the corect elevator we will insert the call to the specific elevator "calls list" and write the elevator id in the output csv file.






how we choose the best elevator?

case 0: elevator has 0 calls. return the time it will take to get to the src floor and then to the dest floor

case 1_up: elevator sign and call type are both up. the src floor of the call is above the elevator current floor.
           insert the two new floors in the elevator journey up

case 1_down: elevator sign and call type are both down. the src floor of the call is under the elevator current floor.
           insert the two new floors in the elevator journey down

case 2_up: elevator sign and call type are both up. the src floor of the call is under the elevator current floor.
           finish the journey up and then go down to the src floor, and then go up to the dest floor.

case 2_down: elevator sign and call type are both down. the src floor of the call is above the elevator current floor.
           finish the journey down and then go up to the src floor, and then go down to the dest floor.

case 3_up: elevator sign is down and call type is up.
           finish the journey down and then go to the src floor, and then go up to the dest floor.

case 3_down: elevator sign is up and call type is down.
           finish the journey up and then go to the src floor, and then go down to the dest floor.






* best_elevator(): receive the new call and building. return the id of the elevator with the best time.
    * if building have only 1 elevator, return id of elevator
    * if building has more than 1, go over all the elevators and return the id of the nest one

* elevator_time(): recieve an elevator and the new call and return how much time it will take the elevator to complete all its calls
  with the new one.
* case0(): elevator doesn't have calls yet. check time from elevator current floor (floor 0) to the new call src and to dest.

* case1_up(): new call and the elevator are up type. time stemp on the call allow the elevator to reach its src and dest floors.
  organize the floors in a sorted list of integers and return time it takes the elevator to reach all of them.

* case1_down(): new call and the elevator are down type. time stemp on the call allow the elevator to reach its src and dest floors.
  organize the floors in a sorted list of integers and return time it takes the elevator to reach all of them.
* ........