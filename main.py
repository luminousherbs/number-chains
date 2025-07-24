from math import *

def interpret(code: str):
    parts: list[str] = code.split(" => ")
    function_input: str = parts[0]
    function_body: str = parts[1]

    # handle cases where the function input is an expression
    try:
        function_input = eval(function_input)
        # for now, assume the function body never contains selection {}
        def transform(n: float) -> float:
            return float(eval(function_body) if n == float(function_input) else n)

    # handle cases where the function input is a variable
    except ValueError:
        # for now, assume the function body never contains selection {}
        def transform(n: float) -> float:
            return float(eval(function_body.replace(function_input, f"({str(n)})")))
    
    return transform

print(interpret(input())(float(input())))
