'''You are traveling the seven seas. 
Given a string representing land, find the character
 ‘X’ (marks the spot) and return the index of the treasure! 
 Return -1 if no treasure exists. If there are multiple treasures, 
 return the one with the smallest index.'''

def treasure_hunt(land_str):
	return land_str.find("X")

print(treasure_hunt("no treasure"))
print(treasure_hunt("X marks the spot X"))

# returns -1 if X not there