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
    while (step < 32):
        ca_new = []
        # loop through 0 to 63 and store the current cell status in ca_new list
        for i in range(0, 64):
            # inside cells - check the neighbor cell state
            if i > 0 and i < 63:
                # current cell is in the majority - flip it
                if ca[i-1] or ca[i+1] == ca[i]:
                    if ca[i] == 0:
                        ca_new.append(1)
                    else:
                        ca_new.append(0)
                # else, current cell is in the minority - maintain state
                else:
                    ca_new.append(ca[i])
            
            # left most cell: check the second and last cells
            elif (i == 0):
                # current cell is in the majority - flip it
                if ca[1] or ca[63] == ca[i]:
                    if ca[i] == 0:
                        ca_new.append(1)
                    else:
                        ca_new.append(0)
                # else, current cell is in the minority - maintain state
                else:
                    ca_new.append(ca[i])
            
            # right most cell: check the first and second to last cell
            elif (i == 63):
                # current cell is in the majority - flip it
                if ca[0] or ca[62] == ca[i]:
                    if ca[i] == 0:
                        ca_new.append(1)
                    else:
                        ca_new.append(0)
                # else, current cell is in the minority - maintain state
                else:
                    ca_new.append(ca[i])
        
        # draw current cell state
        print(''.join([dic[e] for e in ca_new]))
        
        # update cell list
        ca = ca_new[:]
        
        # step count
        step += 1
        
if __name__ == '__main__':
    ca()