#Map function : sequence 자료형 각 element에 동일한 function 을 적용함
ex = [1,2,3,4,5]
f = lamda x : x**2
print(list(map(f,ex)))

f= lamda x,y : x+y
print(list(map(f,ex,ex)))

#lamda filter에서는 else 반드시 해줘야됨
list(map(lambda x: x**2 if x%2 ==0 else x,ex))

[value**2 for value in ex]

#reduce function : -map function과 달리 list에 똑같은 함수를 적용해서 통합
from functools import reduce
print(reduce(lambda x,y : x+y, [1,2,3,4,5]))


#lambda나 reduce는 코드의 직관성이 떨어져서 python 3 이후에는 사용 권장 x
#그러나 다양한 러신머닝 코드에서 사용중 
