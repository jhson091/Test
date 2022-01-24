import random

user=int(input("하나를 선택하세요 : 가위(0), 바위(1), 보(2) : "))

com=random.randint(0,2)

if com == 0:
    print("컴퓨터는 가위를 냈습니다")
elif com == 1:
    print("컴퓨터는 바위를 냈습니다")
else:
    print("컴퓨터는 보를 냈습니다")


if user==com:
    print("비겼습니다")
elif user==2:
    if com==1:
        print("당신이 이겼습니다")
    else:
        print("컴퓨터가 이겼습니다")
elif user==1:
    if com==0:
        print("당신이 이겼습니다")
    else:
        print("컴퓨터가 이겼습니다")
elif user==0:
    if com==2:
        print("당신이 이겼습니다")
    else:
        print("컴퓨터가 이겼습니다")
