# Vacuum Cleaner using Simple Reflex Agent
# T.C = O(n) S.C=O(n)
def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"
# Environment
location = "A"
rooms = {"A": "Dirty", "B": "Dirty"}
while rooms["A"]=="Dirty" or rooms["B"]=="Dirty":
    print("Location:", location)
    print("Room status:", rooms[location])

    action = vacuum_agent(location, rooms[location])
    print("Action:", action)

    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    else:
        location = "A"
print("Both rooms are clean!")


# Algorithm
# 1. Start with two rooms, A and B.
# 2. Check the agent's current location and room status.
# 3. If the room is dirty, perform the Suck action.
# 4. If the room is clean and the agent is at A, move right.
# 5. Otherwise, move left.
# 6. Stop when both rooms are clean.
# How it works: A simple reflex agent selects an action using the current percept only. It does not maintain an internal memory of previous actions.

# Complexity: Each action takes \(O(1)\) time. For \(k\) actions, the total time is \(O(k)\), and the environment uses \(O(1)\) space.*#