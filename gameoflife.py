from time import sleep
from copy import deepcopy
from random import randint
from matplotlib import pyplot as plt

N=int(input("Enter Grid Size - "))
sleeptime = float(input("Enter Sleep Time - "))

grid = [[randint(0,1) for j in range(N)] for i in range(N)]

plt.ion()
fig, ax = plt.subplots()
axim = ax.imshow(grid, cmap="Greys")

print(grid)
i = 0
while True:
    ngrid = deepcopy(grid)
    for y in range(N):
        for x in range(N):
            n = 0
            for a in range(-1,2):
                for b in range(-1,2):
                    n += grid[(y+a)%N][(x+b)%N]
            n -= grid[y][x]
            if grid[y][x] and n < 2:
                ngrid[y][x] = 0
            if grid[y][x] and n > 3:
                ngrid[y][x] = 0
            if not grid[y][x] and n == 3:
                ngrid[y][x] = 1
    grid = deepcopy(ngrid)
    i+=1
    print(i)
    axim.set_data(grid)
    fig.canvas.flush_events()
    sleep(sleeptime)
