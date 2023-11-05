import random

def analysis(ans,guess):
    A=0;
    B=0;
    print(ans)
    for i in range(4):
         print("A=",A,"B=",B)
         print(ans[i],guess[i])
         if guess[i]==ans[i]:
            A+=1
         else:
            if guess[i] in set(ans):
                B+=1;
    return A,B

nums=[0,1,2,3,4,5,6,7,8,9]
ans=random.sample(nums,4);

while 1>0:
    guess= input("Please enter a 4-digit number:")
    A=analysis(ans,guess)[0]
    B=analysis(ans,guess)[1]
    print(analysis(ans,guess))
    if A==4:
        print("Congratulation!!!")
        break;
    else:
        print(A,"A",B,"B")