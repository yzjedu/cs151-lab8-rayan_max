import random
count = 0
times_rolled = input("How many times do you rolled? ")
times_rolled = int(times_rolled)
while not times_rolled.isdigit():
  times_rolled = input("How many times do you rolled? ")
while count < times_rolled:
    random_int = random.randint(2,12)
    list = [].append(random_int)
    count = count + 1
print(list)
