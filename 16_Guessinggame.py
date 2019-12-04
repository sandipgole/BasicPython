secret_num=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("guess: "))
    guess_count+=1
    if guess==secret_num:
        print("you won")
        break
else:
    print("you loose")