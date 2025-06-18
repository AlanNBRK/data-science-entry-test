## Task 1

def check_divisibility(num, divisor):
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return False  
    
    if divisor == 0:
        return False  
    
    return num % divisor == 0


## Task 2

# Scenario 1
print(check_divisibility(10, 2))  

# Scenario 2
print(check_divisibility(7, 3))   