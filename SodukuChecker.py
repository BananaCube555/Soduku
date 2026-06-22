mat = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],

    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],

    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]





def CheckRow():
    a = []

    for r in range(9):
        for c in range(9):
            n = mat[r][c]
            a.append(n)

        a1 = set(a)

        if len(a) != len(a1):
            print("Soduku is invalid")
            break
        else:
            a.clear()
            a1.clear()
            

def CheckColum():
    b = []

    for c in range(9):
        for r in range(9):
            n1 = mat[r][c]
            b.append(n1)

        b1 = set(b)

        if len(b) != len(b1):
            print("Soduku is invalid")
            break
        else:
            b.clear()
            b1.clear()

                        


def CheckBox():
    for box_row in range(3):
        for box_col in range(3):
            c = []

            for row in range(3):
                for col in range(3):
                    n2 = mat[box_row * 3 + row][box_col * 3 + col]  
                    c.append(n2)

            c1 = set(c)  

            if len(c) != len(c1):  
                print("Sudoku is invalid")
                return
            else:
                pass



CheckRow()
CheckColum()
CheckBox()