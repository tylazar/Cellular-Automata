import random
import numpy as np

def ca():
    # 64 Boolean - True(1) : '*'
    #            - False(0): '-'
    # Rule - each cell looks at its Moore neighborhood
    # Cell state takes on the minority state of the eight surveyed cells plus itself
    # If there are less than 2 or more than 3 alive, the current cell is alive
    
    # height and width of grid
    height = 32
    width = 64
    
    # list representing the current status of 64 cells - randomly generated
    ca = [[random.randint(0,1) for i in range(width)] for j in range(height)]
        
        
    # new cell values
    ca_new = ca
    
    # dictionary maps the cell value to a symbol
    dic = {0:'-', 1:'*'}
    
    # initial draw - step 0
    # print one row of ca_new at a time, changing to symbols as it goes
    print("Initial configuration: ")
    for i in range(height):
        symbol_row = [dic[e] for e in ca_new[i]]
        joined = ''
        for symbol in symbol_row:
            joined += symbol
        print(joined)
    print("\n")
    
    # additional 31 steps
    step = 1
    while (step < 32):
        ca_new = [([0] * width) for row in range(height)]
        neighbors = 0
        for i in range(0, height):
            for j in range(0, width):
                # add up values of neighbors
                neighbors = ca[(i - 1) % height][j] # north
                + ca[i][(j + 1) % width] # east
                + ca[(i + 1) % height][j] # south
                + ca[i][(j - 1) % width] # west
                + ca[(i - 1) % height][(j + 1) % width] # northeast
                + ca[(i + 1) % height][(j + 1) % width] # southeast
                + ca[(i + 1) % height][(j - 1) % width] # southwest
                + ca[(i - 1) % height][(j - 1) % width] # northwest
                
                # if current cell is True
                if ca[i][j] == 1:
                    # current alive cell is in the minority - maintain state
                    if neighbors < 4:
                        ca_new[i][j] = 1
                    # else, change state
                    else:
                        ca_new[i][j] = 0
                # else, if current cell is False
                else:
                    # current cell is in the majority - flip it
                    if neighbors < 5:
                        ca_new[i][j] = 1
                    else:
                        ca_new[i][j] = 0
        
        # update cell list
        ca = ca_new[:][:]
        
        # step count
        step += 1
    
    # draw final cell state
    print("Final configuration: ")
    for i in range(height):
        symbol_row = [dic[e] for e in ca_new[i]]
        joined = ''
        for symbol in symbol_row:
            joined += symbol
        print(joined)
    print("\n")

if __name__ == '__main__':
    ca()
                        
                        