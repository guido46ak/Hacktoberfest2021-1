def isPalindrome(s):
    return s == s[::-1]
s = input("Enter String:")
ans = isPalindrome(s)

if ans:
    print("Palindrome string che BRO..!!")
else:
    print("Palindrome string nathi BRO..!!")