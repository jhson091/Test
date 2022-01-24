num=int(input("숫자를 입력해주십시오: "))
guess=int(input("숫자를 추측해주십시오: "))
cnt=0
while num != guess:
    if num>guess:
        print(str(guess)+"업")
        guess = int(input("숫자를 다시 추측해주십시오: "))
        cnt+=1
    elif num<guess:
        print(str(guess)+"다운")
        guess=int(input("숫자를 다시 추측해주십시오: "))
        cnt += 1
    else:
        print("정답입니다")

print("시도 횟수는 "+str(cnt)+"번입니다")