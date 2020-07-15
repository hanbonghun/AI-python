#Enumerate: list 의 값을 추출할 때 번호를 붙여 추출
for i, v in enumerate(['tic','tac','tok']):
    print(i,v)

mylist = ["a","b","c","d"]
a = list(enumerate(mylist))
for lst in a:
    print(lst)

b={i:j for i,j in enumerate('Gacheon University is an academic institute located in South Korea'.split()) }
for i,j in b.items():
    print(i,j)

#zip : 두 개의 list 병렬적으로 추출
alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for a,b in zip(alist, blist):
    print(a,b)
