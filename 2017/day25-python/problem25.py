check=12586542
ones=0
state="A"
curr=0

arr = [0] * (check*2+1) # empty tape
curr = check #middle of the tape


while (check>0):
    if state=="A":
        if arr[curr]==0:
            arr[curr]=1
            ones=ones+1
            curr=curr+1
            state="B"
        elif arr[curr]==1:
            arr[curr]=0
            ones=ones-1
            curr=curr-1
            state="B"
    elif state=="B":
        if arr[curr]==0:
            arr[curr]=0
            curr=curr+1
            state="C"
        elif arr[curr]==1:
            arr[curr]=1
            curr=curr-1
            state="B"
    elif state=="C":
        if arr[curr]==0:
            arr[curr]=1
            ones=ones+1
            curr=curr+1
            state="D"
        elif arr[curr]==1:
            arr[curr]=0
            ones=ones-1
            curr=curr-1
            state="A"
    elif state=="D":
        if arr[curr]==0:
            arr[curr]=1
            ones=ones+1
            curr=curr-1
            state="E"
        elif arr[curr]==1:
            arr[curr]=1
            curr=curr-1
            state="F"
    elif state=="E":
        if arr[curr]==0:
            arr[curr]=1
            ones=ones+1
            curr=curr-1
            state="A"
        elif arr[curr]==1:
            arr[curr]=0
            ones=ones-1
            curr=curr-1
            state="D"
    elif state=="F":
        if arr[curr]==0:
            arr[curr]=1
            ones=ones+1
            curr=curr+1
            state="A"
        elif arr[curr]==1:
            arr[curr]=1
            curr=curr-1
            state="E"
    check=check-1



print("answer is:")
print(ones)
