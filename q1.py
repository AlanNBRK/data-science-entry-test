## Task 1
def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    x = x + y
    y = x - y
    x = x - y
   
    print(f"Swapped values successful: x= {x}, y= {y}")

## Task 2
print(swap("Apple", 10))  
print(swap(9, 17))        
