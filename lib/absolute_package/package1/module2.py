def function1():
    print('Function 1 in module 2')


from .module1 import function1
from .. import module3

function1()
module3.function1()