class myReverseString:
	def my_reverse(self, chars: str) -> str: 
		if len(chars) == 1:
			return chars
		# use 2 pointer 
		left = 0
		right = len(chars)-1
		result = list(chars)
		while left < right:
			result[left], result[right] = result[right], result[left]
			left += 1
			right -= 1
		return "".join(result)

#time complexity O(n)
#space complexity O(n)
test = myReverseString()
test_case1 = "hello world"
test_case2 = 'Using a programming language of your choice, write a function to reverse a string. Please do not use features that include "reverse" function as built-in.'
assert test.my_reverse(test_case1) == test_case1[::-1]
assert test.my_reverse(test_case2) == test_case2[::-1]