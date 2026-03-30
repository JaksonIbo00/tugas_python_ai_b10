#List
B = ["a", "b", "c"]
print(B[1:]) #Mengakses elemen mulai dari indeks satu dan setelahnya dari list B
print(B[:1]) #Mengakses elemen sebelum indeks 1 dari list B

#Tuple
A=(0,1,2,3)
print(A[3]) #Mengakses elemen ke 3(indeks 3) dari tuple A
print(A[-2]) #Mengakses elemen terakhir dari tuple A

#Sets
X={'a', 'b', 'c', 'd'}
Y={'a', 'c', 'd', 'e', 'z'}
print(X.union(Y))

#Dictionary
student = {
    "name": "Jakson",
    "age": "21",
    "major": "computer science",
    "is_graduated": False,
    "height": 170.0
}
print(student)
print(student[name])