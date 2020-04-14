# Print out all of the strings in the following array in alphabetical order, each on a separate line.
arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

sorted_arr = sorted(arr)

for i in sorted_arr:
    print(i)


print()
print()


# Print out all of the strings in the following array in alphabetical order sorted by the middle letter of each string, each on a separate line. If the word has an even number of letters, choose the later letter, i.e. the one closer to the end of the string.
arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
# 'Cha Cha'
# 'Paso Doble'
# 'Viennese Waltz'
# 'Waltz'
# 'Samba'
# 'Rumba'
# 'Tango'
# 'Foxtrot'
# 'Jive'
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

8
4
# len(string) // 2

9 // 2
4

123456789

def func(string):
    return string[len(string) // 2]

arr.sort(key = func)

for i in arr:   
    print(i)

print()
print()


import random

def generate_island_matrix(width, height, density):
    matrix = []
    for _ in range(height):
        matrix.append([0] * width)
    for x in range(width):
        for y in range(height):
            # print(random.random() < density)
            if random.random() < density:
                matrix[y][x] = 1
    return matrix

# generate_island_matrix(10, 10, 0.5)

# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

def nsew(row_index, col_index, islands, visited):
    # North
    # check if there is room to go north
    if row_index > 0:
        # check if we've already been here
        if visited[row_index - 1][col_index] == 0:
            # mark that we've been here and recurse on the neighbors
            if islands[row_index - 1][col_index] == 1:
                visited[row_index - 1][col_index] = 1
                nsew(row_index - 1, col_index, islands, visited)
    
    # South
    # check if there is room to go south
    if row_index < len(islands) - 1:
        # check if we've been here
        if visited[row_index + 1][col_index] == 0:
            # mark we've been here and recurse on the neighbors
            if islands[row_index + 1][col_index] == 1:
                visited[row_index + 1][col_index] = 1
                nsew(row_index + 1, col_index, islands, visited)
    
    # East
    # check if there is room to go east
    if col_index < len(islands[row_index]) - 1:
        # check if we've been here
        if visited[row_index][col_index + 1] == 0:
            # mark that we've been here and recurse on neighbors
            if islands[row_index][col_index + 1] == 1:
                visited[row_index][col_index + 1] = 1
                nsew(row_index, col_index + 1, islands, visited)

    # West
    # check if we can go west
    if col_index > 0:
        # check if we've already been west
        if visited[row_index][col_index - 1] == 0:
            # mark that we've been here and recurse on neighbors
            if islands[row_index][col_index - 1] == 1:
                visited[row_index][col_index - 1] = 1
                nsew(row_index, col_index - 1, islands, visited)


def island_counter(islands):
    # count the number of islands
    counter = 0
    # create a visited matrix of zeroes the same size as islands
    visited = generate_island_matrix(len(islands[0]), len(islands), density=0)
    # traverse the matrix
    for row_index in range(len(islands)):
        for col_index in range(len(islands[row_index])):
            # check if we've hit an island that we hadn't hit before
            if islands[row_index][col_index] == 1 and visited[row_index][col_index] == 0:
                # counter up by 1
                counter += 1
                # mark the spot as visited
                visited[row_index][col_index] = 1
                # mark all connected spots of the island as visited
                nsew(row_index, col_index, islands, visited)
    return counter

islands = generate_island_matrix(6, 6, .5)
for row in islands:
    print(row)
print(island_counter(islands)) # returns 4