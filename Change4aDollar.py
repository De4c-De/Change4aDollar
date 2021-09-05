# -*- coding: utf-8 -*-
"""Created on Wed Aug 25 20:10:37 2021

@author: de4cd
make chage for a Dollar
"""

count = 0
for half in range(3):
    for quart in range(5):
        dimes= (10)
        nickl = (5)
        penny = (1)
    
    
    
    
    
        amt = 50*half + 25*quart + 10*dimes + 5*nickl + penny
        if amt == 100: count +=1
        
print('number of ways to make change is {}' .format(amt))