>>> from mypackage import package1
>>> package1.fun1()
Fun1 printing
>>> from mypackage import package2
>>> package2.fun2()
Fun2 printing
>>>    
>>> import mypackage
>>> mypackage.package1.fun1()
Fun1 printing
>>> mypackage.package2.fun2()
Fun2 printing         