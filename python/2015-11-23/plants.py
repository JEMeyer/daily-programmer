import sys

# Read in populat and starting pland size. Initialize weeks and fruit count
population, plants = int(sys.argv[1]), int(sys.argv[2])
weeks, fruit = 1, 0

# While we don't have enough food, go another week, add up new fruit count from
# plants, increment total plants planted with the seeds from this week
while (fruit < population):
    weeks += 1
    fruit += plants
    plants += fruit
        
print(weeks)