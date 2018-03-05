from IPython.display import clear_output


def cc(n):
    count = 0
    
    if n <= 1:
        return 'Number need to be larger than 1.\n'
    
    while n > 1:
        if n%2 == 0:
            n = n / 2
        else:
            n = (n*3) + 1
        
        count += 1
    
    return count

def main():
    while True:
        print 'Collatz Conjecture of your number.'
        try:
            print cc(int(raw_input('Your number is? ')))
            break
        except:
            print 'Please enter interger number only.'
            
if __name__ == '__main__':
    while True:
        main()
        if str(raw_input("Enter 'Q' to quit or any letter to again. ")).upper() == 'Q':
            clear_output()
            break
        else:
            clear_output()
