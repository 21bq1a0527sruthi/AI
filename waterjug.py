from collections import defaultdict
import math
#wj1,wj2 means water in jug 1 and water in jug 2
def reachinggoalstate(wj1, wj2):
    if (wj1== goal and wj2 == 0) or (wj2 == goal and wj1 == 0):
        print(wj1, wj2)
        return True
    if visited[(wj1, wj2)] == False:
        print(wj1, wj2)
        visited[(wj1, wj2)] = True
        return (reachinggoalstate(0, wj2) or
                reachinggoalstate(wj1, 0) or
                reachinggoalstate(jug1, wj2) or
                reachinggoalstate(wj1, jug2) or
                reachinggoalstate(wj1 + min(wj2, (jug1-wj1)),
                wj2 - min(wj2, (jug1-wj1))) or
                solveWaterjug(wj1 - min(wj1, (jug2-wj2)),
                wj2 + min(wj1, (jug2-wj2))))
    else:
        return False
def check():
    if (jug1 <= goal) and (jug2 <= goal):
        print("Not Possible")
        return True
    
    elif (jug1 / 2 == jug2 or jug2 / 2 == jug1) and (jug1 != goal and jug2 != goal):
        print("Not Possible")
        return True
    elif(goal % (math.gcd(jug1, jug2)) != 0):
        print("Not Possible")
        return True

jug1 = int(input("enter the jug1 value "))
jug2 = int(input("enter the jug2 value "))
goal = int(input("enter the goal value of the jug "))
visited = defaultdict(lambda: False)
result = check()
if result != True:
    print("Steps: ")
    reachinggoalstate(0, 0)
    print("reached goal value")
