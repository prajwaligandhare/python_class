#4. Apne 3 functions ko poore docstring + type hints ke saath document karo.

def my_function(a: int, b: int, c: int) -> int:
    """
       create three functions & apply docstring & hints.

       Args: 
           write a function name
           my_functions(a, b, c)

       Returns:   
              print the result using
              docstring & hints. 
    """

    return print("The sum of the numbers is: ", a + b + c)

my_function(2, 3, 5)    


help(my_function)

my_function.__doc__