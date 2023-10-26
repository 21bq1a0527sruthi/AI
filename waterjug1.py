from math import gcd

# Function to find the greatest common divisor (GCD) of two numbers
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to solve the water jug problem
def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    # Check if the target amount is greater than the sum of jug capacities
    if target_amount > jug1_capacity + jug2_capacity:
        print("No solution. Target amount is greater than the sum of jug capacities.")
        return

    # Check if the GCD of jug capacities does not evenly divide the target amount
    if target_amount % find_gcd(jug1_capacity, jug2_capacity) != 0:
        print("No solution. GCD of jug capacities does not divide the target amount.")
        return

    # Initialize the state of both jugs
    jug1 = 0
    jug2 = 0

    # Initialize a list to store the path
    path = []

    while jug1 != target_amount and jug2 != target_amount:
        # Fill jug1 if it's empty
        if jug1 == 0:
            jug1 = jug1_capacity
            path.append(f"Fill jug1 ({jug1_capacity}L)")
        # Pour water from jug1 to jug2
        elif jug1 > 0 and jug2 < jug2_capacity:
            transfer_amount = min(jug1, jug2_capacity - jug2)
            jug1 -= transfer_amount
            jug2 += transfer_amount
            path.append(f"Pour from jug1 to jug2 ({transfer_amount}L)")
        # Empty jug2 if it's full
        elif jug2 == jug2_capacity:
            jug2 = 0
            path.append(f"Empty jug2 (0L)")

    if jug1 == target_amount:
        print("Solution found:")
        for step in path:
            print(step)
        print(f"Jug1 contains {jug1}L, Jug2 contains {jug2}L")
    elif jug2 == target_amount:
        print("Solution found:")
        for step in path:
            print(step)
        print(f"Jug1 contains {jug1}L, Jug2 contains {jug2}L")

# Input jug capacities and target amount
jug1_capacity = int(input("Enter capacity of jug1: "))
jug2_capacity = int(input("Enter capacity of jug2: "))
target_amount = int(input("Enter target amount: "))

water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
