import mymodule
mymodule.printer("Sum is")
mymodule.sum(2,3)

from mymodule import printer

printer("Sum is with printer")

from mymodule import *

import sum
mylist = [1,2,3,4]
result = sum.addnum(mylist)
print(result)

import mymodule
x=0
x=mymodule.counter(x)
print(x)

from imp import reload
reload(mymodule)


import mypackage
mypackage.package1.fun1()
mypackage.package2.fun2()
