import random

def ca():
    # 64 Boolean - True(1) : '*'
    #            - False(0): '-'
    # Rule - each cell looks at itself and its two nearest neighbors
    # Cell state takes on the majority state of the three surveyed cells
    
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
    # note: can make into 3 cases (inside and not inside) by using mod
    while (step < 32):
        ca_new = []
        # loop through 0 to 63 and store the current cell status in ca_new list
        for i in range(0, 64):
            # inside cells - check the neighbor cell state
            if i > 1 and i < 62:
                trues = 0
                falses = 0
                # check the value of each neighbor
                for cell in range(i-2, i+3):
                    if ca[cell] == 1:
                        trues += 1
                    else:
                        falses += 1
                # if there are more True, append False
                if trues > falses:
                    ca_new.append(0)
                # if there are more False, append True
                else:
                    ca_new.append(1)
                    
            
            #second to left most cell: check first, third, fourth, and last cells
            elif (i == 1):
                trues = 0
                falses = 0
                # check the value of each neighbor individually, so I don't have to come up with a better way
                if ca[0] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[1] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[2] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[3] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[63] == 1:
                    trues += 1
                else:
                    falses += 1
                # if there are more True, append False
                if trues > falses:
                    ca_new.append(0)
                # if there are more False, append True
                else:
                    ca_new.append(1)
                
            
            # left most cell: check the second, third, last, and second to last cells
            elif (i == 0):
                trues = 0
                falses = 0
                # check the value of each neighbor individually, so I don't have to come up with a better way
                if ca[0] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[1] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[2] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[63] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[62] == 1:
                    trues += 1
                else:
                    falses += 1
                # if there are more True, append False
                if trues > falses:
                    ca_new.append(0)
                else:
                    ca_new.append(1)
            
            # second to right most cell: check fourth to last, third to last, last, and first cells
            elif (i == 62):
                trues = 0
                falses = 0
                # check the value of each neighbor individually, so I don't have to come up with a better way
                if ca[60] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[61] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[62] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[63] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[0] == 1:
                    trues += 1
                else:
                    falses += 1
                # if there are more True, append False
                if trues > falses:
                    ca_new.append(0)
                else:
                    ca_new.append(1)
                
            
            # right most cell: check third to last, second to last, first, and second cells
            elif (i == 63):
                trues = 0
                falses = 0
                # check the value of each neighbor individually, so I don't have to come up with a better way
                if ca[61] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[62] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[63] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[0] == 1:
                    trues += 1
                else:
                    falses += 1
                if ca[1] == 1:
                    trues += 1
                else:
                    falses += 1
                # if there are more True, append False
                if trues > falses:
                    ca_new.append(0)
                else:
                    ca_new.append(1)
        
        # draw current cell state
        print(''.join([dic[e] for e in ca_new]))
        
        # update cell list
        ca = ca_new[:]
        
        # step count
        step += 1
        
if __name__ == '__main__':
    ca()