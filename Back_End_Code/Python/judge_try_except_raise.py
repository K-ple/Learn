class NotPalindromeError(Exception):
    def __init__(self) -> None:
        super().__init__('회문이 아닙니다')
        
def palindrome(a):
    if a[::1] == a[::-1]:
        print(a)
    else:
        raise NotPalindromeError

try:
    word = input()
    palindrome(word)

except NotPalindromeError as e:
    print(e)
