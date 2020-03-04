import random

# 堆排序

def heap(obj):
    # 构造堆	
	for i in range(1, len(obj)):
		while i > 0:
			if obj[i] > obj[(i-1)//2]:
				obj[i], obj[(i-1)//2] = obj[(i-1)//2], obj[i]
				i = (i-1)//2
			else: 
				break
	print(obj)


def heap_order(obj):
	heap(obj)  #先构造堆
	m = len(obj)-1  #m是堆里最大的下标，从0起
	while m > 0:
		obj[0], obj[m] = obj[m], obj[0]  #交换头尾
		m = m-1
		i = 0  #标记当前位置
		while 2*i+1 <= m:
			j = 2*i+1  #标记左节点
			if j == m:  #先判断是否有右节点
				if obj[i] <	obj[j]:
					obj[i], obj[j] = obj[j], obj[i]
					i = j
					break
				else:
					break
			if obj[i] < obj[j] or obj[i] < obj[j + 1]:
				if obj[j] < obj[j+1]:
					j += 1
				obj[i], obj[j] = obj[j], obj[i]
				i = j
			else:
				break

if __name__ == '__main__':
	array = random.sample(range(0,100),100)
	heap_order(array)
	print(array)
