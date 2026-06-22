class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def CheckRow(self):
        a = []

        for r in range(9):
            for c in range(9):
                n = self.mat[r][c]
                a.append(n)

            a1 = set(a)

            if len(a) != len(a1):
                print("Soduku is invalid")
                break
            else:
                a.clear()
                a1.clear()
    
    def CheckColum(self):
        b = []

        for c in range(9):
            for r in range(9):
                n1 = self.mat[r][c]
                b.append(n1)

            b1 = set(b)

            if len(b) != len(b1):
                print("Soduku is invalid")
                break
            else:
                b.clear()
                b1.clear()


    def CheckBox(self):
        for box_row in range(3):
            for box_col in range(3):
                c = []

                for row in range(3):
                    for col in range(3):
                        n2 = self.mat[box_row * 3 + row][box_col * 3 + col]  
                        c.append(n2)

                c1 = set(c)  

                if len(c) != len(c1):  
                    print("Sudoku is invalid")
                    return
                else:
                    pass


