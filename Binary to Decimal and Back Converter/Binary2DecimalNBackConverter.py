from IPython.display import clear_output

def dec2bi(dec):
    out = ''
    i = dec
    
    while i >= 1:
        out = str(i%2) + out
        i = int(i/2)
    
    else:
        out = i
    
    return out

def bi2dec(bi):
    out = 0
    n = 0
    
    for i in str(bi)[::-1]:
        if i == '1':
            out += 2**n
            n += 1
        else:
            n += 1
    
    return out

def main():
    print "Welcome to decimal/binary converter."
    print "Enter 'D' for decimal to binary, Enter 'B' for binary to decimal.\n"
    
    user_input = str(raw_input('D/B: ')).upper()
    
    while user_input is not str:
        if user_input == 'D':
            try:
                print dec2bi(int(raw_input('Enter your decimal to convert to binary: ')))
                break
            except:
                print 'Please enter interger number only.'
                
        elif user_input == 'B':
            try:
                print bi2dec(int(raw_input('Enter your binary to convert to decimal: ')))
                break
            except:
                print 'Please enter in correct binary number.'
                
if __name__ == '__main__':
    clear_output()
    while True:
        main()
        if str(raw_input("Enter 'R' to run again: ")).upper() == 'R':
            clear_output()
        else:
            clear_output()
            break
