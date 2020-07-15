u =[2,2]
v = [2,3]
z= [3,5]

result = [sum(t) for t in zip(u,v,z)]
print(result)
#scalar vector product
u=[1,2,3]
v=[4,5,6]
a=5
print([a * sum(t) for t in zip(u,v)])

#Matrix addiction
matrix_a = [[3,6],[4,6]]
matrix_b = [[5,8],[4,7]]
result = [[sum(row) for row in zip(*t)]for t in zip(matrix_a, matrix_b)]
print(result)

#scalar-Matrix product
matrix_a = [[3, 6], [4, 5]]
alpha = 4
result = [[alpha * element for element in t] for t in matrix_a]
print(result)

#Matrix Transpose
matrix_a=[[1,2,3],[4,5,6]]
result = [[element for element in t] for t in zip(*matrix_a)]
print(result)

#Matirx product
matrix_a=[[1,1,2],[2,1,1]]
matirx_b=[[1,1],[2,1],[1.3]]
result = [[sum(a * b for a, b in zip(row_a, column_b))
          for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)
