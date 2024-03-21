string = input("문자를 입력해주세요: ")
try:
    number = int(input("숫자를 입력해주세요: "))
except ValueError:
    print("숫자를 입력해주세요.")
    exit()

print(string)
print(number)