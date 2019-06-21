import random

def ca():
    # 64 Boolean - True(1) : '*'
    #            - False(0): '-'
    # Rule - the current cell looks at 2 neighbors to the left and right
    # If all 4 are True, the current cell status becomes True ('*')
    # If 3 are True, the current cell status retains its state
    # If 2 or fewer are true, the current cell status becomes False ('-')
    
    # list representing the current status of 64 cells - randomly generated
    ca = []
    
    while len(ca) < 64:
        ca.append(random.randint(0,1))
    
    # new cell values
    ca_new = ca[:]
    
    # dictionary maps the cell value to a symbol
    dic = {0:'-', 1:'*'}
    
    # initial draw - step 0
    print(''.join([dic[e] for e in ca_new]))
    
    # additional 31 steps
    step = 1
    while step < 32:
        ca_new = []
        # loop through 0 to 63 and store the current cell status in ca_new list
        for i in range (0,64):
            # inside cells - check the 4 neighbor cell states
            if i > 1 and i < 62:
                # all 4 are True - change state to True
                if ca[i-1] + ca[i-2] + ca[i+1] + ca[i+2] == 4:
                    ca_new.append(1)
                # 3 are True - maintain current state
                elif ca[i-1] + ca[i-2] + ca[i+1] + ca[i+2] == 3:
                    ca_new.append(ca[i])
                # 2 or fewer are True - change state to False
                else:
                    ca_new.append(0)
            
            #second to left most cell: check first, third, fourth, and last cells
            elif (i == 1):
                # all 4 are True - change state to True
                if ca[0] + ca[2] + ca[3] + ca[63] == 4:
                    ca_new.append(1)
                # 3 are True - maintain current state
                elif ca[0] + ca[2] + ca[3] + ca[63] == 3:
                    ca_new.append(ca[i])
                # 2 or fewer are True - change state to False
                else:
                    ca_new.append(0)
            
            # left most cell: check the second, third, last, and second to last cells
            elif (i == 0):
                # all 4 are True - change state to True
                if ca[1] + ca[2] + ca[63] + ca[62] == 4:
                    ca_new.append(1)
                # 3 are True - maintain current state
                elif ca[1] + ca[2] + ca[63] + ca[62] == 3:
                    ca_new.append(ca[i])
                # 2 or fewer are True - change state to False
                else:
                    ca_new.append(0)
            
            # second to right most cell: check fourth to last, third to last, last, and first cells
            elif (i == 62):
                # all 4 are True - change state to True
                if ca[60] + ca[61] + ca[63] + ca[0] == 4:
                    ca_new.append(1)
                # 3 are True - maintain state
                elif ca[60] + ca[61] + ca[63] + ca[0] == 3:
                    ca_new.append(ca[i])
                # 2 or fewer are True - change state to False
                else:
                    ca_new.append(0)
            
            # right most cell: check third to last, second to last, first, and second cells
            elif (i == 63):
                # all 4 are True - change state to True
                if ca[61] + ca[62] + ca[0] + ca[1] == 4:
                    ca_new.append(1)
                # 3 are True - maintain state
                elif ca[61] + ca[62] + ca[0] + ca[1] == 3:
                    ca_new.append(ca[i])
                # 2 or fewer are True - change state to False
                else:
                    ca_new.append(0)
                    
        # draw current cell state
        print(''.join([dic[e] for e in ca_new]))
        
        # update cell list
        ca = ca_new[:]
        
        # step count
        step += 1

if __name__ == '__main__':
    ca()
                