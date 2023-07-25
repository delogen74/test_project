field = [[" "] * 3 for i in range(3)]
field[0][1] = "X"

def show():
    print(f" 0 1 2 ")
    for i in ran(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")

show()
