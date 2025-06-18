## Task 1

def string_reverse(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]

## Task 2

# Scenario 1
print(string_reverse("Hello World"))  

# Scenario 2
print(string_reverse("Python"))       
