## Task 1
def find_first_negative(lst):
    index = 0
    while index < len(lst):
        if lst[index] < 0:
            return lst[index]
        index += 1
    return "No negatives"

## Task 2
# Scenario 1
print(find_first_negative([3, 5, -1, 7, -2, 8]))  

# Scenario 2
print(find_first_negative([2, 10, 7, 0]))         
