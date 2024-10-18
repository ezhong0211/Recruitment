class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        running_arr = []
        for num in range(1, n + 1):
            if num % 15 == 0:
                running_arr.append("FizzBuzz")
            elif num % 3 == 0:
                running_arr.append("Fizz")
            elif num % 5 == 0:
                running_arr.append("Buzz")
            else:
                running_arr.append(str(num))
        return running_arr
