import os
import pickle
def input_num(score):
    i=1
    print("[점수 입력]")
    while True:
       
        num=int(input(f'#{i}?'))
        if num<0:
            return False
        score.append(num)
        i+=1
def show(score):
    sum=0
    print()
    for i in score:
        sum+=i

    print("개인점수:",end="")
    for i in score:
        print(i,end="")
    print()
    print(f'평균:{sum/len(score):.1f}')
def save_data(score,filepath):
    with open(filepath,'wb') as file:
        pickle.dump(score,file)
def load_data(filepath):
    with open(filepath,'rb') as file:
        score=pickle.load(file)
        return score
filename="score.bin"
if os.path.exists(filename):
    print('[파일읽기]')
    print()
    score=load_data(filename)
else:
    score=[]
    while True:
        if input_num(score)==False:
            break
    save_data(score,filename)
show(score)
