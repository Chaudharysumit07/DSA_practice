# Question link: https://leetcode.com/problems/product-of-the-last-k-numbers/

# T.C. = O(N), S.C. = O(N)

class ProductOfNumbers:

    def __init__(self):
        
        self.prefixProduct=[1]
        self.size=0
        

    def add(self, num: int) -> None:
        if num==0:
            self.prefixProduct=[1]
            self.size=0
        else:
            self.prefixProduct.append(self.prefixProduct[self.size]*num)
            self.size+=1
    

    def getProduct(self, k: int) -> int:

        product=1
        if k > self.size:
            product= 0
        else:
            product= (self.prefixProduct[self.size] // self.prefixProduct[self.size - k])
        return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
