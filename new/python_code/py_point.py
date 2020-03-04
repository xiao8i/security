# 验证python指向=的具体功能


a = 10
b = a
a = 20
print(b)


def cut(arr):
	arr[0], arr[1] = arr[1], arr[0] 
	print(arr)

	
test = [1, 2, 3, 4]
cut(test[1:3])
print(test)
cut(test)
print(test)