import pyflowchart
import astunparse 
import ast
import inspect


source_list = inspect.getsourcelines(pyflowchart)
print(source_list)
f = open('test_logs.txt', 'a+')
f.write(str(source_list))
print(pyflowchart.__file__)