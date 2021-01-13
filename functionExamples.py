def simple_function():
    print("simple_function")


def function_with_parameter(parameter_value):
    print(f'function_with_parameter({parameter_value})')


def function_with_default_parameter(default_parameter_value='default'):
    print(f'function_with_default_parameter({default_parameter_value})')


def function_name_parameter(param_one, param_two):
    print(f'function_name_parameter({param_one}, {param_two})')


def function_with_return(number):
    return number * number


print("start")
simple_function()
function_with_parameter('hi')
function_with_default_parameter('new pass')
function_with_default_parameter()
function_name_parameter(param_two=2, param_one=1)
function_name_parameter(1, param_two=2)
print(function_with_return(2))
print('end')
