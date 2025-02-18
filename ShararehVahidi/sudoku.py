import turtle
turtle.tracer(0)
t = turtle.Turtle()
t.hideturtle()
# t.speed(0)

def grid(W=300, N=9): # THIS FUNCTION DRAWS A GRID USING TURTL
    t.penup()
    zero= -W/2, W/2
    t.goto(zero)
    t.pendown()
    n = int(N ** 0.5)
    for i in range(4):
        t.pensize(5)
        t.forward(W)
        t.right(90)
    t.rt(90)
    for i in range(1, N):
        t.penup()
        t.goto(zero[0] + (i * W / N), zero[1])
        t.pendown()
        t.pensize(1)
        t.forward(W)

    for i in range(1, n):
        t.penup()
        t.goto(zero[0]+ (i * W / n), zero[1])
        t.pendown()
        t.pensize(3)
        t.forward(W)

    t.lt(90)
    for i in range(1, N):
        t.penup()
        t.goto(zero[0], zero[1]- (i * W / N))
        t.pendown()
        t.pensize(1)
        t.forward(W)

    for i in range(1, n):
        t.penup()
        t.goto(zero[0] , zero[1]- (i * W / n))
        t.pendown()
        t.pensize(3)
        t.forward(W)
    t.penup()

def map(W=300, N=9):  # THIS FUNCTION MAPS THE COORDINATES OF THE GRID
    n = int(N ** 0.5)
    border_width = 5
    w = (W - 2 * border_width) / N
    zero = -W / 2, W / 2
    x0 = zero[0] + w / 2
    y0 = zero[1] - w / 2 - 10

    point_num = 0
    square_num = 1
    coordinates = {}

    for r in range(n):
        for c in range(n):
            x = c * n * (w + 1.3) + x0
            y = y0 - r * n * (w + 1.3)
            for i in range(n):
                for j in range(n):
                    coordinates[point_num] = [(x, y), 0, square_num]
                    point_num += 1
                    y = y - (w + 1.3)
                x = x + w
                y = y0 - r * n * (w + 1.3)
            square_num += 1
    return coordinates



if __name__ == '__main__':
    import random
    grid(400, 9)
    coordinates = map(400,9)
    numbers = set(range(1, 10))
    cell_numbers = list(coordinates.keys())
    valid_values = {}
    i = 0
    while i < len(cell_numbers):
        cell_num = i
        print(f"cell_num: {cell_num}")
        square = set([value[1] for key, value in coordinates.items() if value[2] == coordinates[cell_num][2]])
        row = set([value[1] for key, value in coordinates.items() if value[0][0] == coordinates[cell_num][0][0]])
        column = set([value[1] for key, value in coordinates.items() if value[0][1] == coordinates[cell_num][0][1]])
        valid = numbers.difference(square.union(row, column))
        valid = list(valid)
        random.shuffle(valid)
        if valid :
            print("cell has valid numbers")
            print(f"valid: {valid}")
            num = valid.pop()
            print(f"remain valid:{valid}")
            valid_values[cell_num] = valid
            coordinates[cell_num][1] = num

        else: # Backtracking
            print("cell doesn't have valid numbers")
            for cell, valid_nums in reversed(valid_values.items()):
                if valid_nums :
                        print(f"to change: {cell, valid_nums}")
                        num = valid_nums.pop()
                        coordinates[cell][1] = num
                        for p in coordinates.keys():
                            if p > cell:
                                coordinates[p][1] = 0
                        break
                continue
            i = cell
        i += 1


    for key, point in coordinates.items():
        t.goto(coordinates[key][0])
        t.write(coordinates[key][1], align='center', font=("Arial", 12))
    turtle.done()


