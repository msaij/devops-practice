class primeFactors():
    def __init__(self, x:int) -> None:
        self.x = x

    def largest(self, d:int = 2, arr:list=[]):
        while self.x > 1:
            while self.x % d == 0:
                arr.append(d)
                self.x //= d
            d+=1
        print(max(arr))

x = int(input("Give me a numeber: "))
primeFactors(x).largest()