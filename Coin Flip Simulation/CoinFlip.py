import random
from IPython.display import clear_output


def coinflip(n):
    out = []
    for i in xrange(n):
        state = random.randint(1,2)
        
        if state == 1:
            out.append('Head')
            
        else:
            out.append('Tail')
    
    for i in xrange(len(out)):
        out[i] = str(out[i])
    
    return ', '.join(out)

def main():
    clear_output()
    while True:
        try:
            i = int(raw_input('Enter number of flips: '))
            print coinflip(i)
            break
        except:
            clear_output()
            print 'Enter number only.'
            
if __name__ == '__main__':
    main()            
    
coinflip(4)
