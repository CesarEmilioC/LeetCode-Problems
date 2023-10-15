class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = ""
        for i in range(31,-1,-1):
            if 2 ** i <= n:
                num += "1"
                n -= 2 ** i
            else:
                num += "0"
        num_reversed = num[::-1]
        new_num = 0
        for i in range(len(num_reversed)):
            new_num += int(num_reversed[i]) * 2 ** (len(num_reversed)-1-i)
        return new_num

        