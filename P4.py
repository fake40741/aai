# # Tower of Hanoi without Recursion
# n = int(input("Enter number of disks: "))
# A = list(range(n, 0, -1))  # Source rod
# B = []                    # Auxiliary rod
# C = []                    # Destination rod
# # Rod names and lists
# rods = {"A": A, "B": B, "C": C}
# # Total number of moves
# total = 2 ** n - 1
# # Swap destination and auxiliary for even disks
# if n % 2 == 0:
#     rods["B"], rods["C"] = rods["C"], rods["B"]
# for i in range(1, total + 1):
#     # Select the legal rod pair
#     if i % 3 == 1:
#         x, y = "A", "C"
#     elif i % 3 == 2:
#         x, y = "A", "B"
#     else:
#         x, y = "B", "C"
#     # Move the smaller top disk legally
#     if not rods[x]:
#         rods[x].append(rods[y].pop())
#         print("Move disk from", y, "to", x)

#     elif not rods[y]:
#         rods[y].append(rods[x].pop())
#         print("Move disk from", x, "to", y)
#     elif rods[x][-1] < rods[y][-1]:
#         rods[y].append(rods[x].pop())
#         print("Move disk from", x, "to", y)
#     else:
#         rods[x].append(rods[y].pop())
#         print("Move disk from", y, "to", x)
# print("Tower of Hanoi completed!")
#T.C=O(2^n) S.C=O(n)
n=int(input("Enter no. of disks"))
source='A'
auxiliary='B'
destination='C'
moves=2**n-1
if n%2==0:
    auxiliary,destination=destination,auxiliary
for i in range(1,moves+1):
    if i%3==1:
        src,dest=source,destination
    elif i%3==2:
        src,dest=source,auxiliary
    else:
        src,dest=auxiliary,destination        
    print("move disk from:",src,"to",dest)
print("total moves:",moves)    
# Algorithm
# 1. Create three rods: source, auxiliary, and destination.
# 2. Calculate the total moves using \(2^n-1\).
# 3. Repeat the moves using a loop.
# 4. Select two rods according to the move number.
# 5. Move the smaller top disk legally between those rods.
# 6. Stop after all moves are completed.
# Complexity: Time \(O(2^n)\); space \(O(n)\) for storing the disks.

# Viva point: This program solves the problem iteratively using legal state transitions. It does not use recursion.