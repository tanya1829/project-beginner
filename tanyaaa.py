while(true):
    import random
    c=6
    rd=random.randrange(1,100)
    n=input("enter your name")
    while(c):
        num=int(input("guess the num"))
        if num>rd:
            print("too large")
        elif num<rd:
                  print("too small")
        elif num==rd:
                print("right")
                print(n, "you have win the game")
                break
        c-=1
    else:
       print("you loose the game!")
       print("do you want to play the game again?")
    w=input()
    if w=='no':
                break
        print("thankyou, have a good day!")
            
                
