class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = 0
        for i in range(31,-1,-1):
            if 2 ** i <= n:
                num += 2 ** (31 - i)
                n -= 2 ** i
        return num
        