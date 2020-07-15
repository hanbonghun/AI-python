

#List comprehension, filter, 2-dimension
result = [i for i in range(10) if i%2 == 0]
print(result)

word_1 = "hello"
word_2 = "world"
#Two dimensional
result = [[i+j for i in word_1] for j in word_2]
#One dimensional
result = [i+j for i in word_1 for j in word_2]
print(result)

case_1 = ['A','B','C']
case_2 =["D",'E','A']
result = [i+j for i in case_1 for j in case_2 if not (i==j) ]
print(result)
