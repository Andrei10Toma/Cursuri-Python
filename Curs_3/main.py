from my_package import my_first_module
from my_package.my_second_module import my_second_var as some_var, my_function as my_second_function
from my_package.factorial import *

my_first_module.print_credentials()
my_first_module.my_function()
my_second_function()

print(fact(3))