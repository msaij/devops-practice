class palindrome():
    def __init__(self, v:int) -> None:
        self.v = v
    
    def digitsCount(self, n:int) -> int:
        digits:int = len(str(n))
        return digits
    
    def palindrome(self, p:int):
        pstr = str(p)
        return int(pstr[::-1])
    
    def palindromeOfProductOfNums(self) -> None:
        arr = set()
        start = 10 ** (self.v - 1)
        end = 10 ** self.v
        for x in range(start, end):
            for y in range(start, end):
                z = x * y
                arr.add(z) if self.palindrome(z) == z else None
        return arr
    
    def highestPalindrome(self):
        print(max(self.palindromeOfProductOfNums()))

v = int(input("Number of digits for product of numbers (sample: for xx*xx, give input as 2. for xxx*xxx, give input 3):"))
palindrome(v).highestPalindrome()