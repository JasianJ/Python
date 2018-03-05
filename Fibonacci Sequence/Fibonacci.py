from IPython.display import clear_output

def findnum(n):
    out = []
    a, b = 0, 1
    
    for i in range(n):
        out.append(a)
        a, b = b, a+b
        
    return out
def nth(n):
    a, b = 0, 1
    
    for i in range(n):
        a, b = b, a+b
        
    return a
    
on = True
print 'Enther a number to generate Fibonacci sequence to that number.'
while on == True:
    print 'Option 1 for display sequence\nOption 2 for display Nth number'
    op = int(raw_input('Press 1 or 2: '))
    if op == 1:
        n = int(raw_input('Display Fibonacci sequence, starts from 0, upto '))
        if n > 20:
            print 'Sorry your sequence is too long. Please use option 2.'
            
        else:
            print findnum(n)
        
    elif op == 2:
        n = int(raw_input('Display Nth number of Fibonacci sequence starts from 0. N = '))
        print nth(n-1)
        
    again = str(raw_input('Again? Y/N: ')).upper()
    if again == 'Y':
        clear_output()
        pass
    elif again == 'N':
        clear_output()
        on = False
        break
    else:
        again = str(raw_input('Y or N only. Again? Y/N: ')).upper()
        clear_output()
        
