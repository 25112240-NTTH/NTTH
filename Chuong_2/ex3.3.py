# Cau 1

def draw_horiziontal():
    print("+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+")
def draw_vertical():
    print("|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|")
def draw_grid():
    draw_horiziontal()
    draw_vertical()
    draw_vertical()
    draw_vertical()
    draw_vertical()
    draw_horiziontal()
    draw_vertical()
    draw_vertical()
    draw_vertical()
    draw_vertical()
    draw_horiziontal()
draw_grid()

# Cau 2

def draw_4x4_grid():
    line_h = ('+'+'-' * 4)*4 + '+'
    line_v = ('|'+' ' * 4)*4 + '|'
    for i in range(4):
        print(line_h)
        for i in range(4):
            print(line_h)
            print(line_v)
            print(line_v)
            print(line_v)
            print(line_v)
            print(line_h)
draw_4x4_grid()