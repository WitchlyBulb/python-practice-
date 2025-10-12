#Drill 1 — Basic Push & Pop
stack = []      # empty stack
stack.append("Mia")    # push
stack.append("Sam")
stack.append("Ana")
print(stack)    # what does this show?
# Output --> ["Mia", "Sam", "Ana"]
stack.pop()     # remove top (Ana)
print(stack) 
# Output --> ["Mia", "Sam"]

# Drill 2 — Peek (look at top without removing)
stack = ["Mia", "Sam", "Ana"]
print("Top of stack:", stack[-1])
# Output --> "Ana"

# Drill 3 — Patient Notes Undo Simulation
actions = []
actions.append("Add HR")
actions.append("Update Temp")
actions.append("Correct O2")
print("Actions:", actions)
#Output --> Actions:["Add HR", "Update Temp", "Correct O2"]

# Undo last action
last = actions.pop()
print("Undo:", last) 
print("Remaining:", actions)
# Output:
# "Correct O2"
#"Add HR", "Update Temp"

