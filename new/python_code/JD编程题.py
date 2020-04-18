"""
输入版本
in1=[]
in1.append(input("m支股票 每天最多出n支'm n':"))
in1.append(input("m支股票每天亏损'a b c ……':"))
plan = input("方案数'plan':")
in1.append(plan)
for i in range(0,int(plan)):
	in1.append(input("%d方案需要卖出o支股票:" %i)) 
print(in1)
"""
in1 = """5 2
2 1 3 5 4
2
3
5""" 
in1 = in1.split("\n")
print(in1)
in2 = []
for i in in1:
	j = i.split(" ")
	print(j)
	j = [int(i) for i in j]
	in2.append(j)
in2[1].sort()
print(in2)
m = in2[0][1]
test = in2[1]
o = [0] * in2[2][0]
p = 0
for n in in2[3::]:
	i = 0
	p += 1
	d = 1
	t = n[0]
	while i < n[0]: 
		j =0
		while j < m and t > 0:
			o[p -1] += test[t-1] * d
			j += 1
			i += 1
			t -= 1
		d += 1
for i in o:
	print(i)
