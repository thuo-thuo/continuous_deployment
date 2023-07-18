# Assume this code is in a file called myfunc.py 

def f1(): 

    x = 1 

    y = 2 

    return x + y 

 

# This part is in a file called pytest_test.py 

from myfunc import f1 

 
def test_myfunc(): 


    assert f1() == 3