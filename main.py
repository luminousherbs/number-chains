from math import *

def substitute(expression: str, variable: str, value: str) -> float:
    return float(eval(expression.replace(variable, f"({value})")))

def interpret(code: str):
    parts: list[str] = code.split(" => ")
    function_input: str = parts[0]
    function_body: str = parts[1]
    
    # handle selection {}
    if "{" in function_body:
        selection_parts: list[str] = function_body.split("[")
        condition: str = selection_parts[0].replace("{", "").replace("}", "")
        true_body: str = selection_parts[1].replace("]", "")
        false_body: str = selection_parts[2].replace("]", "")
        substitute("n < 20 ", "n", "2")
        # "{x < 20} ", "x * 2] ", "x * 3]"
        def transform(n: float) -> float:
            return substitute((true_body if substitute(condition, function_input, str(n)) else false_body), function_input, str(n))
        return transform

    # handle cases where the function input is an expression
    try:
        function_input: str = eval(function_input)
        # for now, assume the function body never contains selection {}
        def transform(n: float) -> float:
            return float(eval(function_body) if n == float(function_input) else n)

    # handle cases where the function input is a variable
    except NameError:
        # for now, assume the function body never contains selection {}
        def transform(n: float) -> float:
            return float(eval(function_body.replace(function_input, f"({str(n)})")))
    
    return transform

print(interpret(input())(float(input())))
