#This is a python based application 
#GUI will be implemented soon
#here we use use oop for our program
import random
import numpy as np
class Sudoku:
    def __init__(self):
        self.board=np.matrix([[0]*9]*9)
        self.finalBoard=np.matrix([[0]*9]*9)
        self.ranges=[[0,1,2],[3,4,5],[6,7,8]]
        self.completed=False
    def checkColumn(self,num,col):
        for r in range(0,9):
            if self.board[r,col]==num:
                return True
        return False
    def checkRow(self,num,row):
        for c in range(0,9):
            if self.board[row,c]==num:
                return True
        return False
    def boxCheck(self,num,row,col):
        rows=self.ranges[int(row/3)]
        cols=self.ranges[int(col/3)]
        for r in rows:
            for c in cols:
                if self.board[r,c]==num:
                    return True
        return False
    def possible(self,num,row,col):
        if not self.checkColumn(num,col) and not self.checkRow(num,row) and not self.boxCheck(num,row,col):
            return True
        else:
            return False
    def fillBox(self):
        if not self.completed:
            for r in range(9):
                for c in range(9):
                    if self.board[r,c]==0:
                        iter_list=[1,2,3,4,5,6,7,8,9] #making completely randomized
                        random.shuffle(iter_list)
                        for n in iter_list:
                            if self.possible(n,r,c):
                                self.board[r,c]=n
                                self.fillBox() #branch
                                self.board[r,c]=0
                    if self.board[r,c]==0:#if no value is placed then back track
                        return
            #print(self.board)
            self.finalBoard=self.board.copy()
            self.completed=True
    def finalBoardZeroFilling(self):
        noOfZeros=random.randint(40,50)
        while noOfZeros>=0:
            r=random.randint(0,8)
            c=random.randint(0,8)
            if self.finalBoard[r,c]!=0:
                self.finalBoard[r,c]=0
                noOfZeros-=1
    def generateBoard(self):
        self.fillBox()
        self.finalBoardZeroFilling()
        ##################### Reseting ##############
        self.completed=False
        self.board=self.finalBoard.copy()
    def solve(self):
        if not self.completed:
            for r in range(9):
                for c in range(9):
                    if self.board[r,c]==0:
                        for n in range(1,10):
                            if self.possible(n,r,c):
                                self.board[r,c]=n
                                self.fillBox() #branch
                                self.board[r,c]=0
                    if self.board[r,c]==0:#if no value is placed then back track
                        return
            #when finaly it get resolved, means out of the loop
            self.finalBoard=self.board.copy()
            self.completed=True
    def playBySelf(self):
        nonZeroList=[]
        noOfZeros=0
        for r in range(9):
            for c in range(9):
                if self.board[r,c]==0:
                    noOfZeros+=1
                else:
                    nonZeroList.append([r,c])
        while noOfZeros>=0:
            q=input("want to quit?y/n\n")
            if q=="y":
                #1st undoing all changes
                for r in range(9):
                    for c in range(9):
                        if [r,c] not in nonZeroList:
                            self.board[r,c]=0
                self.solve()
                print(self.finalBoard)
                return
            else:
                print(self.board)
                r=int(input("Enter row number"))
                c=int(input("Enter col number"))
                if self.board[r,c]!=0:
                    if [r,c] in nonZeroList:
                        print("again enter position...")
                    else:
                        print(f"making the position {r,c} zero ")
                        noOfZeros+=1
                else:
                    try:
                        n=int(input("Enter number between 1-9: "))
                    except:
                        print("give an integer number please")
                        continue
                    if n<0 or n>9:
                        print("Out of range input")
                    else:
                        if self.possible(n,r,c):
                            self.board[r,c]=n
                            noOfZeros+=1
                        else:
                            print("Not the correct number")
        print("solved......")
        print(self.board)

    def play(self):
        self.generateBoard()
        print("Your board is generated..........")
        print(self.board)
        key=input('''1.play your self \n2.let comp solve it\n''')
        if key=="2":
            self.solve()
            print("Output.......")
            print(self.finalBoard)
        elif key=="1":
            self.playBySelf()
        else:
            print("Press option correctly....-_-")

if __name__=="__main__":
    while True:
        print("Hi user play sudoku here....")
        key1=input('''1.New Board\n2.Quit\n''')
        if key1=="1":
            s=Sudoku()
            s.play()
            del s
        elif key1=="2":
            print("Thanks....-_-")
            break
        else:
            print("Press option correctly....-_-")
        




        


