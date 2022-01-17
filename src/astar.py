def h(start, x):
    '''
    Distance from start to current node
    '''
    X, Y = start
    X_, Y_ = x

    return (((X_-X)**2) + ((Y_-Y)**2))**.5


def f(h, g):
    '''
    h(x)+g(x)
    '''

    return h+g


def g(end, x):
    '''
    Distance from current node to the end
    '''

    X, Y = end
    X_, Y_ = x

    return (((X_-X)**2) + ((Y_-Y)**2))**.5


def find_neighbors(end, current):
    neighbors = []
    if current[0] != 0:
        neighbors.append([current[0]-1, current[1]])  # up

    if current[0] != end[0]:
        neighbors.append([current[0]+1, current[1]])  # down

    if current[1] != 0:
        neighbors.append([current[0], current[1]-1])  # left

    if current[1] != end[1]:
        neighbors.append([current[0], current[1]+1])  # right

    
    return neighbors


def astarsolver(maze):
    start = current = [1, 0] # the first 'free' block
    end = [len(maze)-2, len(maze[0])-1] # the last 'free' block

    points = []

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                points.append((i,j))

    points = [current]
    eliminated = [current]
    seen = [current]


    while len(current)>1:
        neighbors = find_neighbors(end, current)
        neighbors = [
                        n for n in neighbors\
                        if maze[n[0]][n[1]] == 1 and n not in eliminated and n not in seen
                    ]  # can't move into walls


        if points[-1] == end:
            break

        if len(neighbors) == 0:
            eliminated.append(points[-1])
            points.pop()
            if points == []:
                print('Maze cannot be solved')
                print('Probs cos :')
                print('\t1. The maze entries are not the top left and bottom right')
                print('\t2. The maze does not have a solution')

                break
            current = points[-1]
            seen.pop()

        else:      

            cost = [f(h(start, c), g(end, c)) for c in neighbors]

            current = neighbors[cost.index(min(cost))]

            points.append(current)
            seen.append(current)

    return points