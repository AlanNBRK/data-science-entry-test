## Task 1

def update_dictionary(dct, key, value):
    if key in dct:
        print(dct[key])  
    dct[key] = value    
    return dct          

## Task 2 
# Scenario 1
result1 = update_dictionary({}, "name", "Alice")
print(result1)  

# Scenario 2
result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)  

