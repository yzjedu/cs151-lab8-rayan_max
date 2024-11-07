
import random
# Initialzing count and list_rolls
count = 0
list_rolls = [0] * 11  # Only 11 elements since sums go from 2 to 12
# Asking the user how many times they want to roll
times_rolled = input("How many times do you want to roll? ")
#error checking making sure that there input is a digit
while not times_rolled.isdigit():
    times_rolled = input("Please enter a valid number for how many times to roll: ")
times_rolled = int(times_rolled)  #Coverting the amount times rolled to a int
# Rolling the dice a certain amount of times
while count < times_rolled:
    # The simulation of rolling the dice and adding the results
    ran_int = random.randint(2,12)
    # Increment the count for the rolled sum
    list_rolls[ran_int - 2] += 1
    # Increment the loop counter
    count += 1
# Printing the list of counts
print(f"\nRolling {times_rolled} pairs of dice")
print(list_rolls)
# This is displaying how many times each number was rolled
for i in range(2, 13):
    # Finding out how many times i was rolled
    count_of_sum = list_rolls[i - 2]

    # Creating stars as a string because of the rubric
    stars = '*' * count_of_sum

    # Finnaly printing the results in the most proper way
    if i < 10:
        print("Sum of 0" + str(i) + " " + stars)  # Adding leading zero for single-digit sums
    else:
        print("Sum of " + str(i) + " " + stars)
