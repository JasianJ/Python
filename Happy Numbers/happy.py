from collections import Counter
from IPython.display import clear_output


def happynum(n):
    num = n
    
    if num < 0 or type(num) is not int:
        return 'Number must be positive interger.'
    
    cycle = []
    while True:
        cycle_counter = Counter(cycle)
        
        if len(cycle_counter.most_common(1)) == 0:
            pass
        else:
            if cycle_counter.most_common(1)[0][1] == 4:
                return '{} is not happy number!'.format(n)
        
        if num < 10:
            num = num**2
            
            if num == 1:
                return '{} is a happy number!'.format(n)
        elif num >= 10:
            num_list = []
            temp_num = 0
            
            for i in str(num):
                num_list.append(int(i)**2)
            
            for i in num_list:
                temp_num += i
            
            num = int(temp_num)
            
        cycle.append(num)

def main():
    print "Check your number if it's happy or not!"
    
    while True:
        n = int(raw_input('Enter your number: '))
        
        try:
            print happynum(n)
        except:
            print 'You must enter number!'
        finally:
            while True:
                i = str(raw_input('Try again? Y/N ')).upper()
                
                if i == 'Y':
                    break
                elif i == 'N':
                    clear_output()
                    return None
                else:
                    print 'Y/N only.\n'

if __name__ == '__main__':
    main()
    
for i in xrange(1,16):
    print happynum(i)
