class Matrix:
    def __init__(self):
        self.mat = []  

    def GetMatrix(self):
        with open(r"C:\Users\Marios\Desktop\Sdk.txt") as f:
            for line in f:
                row = []
                for n in line.split():
                    row.append(int())
                self.mat.append(row)

    def CheckRow(self):
        a = []
        for r in range(9):
            for c in range(9):
                n = self.mat[r][c]
                a.append(n)

            a1 = set(a)
            if len(a) != len(a1):
                print("Sudoku is invalid")
                return
            else:
                a.clear()

    def CheckColum(self):
        b = []
        for c in range(9):
            for r in range(9):
                n1 = self.mat[r][c]
                b.append(n1)

            b1 = set(b)
            if len(b) != len(b1):
                print("Sudoku is invalid")
                return
            else:
                b.clear()

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


m = Matrix()      
m.GetMatrix()     
m.CheckRow()
m.CheckColum()
m.CheckBox()