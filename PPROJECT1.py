import random
def evote():
    a=["bisat","mayank","akash","dakshdeep","devanshu"]
    b=["8168196670","8901009460","6395910040"]
    c=["BJP","CONGRESS","AAP","BSPA"]
    print("please enter your Name")
    name=str(input())
    name=name.lower()
    if name in a:
      print("Now,please enter your voter id")
      number=str(input())
      if number not in b:
        print("Yeah Match Not found")
        exit(0)
      if number in b:
        print("Match found")
        
    else:
         print("ENTER A VALID NAME")
         exit(0)
    print("Now ,please enter the OTP below")
    otp=""
    for i in range(6):
        otp+=str(random.randint(1,9))

    print(otp)
    print("Now, enter the OTP")
    u=str(input())
    if otp==u:
       print("YES,YOU MAY PROCEED NOW")
       print("please choose your candidate")
    for g in range(len(c)):
        print(c[g])
    candidate=str(input())
    candidate=candidate.upper()
    for g in range(len(c)):
        if candidate==c[g]:
            print("you choose ",candidate)
            print("THANK YOU")
        print(" Press Y to do vote Or N to exit")
        l=str(input())
        l=l.upper()
        if l=="Y":
            evote()
        else:
            exit(0)
            
a=["bisat","mayank","akash","dakshdeep","devanshu"]
b=["8168196670","8901009460","6395910040"]
c=["BJP","CONGRESS","AAP","BSPA"]
print("please enter your Name")
name=str(input())
name=name.lower()
if name in a:
    print("Now,please enter your voter id")
    number=str(input())
    if number not in b:
        print("Yeah Match Not found")
        exit(0)
    if number in b:
        print("Match found")
        
else:
    print("ENTER A VALID NAME")
    exit(0)
print("Now ,please enter the OTP below")
otp=""
for i in range(6):
    otp+=str(random.randint(1,9))

print(otp)
print("Now, enter the OTP")
u=str(input())
if otp==u:
    print("YES,YOU MAY PROCEED NOW")
    print("please choose your candidate")
    for g in range(len(c)):
        print(c[g])
    candidate=str(input())
    candidate=candidate.upper()
    for g in range(len(c)):
        if candidate==c[g]:
            print("you choose ",candidate)
            print("THANK YOU")
    print(" Press Y to do vote Or N to exit")
    l=str(input())
    l=l.upper()
    if l=="Y":
         evote()
    else:
         exit(0)
            
            
elif otp!=u:
    print("ACCESS DENIED")
    exit(0)
