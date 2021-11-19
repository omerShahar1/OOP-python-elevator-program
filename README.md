# Ex1_oop_ariel

websites with information about the elevator problem:
* https://www.youtube.com/watch?app=desktop&v=siqiJAJWUVg
* https://tedweishiwang.github.io/journal/object-oriented-design-elevator.html
* https://coderanch.com/t/707819/engineering/Design-Elevator-System


start the program:
1. we take the strngs with the names of the building.json, the call.csv and the out.csv.
2. we create Building object and Elevator objects with the json file and create Call objects with the call.csv file.
3. we go over every line in the calls.csv file, find the best elevator to give by using the best_elevator function and change the value in the out.csv file.

Building object:
* 2 integers as values (min floor and max floor).
* list of elevator objects (we put in the list only the elevator from the specific json file)

Call object:
* 1 float value (time)
* 3 integers as values (src and dest floors are the first two. the third is "type" to tell us if the call is up or down)
* 1 boolean value to tell us if we already inserted the call data (dest and src floors) to the elevator floors lists.

Elevator object:
* store all the given data about the elevator (id, speed, minfloor, maxfloor, close time, open time, start time, stop time)
* integer value called current (current floorr of elevator. start always with 0)
* integer value called sign (0 if elevator hadnt started moving. 1 if it go up and -1 if down)
* float value called time (tell us how much time has passed since elevator started)
* list of calls
* upList and downList (lists of floors the elevator would need to reach when going down or up in the next run. the lists are sorted)
* newUpList and newDownList (lists of floors the elevator would need to reach when going down or up in the next run. the lists are sorted)

* zero data function: after we finish checking the elevator time we will delete all its progress in order to start it from zero in the next check
* add call function: if we chose this specific elevator then add the new call to its list and add the src and dest floors to the correct elevator floors lists
* switch_up_list: if the upList is empty then its means the up run is over so prepare the next run by insert the floors from the newUpList to the UpList
* switch_down_list: same as the swich_up_list but for down runs.


* Best_elevator(): receive the new call and building. Return the id of the elevator with the best time:
    * If the building have only 1 elevator, return the id of the elevator.
    * if the building have more than 1 elevator, go over all the elevators and return the id of the best one.

how we choose the best elevator?
* we will go over every elevator and check the time it will take it to complete the new call with all its previus calls.
* after finding the elevator, return its id and add the new call to its call list.
* if there is only 1 elevator just pick it and dont run the algoritm.

case 0: elevator has 0 calls. return the time it will take to get to the src floor and then to the dest floor (if src floor is 0 then just check close and and open time instaed of reaching the src floor).

case 2: elevator have at least one call. in that case we will tell the elevator to first go up or down based on its first call type.

* when going down we will change the elevator sign, and go over all the floors in the current run (downList). when it is over, activate switch_down_list and start going up. alse in every time the elevator moves we will check if the new call time had ariived. if not then do nothing but if yes then insert it in the correct floor list and change the call boolean value, start, to false.
* when going up do a miror image of the go down scenario.
* if the call is up type then we will insert its src and dest floors to the upList only if those floors are above the elevator current floor in the given moment. if they arent then we will insert the floors to the newUpList and sort to list from small to big.
* if the call is down type then we will insert its src and dest floors to the downList only if those floors are under the elevator current floor in the given moment. if they arent then we will insert the floors to the newdownList and sort to list from big to small.

note:
the algoritm is based on the idea that the elevator will start the run like ordinary elevator. for example if the first call to reach it was up type then the elevator will start its run by moving up.
if the elevator recieve new call and it is possible to complete it durring the current run then the elevator would do it. but if the new call is not possible to complete (for example if we go up and the new call src is under us) then the call will have to wait for the next run up.
the calls for the new run are sorted because the elevator already know them and would prefer to start them from the lowest floor (if it goes up) or from the highest floor (if go down).
