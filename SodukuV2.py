class Matrix:
    def __init__(self):
        self.mat = []  

    def GetMatrix(self):
        with open(r"C:\Users\Marios\Desktop\Sdk.txt") as f:
            for line in f:
                row = []
                for n in line.split():
                    row.append(int(n))
                self.mat.append(row)



    def CheckRow(self):
        a = []
        for r in range(9):
            for c in range(9):
                n = self.mat[r][c]
                if n in a:
                    print("Soduku is invalid,",n ,"appears more than one time")
                    return
                else:
                    a.append(n)
            a.clear()
            

    def CheckColum(self):
        b = []
        for c in range(9):
            for r in range(9):
                n1 = self.mat[r][c]
                if n1 in b:
                    print("Soduku is invalid,",n1 ,"appears more than one time")
                    return
                else:
                    b.append(n1)
            b.clear()

            

    def CheckBox(self):
        for box_row in range(3):
            for box_col in range(3):
                c = []
                for row in range(3):
                    for col in range(3):
                        n2 = self.mat[box_row * 3 + row][box_col * 3 + col]
                        if n2 in c:
                            print("Soduku is invalid,",n2 ,"appears more than one time")
                            return
                        else:
                            c.append(n2)
                        c.clear()

               

m = Matrix()      
m.GetMatrix()     
m.CheckRow()
m.CheckColum()
m.CheckBox()