command=""
started=False
while True:
    command=input("> ").lower()
    if command=="start":
         if started:
             print("already started")
         else:
             started=True
             print("car started")
    elif command=="stop":
        if not started:
            print("car already stopped")
        else:
            started=False
            print("car stopped")
    elif command=="help":
        print('''
start:...start car
stop :....begin car
quit:....quit
        ''')
    elif command=="quit":
        break
    else:
        print("i dont understand")


