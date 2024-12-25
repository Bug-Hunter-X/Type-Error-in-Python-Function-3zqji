def function(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        try:
            return float(a) + float(b)
        except ValueError:
            return "Error: Inputs must be numeric or convertible to numeric."

result = function(5, '10')
print(result)

result = function(5,10)
print(result)

result = function('5','10')
print(result)

result = function('a','10')
print(result)