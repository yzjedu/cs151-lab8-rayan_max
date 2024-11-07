# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
1. import random
2. set count to zero
3. set list_rolls to 11 elements by times it by 11
4. set times rolled to user input
5. while times rolled is not a digit
    - ask user to enter value for times rolled
6. typecast times rolled to integer
7. while count is less than times rolled
   8. set ran_int to a random number between 2 and 12
   9. increment the list list_rolls by rant_int minus 2 and then += 1
   10. then add 1 to count
11. output Rolling (value of times_rolled) pairs of dice
12. output (value of list_rolls)
13. for i in the range of numbers greater than 1 and less than 13
    14. set count_of_sum equal to list_rolls equal to 1 minus 2
    15. stars equals to * times count_of_sum
    16. if i is less then 10
        17. out 'sum of 0' plus i typecasted to a string plus a blank space then add the variable stars
    18. otherwise
        19. output 'sum of' plus i typecasted to a string plus a blank space then add the variable stars