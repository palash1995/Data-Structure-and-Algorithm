# Function to check Palindrome
def checkPalindrome(n):

	reverse = 0
	temp = n
	while (temp != 0):
		reverse = (reverse * 10) + (temp % 10)
		temp = temp // 10
	
	return (reverse == n) # if it is true then it will return 1;
				# else if false it will return 0;

# driver code
n = 7007
if (checkPalindrome(n) == 1):
	print("Yes")

else:
	print("No")