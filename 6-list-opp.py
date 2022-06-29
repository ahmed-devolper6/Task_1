
class Simple:
    def __init__(self) -> None:
        print('''
        Wceclome in our Game
        we have fave Game
        enter i cohice for play
        1:Even odd list
        2:type i squnse and tell u how many word the have
        3:type o number and start the game form zero entil u numb
        4:enter to numbers and tell u if equal or not
        5:input to numbers and tell the even num
        ''')
        self.user_choise()
    def user_choise(slef):
        while True:
            paly = input("Enter y for paly agin and X for exit: ")
            if paly == 'Y':
                User = int(input("Number of the game: "))
                if User == 1:
                    slef.frist()
                elif User == 2:
                    slef.secnd()
                elif User == 3:
                    slef.thred()
                elif User == 4:
                    slef.fort()
                elif User == 5:
                    slef.fif()
                else:
                    print("Type i number 0 to exit or range 1->5")
                    continue
            elif paly == 'X':
                print("Tanks....")
                break

    def frist(self):
        list1 = []
        list2 = []
        start = int(input("the numbert Start on: "))
        end = int(input("the number end on: "))
        for x in range(start,end):
            if x%2 == 0:
                list1.append(x)
            elif x%2 != 0:
                list2.append(x)
        print(f"Even list: {list1}")
        print(f"odd list: {list2}")
    def secnd(self):
        squnse = input("Type i squnse: ")
        count = squnse.split(" ")
        lentght = len(count)
        print(f"you have i {lentght} words")
    def thred(self):
        strat = 0
        end = int(input("type the end: "))
        for x in range(strat,end+1):
            print(x)
    def fort(self):
        mynum = int(input("Type i number: "))
        start = 0
        end = int(input("Type the end: "))
        for x in range(start,end):
             if x%mynum == 0 :
                 print(x)
    def fif(self):
        mynum1 = int(input("Type i nmuber: "))
        mynum2 = int(input("Type i nmuber: "))

        for x in range(1,101):
            if x%mynum1 == 0  :
                print(x)
            elif x%mynum2 == 0:
                 print(x)
g = Simple()