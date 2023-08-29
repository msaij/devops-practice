class fibonacciEven():
    def __init__(self, x:int) -> None:
        self.x = x
    
    def evenFib(self, arr:list=[0,1]) -> None:
        while len(arr) <= self.x :
            arr.append(arr[-1] + arr[-2])
        print("Fibonacci: " + str(arr))
        
        evenFib = [num for num in arr if num % 2 == 0]
        print("Even numbers: " + str(evenFib))

x = int(input("What should be the length:"))
fibonacciEven(x).evenFib()