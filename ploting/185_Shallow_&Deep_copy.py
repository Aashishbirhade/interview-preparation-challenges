import copy
a = [[1,2,3],[4,5,6]]
shallow = copy.copy(a)
shallow[0][0] = 14
print("original copy ",a)
print("shallow copy ",shallow)
# except it not work in 1-d array because in that it immutable so it not change in the orignal array

b = [[1,2,3],[4,5,6]]
deep = copy.deepcopy(b)
deep[0][2] = 54
print("original copy ",b)
print("deep copy ",deep)