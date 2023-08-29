class multiplesOf3and5():
    def __init__(self, n) -> None:
        self.r = range(1, n)
        self.o = [3,5]

    def getMultiples(self):
        self.a = []
        for _ in self.r:
            self.a.append(_) if _ % self.o[0] == 0 or _ % self.o[1] == 0 else quit
        return self.a

    def addMultiples(self):
        self.t = 0
        for e in self.getMultiples():
            self.t+=e
        print(str(self.getMultiples()) +" = "+ str(self.t ))


n = int(input("What is max value:"))
multiplesOf3and5(n).addMultiples()