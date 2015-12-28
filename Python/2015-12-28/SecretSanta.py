import random

def findMatches(people):
    '''
    Input:
        people: List of strings. Whole list of all individuals
    Returns: List of tuples for matched secret santas
    '''
    # End result, list of string tuples
    matches = []
    
    #Loop through list of people and match with next person in list
    for i, person in enumerate(people):
        if (i == len(people) - 1):
            matches.append([person, people[0]])
        else:
            matches.append([person, people[i+1]])
    
    return matches

# Open input data file
f = open('input.txt', 'r')

# Holds each line. Second array for family members
allPeople = []

# Read in each line. Each line is a list of names
for i, rawLine in enumerate(f):
    line = rawLine.split()
    
    # Add each person to allPeople, and append a double digit string at the end
    # We will use this string to determine if two family members match
    for person in line:
        allPeople.append(person + str("{0:0=2d}".format(i)))   
        
# Loop until we get a good set of matches      
while (True):
    # Shuffle our list.
    random.shuffle(allPeople)
    
    # Get our list of tuples for potential matches
    matches = findMatches(allPeople)
    
    # See if any family members get matched. If they do, re-loop
    for match in matches:
        if match[0][-2:] == match[1][-2:]:
            continue
            
    # We made it this far so there are no family members matched with each other
    break
    
# We finally have a good set. Print out the santa pairs after removing IDs    
for match in matches:
    match[0] = match[0][:-2]
    match[1] = match[1][:-2]
    print(match[0] + ' ==> ' + match[1])