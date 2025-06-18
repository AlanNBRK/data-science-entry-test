# Task 1 
def find_and_replace(lst, find_val, replace_val):
    if not isinstance(lst, list):
        raise TypeError("lst must be a list")
    return [replace_val if x == find_val else x for x in lst]

# Task 2
# Scenario 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)  

# Scenario 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(result2)  
