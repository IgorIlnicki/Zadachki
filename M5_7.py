from typing import Callable

def power(exponent: int) -> Callable[[int], int]:
    print(f"exponent = {exponent}")
   
    def inner(base: int) -> int:
        print(f"base = {base}")
        return print(f"base ** exponent {base ** exponent}")
    
    return inner

# Використання
square = power(2)
# cube = power(3)

print(square(4)) 
# print(cube(4))