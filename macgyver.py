Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> test1=list
>>> test1
<class 'list'>
>>> len(test1)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    len(test1)
TypeError: object of type 'type' has no len()
>>> test[1]=21
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    test[1]=21
NameError: name 'test' is not defined
>>> test1[1]=21
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    test1[1]=21
TypeError: 'type' object does not support item assignment
>>> test1[1][1]=21
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    test1[1][1]=21
TypeError: 'type' object is not subscriptable
>>> test1=dict()
>>> i,j=0
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    i,j=0
TypeError: 'int' object is not iterable
>>> i,j=0,0
>>> i
0
>>> j
0
>>> while i<16:
	while j<16:
		test1[i,j]="ok"

		
Traceback (most recent call last):
  File "<pyshell#14>", line 3, in <module>
    test1[i,j]="ok"
KeyboardInterrupt
>>> while i<16:
	while j<16:
		test1[i,j]="ok"
		j+=1
	i+=1

	
>>> test1
{(0, 0): 'ok', (0, 1): 'ok', (0, 2): 'ok', (0, 3): 'ok', (0, 4): 'ok', (0, 5): 'ok', (0, 6): 'ok', (0, 7): 'ok', (0, 8): 'ok', (0, 9): 'ok', (0, 10): 'ok', (0, 11): 'ok', (0, 12): 'ok', (0, 13): 'ok', (0, 14): 'ok', (0, 15): 'ok'}
>>> i
16
>>> len(test1)
16
>>> test1
{(0, 0): 'ok', (0, 1): 'ok', (0, 2): 'ok', (0, 3): 'ok', (0, 4): 'ok', (0, 5): 'ok', (0, 6): 'ok', (0, 7): 'ok', (0, 8): 'ok', (0, 9): 'ok', (0, 10): 'ok', (0, 11): 'ok', (0, 12): 'ok', (0, 13): 'ok', (0, 14): 'ok', (0, 15): 'ok'}
>>> while i<16:
	test1[i]="ok"
	i+=1

	
>>> test1
{(0, 0): 'ok', (0, 1): 'ok', (0, 2): 'ok', (0, 3): 'ok', (0, 4): 'ok', (0, 5): 'ok', (0, 6): 'ok', (0, 7): 'ok', (0, 8): 'ok', (0, 9): 'ok', (0, 10): 'ok', (0, 11): 'ok', (0, 12): 'ok', (0, 13): 'ok', (0, 14): 'ok', (0, 15): 'ok'}
>>> test1=dict()
>>> test1
{}
>>> while i<16:
	test1[i]="ok"
	i+=1

	
>>> test1
{}
>>> i
16
>>> test2
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    test2
NameError: name 'test2' is not defined
>>> test1[2]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    test1[2]
KeyError: 2
>>> test1[3]="ok"
>>> test1[3]
'ok'
>>> test1[2,3]=2
>>> test1
{3: 'ok', (2, 3): 2}
>>> test1[i,j]="ok"
>>> test1
{3: 'ok', (2, 3): 2, (16, 16): 'ok'}
>>> while i<16:
	while j<16:
		test1[i,j]="ok"

		j+=1
	i+=1

	
>>> while i<16:
	while j<16:
		test1[i,j]="ok"

		j+=1
	print(test1[i,j])	
	i+=1

	
>>> print(test1[i,j])
ok
>>> i,j=0,0
>>> while i<16:
	while j<16:
		test1[i,j]="ok"

		j+=1
	print(i,j)
	i+=1

	
0 16
1 16
2 16
3 16
4 16
5 16
6 16
7 16
8 16
9 16
10 16
11 16
12 16
13 16
14 16
15 16
>>> test1
{3: 'ok', (2, 3): 2, (16, 16): 'ok', (0, 0): 'ok', (0, 1): 'ok', (0, 2): 'ok', (0, 3): 'ok', (0, 4): 'ok', (0, 5): 'ok', (0, 6): 'ok', (0, 7): 'ok', (0, 8): 'ok', (0, 9): 'ok', (0, 10): 'ok', (0, 11): 'ok', (0, 12): 'ok', (0, 13): 'ok', (0, 14): 'ok', (0, 15): 'ok'}
>>> test1=dict()
>>> while i<16:
	while j<16:
		test1[i,j]="ok"

		j+=1
	print(i,j)
	i+=1

	
>>> i,j=0,0
>>> while i<16:
	while j<16:
		test1[i,j]="ok"

		j+=1
	print(i,j)
	i+=1

	
0 16
1 16
2 16
3 16
4 16
5 16
6 16
7 16
8 16
9 16
10 16
11 16
12 16
13 16
14 16
15 16
>>> test1
{(0, 0): 'ok', (0, 1): 'ok', (0, 2): 'ok', (0, 3): 'ok', (0, 4): 'ok', (0, 5): 'ok', (0, 6): 'ok', (0, 7): 'ok', (0, 8): 'ok', (0, 9): 'ok', (0, 10): 'ok', (0, 11): 'ok', (0, 12): 'ok', (0, 13): 'ok', (0, 14): 'ok', (0, 15): 'ok'}
>>> j
16
>>> i,j=0,0
>>> while i<16:
	while j<16:
		test1[i,j]="ok"

		j+=1
	print(j)
	i+=1

	
16
16
16
16
16
16
16
16
16
16
16
16
16
16
16
16
>>> i,j=0,0
>>> j
0
>>> i
0
>>> j+=1
>>> j
1
>>> i,j=0,0
>>> while i<16:
	while j<16:
		test1[i,j]="ok"
		print(j)
		j+=1
	
	i+=1

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
>>> i,j=0,0
>>> while i<16:
	while j<16:
		test1[i,j]="ok"
		print(j)
		j+=1
	print(i)
	i+=1

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
>>> i,j=0,0
>>> while i<16:
	while j<16:
		test1[i,j]="ok"
		print(i,j)
		j+=1
	
	i+=1

	
0 0
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
0 9
0 10
0 11
0 12
0 13
0 14
0 15
>>> j=0,0
>>> j
(0, 0)
>>> i,j=0,0
>>> j
0
>>> i
0
>>> while i<16:
	while j<16:
		test1[i,j]="ok"
		print(i,j)
		j+=1

i+=1
SyntaxError: invalid syntax
>>> while i<16:
	while j<16:
		test1[i,j]="ok"
		print(i,j)
		j+=1

	i+=1

	
0 0
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
0 9
0 10
0 11
0 12
0 13
0 14
0 15
>>> i,j=0,0
>>> test1=dict()
>>> for i,j in range(0,16,1):
	test1[i,j]="ok"

	
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    for i,j in range(0,16,1):
TypeError: 'int' object is not iterable
>>> i
0
>>> for i in range(0,16):
	for j in range (0,16):
		test1[i,j]="ok"
		j+=1
	i+=1

	
>>> test1
{(0, 0): 'ok', (0, 1): 'ok', (0, 2): 'ok', (0, 3): 'ok', (0, 4): 'ok', (0, 5): 'ok', (0, 6): 'ok', (0, 7): 'ok', (0, 8): 'ok', (0, 9): 'ok', (0, 10): 'ok', (0, 11): 'ok', (0, 12): 'ok', (0, 13): 'ok', (0, 14): 'ok', (0, 15): 'ok', (1, 0): 'ok', (1, 1): 'ok', (1, 2): 'ok', (1, 3): 'ok', (1, 4): 'ok', (1, 5): 'ok', (1, 6): 'ok', (1, 7): 'ok', (1, 8): 'ok', (1, 9): 'ok', (1, 10): 'ok', (1, 11): 'ok', (1, 12): 'ok', (1, 13): 'ok', (1, 14): 'ok', (1, 15): 'ok', (2, 0): 'ok', (2, 1): 'ok', (2, 2): 'ok', (2, 3): 'ok', (2, 4): 'ok', (2, 5): 'ok', (2, 6): 'ok', (2, 7): 'ok', (2, 8): 'ok', (2, 9): 'ok', (2, 10): 'ok', (2, 11): 'ok', (2, 12): 'ok', (2, 13): 'ok', (2, 14): 'ok', (2, 15): 'ok', (3, 0): 'ok', (3, 1): 'ok', (3, 2): 'ok', (3, 3): 'ok', (3, 4): 'ok', (3, 5): 'ok', (3, 6): 'ok', (3, 7): 'ok', (3, 8): 'ok', (3, 9): 'ok', (3, 10): 'ok', (3, 11): 'ok', (3, 12): 'ok', (3, 13): 'ok', (3, 14): 'ok', (3, 15): 'ok', (4, 0): 'ok', (4, 1): 'ok', (4, 2): 'ok', (4, 3): 'ok', (4, 4): 'ok', (4, 5): 'ok', (4, 6): 'ok', (4, 7): 'ok', (4, 8): 'ok', (4, 9): 'ok', (4, 10): 'ok', (4, 11): 'ok', (4, 12): 'ok', (4, 13): 'ok', (4, 14): 'ok', (4, 15): 'ok', (5, 0): 'ok', (5, 1): 'ok', (5, 2): 'ok', (5, 3): 'ok', (5, 4): 'ok', (5, 5): 'ok', (5, 6): 'ok', (5, 7): 'ok', (5, 8): 'ok', (5, 9): 'ok', (5, 10): 'ok', (5, 11): 'ok', (5, 12): 'ok', (5, 13): 'ok', (5, 14): 'ok', (5, 15): 'ok', (6, 0): 'ok', (6, 1): 'ok', (6, 2): 'ok', (6, 3): 'ok', (6, 4): 'ok', (6, 5): 'ok', (6, 6): 'ok', (6, 7): 'ok', (6, 8): 'ok', (6, 9): 'ok', (6, 10): 'ok', (6, 11): 'ok', (6, 12): 'ok', (6, 13): 'ok', (6, 14): 'ok', (6, 15): 'ok', (7, 0): 'ok', (7, 1): 'ok', (7, 2): 'ok', (7, 3): 'ok', (7, 4): 'ok', (7, 5): 'ok', (7, 6): 'ok', (7, 7): 'ok', (7, 8): 'ok', (7, 9): 'ok', (7, 10): 'ok', (7, 11): 'ok', (7, 12): 'ok', (7, 13): 'ok', (7, 14): 'ok', (7, 15): 'ok', (8, 0): 'ok', (8, 1): 'ok', (8, 2): 'ok', (8, 3): 'ok', (8, 4): 'ok', (8, 5): 'ok', (8, 6): 'ok', (8, 7): 'ok', (8, 8): 'ok', (8, 9): 'ok', (8, 10): 'ok', (8, 11): 'ok', (8, 12): 'ok', (8, 13): 'ok', (8, 14): 'ok', (8, 15): 'ok', (9, 0): 'ok', (9, 1): 'ok', (9, 2): 'ok', (9, 3): 'ok', (9, 4): 'ok', (9, 5): 'ok', (9, 6): 'ok', (9, 7): 'ok', (9, 8): 'ok', (9, 9): 'ok', (9, 10): 'ok', (9, 11): 'ok', (9, 12): 'ok', (9, 13): 'ok', (9, 14): 'ok', (9, 15): 'ok', (10, 0): 'ok', (10, 1): 'ok', (10, 2): 'ok', (10, 3): 'ok', (10, 4): 'ok', (10, 5): 'ok', (10, 6): 'ok', (10, 7): 'ok', (10, 8): 'ok', (10, 9): 'ok', (10, 10): 'ok', (10, 11): 'ok', (10, 12): 'ok', (10, 13): 'ok', (10, 14): 'ok', (10, 15): 'ok', (11, 0): 'ok', (11, 1): 'ok', (11, 2): 'ok', (11, 3): 'ok', (11, 4): 'ok', (11, 5): 'ok', (11, 6): 'ok', (11, 7): 'ok', (11, 8): 'ok', (11, 9): 'ok', (11, 10): 'ok', (11, 11): 'ok', (11, 12): 'ok', (11, 13): 'ok', (11, 14): 'ok', (11, 15): 'ok', (12, 0): 'ok', (12, 1): 'ok', (12, 2): 'ok', (12, 3): 'ok', (12, 4): 'ok', (12, 5): 'ok', (12, 6): 'ok', (12, 7): 'ok', (12, 8): 'ok', (12, 9): 'ok', (12, 10): 'ok', (12, 11): 'ok', (12, 12): 'ok', (12, 13): 'ok', (12, 14): 'ok', (12, 15): 'ok', (13, 0): 'ok', (13, 1): 'ok', (13, 2): 'ok', (13, 3): 'ok', (13, 4): 'ok', (13, 5): 'ok', (13, 6): 'ok', (13, 7): 'ok', (13, 8): 'ok', (13, 9): 'ok', (13, 10): 'ok', (13, 11): 'ok', (13, 12): 'ok', (13, 13): 'ok', (13, 14): 'ok', (13, 15): 'ok', (14, 0): 'ok', (14, 1): 'ok', (14, 2): 'ok', (14, 3): 'ok', (14, 4): 'ok', (14, 5): 'ok', (14, 6): 'ok', (14, 7): 'ok', (14, 8): 'ok', (14, 9): 'ok', (14, 10): 'ok', (14, 11): 'ok', (14, 12): 'ok', (14, 13): 'ok', (14, 14): 'ok', (14, 15): 'ok', (15, 0): 'ok', (15, 1): 'ok', (15, 2): 'ok', (15, 3): 'ok', (15, 4): 'ok', (15, 5): 'ok', (15, 6): 'ok', (15, 7): 'ok', (15, 8): 'ok', (15, 9): 'ok', (15, 10): 'ok', (15, 11): 'ok', (15, 12): 'ok', (15, 13): 'ok', (15, 14): 'ok', (15, 15): 'ok'}
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> test1.values()
dict_values(['ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok'])
>>> len(test1)
256
>>> test1.items
<built-in method items of dict object at 0x03B10960>
>>> test1.keys()
dict_keys([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (13, 9), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (13, 15), (14, 0), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15), (15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15)])
>>> test1.items()
dict_items([((0, 0), 'ok'), ((0, 1), 'ok'), ((0, 2), 'ok'), ((0, 3), 'ok'), ((0, 4), 'ok'), ((0, 5), 'ok'), ((0, 6), 'ok'), ((0, 7), 'ok'), ((0, 8), 'ok'), ((0, 9), 'ok'), ((0, 10), 'ok'), ((0, 11), 'ok'), ((0, 12), 'ok'), ((0, 13), 'ok'), ((0, 14), 'ok'), ((0, 15), 'ok'), ((1, 0), 'ok'), ((1, 1), 'ok'), ((1, 2), 'ok'), ((1, 3), 'ok'), ((1, 4), 'ok'), ((1, 5), 'ok'), ((1, 6), 'ok'), ((1, 7), 'ok'), ((1, 8), 'ok'), ((1, 9), 'ok'), ((1, 10), 'ok'), ((1, 11), 'ok'), ((1, 12), 'ok'), ((1, 13), 'ok'), ((1, 14), 'ok'), ((1, 15), 'ok'), ((2, 0), 'ok'), ((2, 1), 'ok'), ((2, 2), 'ok'), ((2, 3), 'ok'), ((2, 4), 'ok'), ((2, 5), 'ok'), ((2, 6), 'ok'), ((2, 7), 'ok'), ((2, 8), 'ok'), ((2, 9), 'ok'), ((2, 10), 'ok'), ((2, 11), 'ok'), ((2, 12), 'ok'), ((2, 13), 'ok'), ((2, 14), 'ok'), ((2, 15), 'ok'), ((3, 0), 'ok'), ((3, 1), 'ok'), ((3, 2), 'ok'), ((3, 3), 'ok'), ((3, 4), 'ok'), ((3, 5), 'ok'), ((3, 6), 'ok'), ((3, 7), 'ok'), ((3, 8), 'ok'), ((3, 9), 'ok'), ((3, 10), 'ok'), ((3, 11), 'ok'), ((3, 12), 'ok'), ((3, 13), 'ok'), ((3, 14), 'ok'), ((3, 15), 'ok'), ((4, 0), 'ok'), ((4, 1), 'ok'), ((4, 2), 'ok'), ((4, 3), 'ok'), ((4, 4), 'ok'), ((4, 5), 'ok'), ((4, 6), 'ok'), ((4, 7), 'ok'), ((4, 8), 'ok'), ((4, 9), 'ok'), ((4, 10), 'ok'), ((4, 11), 'ok'), ((4, 12), 'ok'), ((4, 13), 'ok'), ((4, 14), 'ok'), ((4, 15), 'ok'), ((5, 0), 'ok'), ((5, 1), 'ok'), ((5, 2), 'ok'), ((5, 3), 'ok'), ((5, 4), 'ok'), ((5, 5), 'ok'), ((5, 6), 'ok'), ((5, 7), 'ok'), ((5, 8), 'ok'), ((5, 9), 'ok'), ((5, 10), 'ok'), ((5, 11), 'ok'), ((5, 12), 'ok'), ((5, 13), 'ok'), ((5, 14), 'ok'), ((5, 15), 'ok'), ((6, 0), 'ok'), ((6, 1), 'ok'), ((6, 2), 'ok'), ((6, 3), 'ok'), ((6, 4), 'ok'), ((6, 5), 'ok'), ((6, 6), 'ok'), ((6, 7), 'ok'), ((6, 8), 'ok'), ((6, 9), 'ok'), ((6, 10), 'ok'), ((6, 11), 'ok'), ((6, 12), 'ok'), ((6, 13), 'ok'), ((6, 14), 'ok'), ((6, 15), 'ok'), ((7, 0), 'ok'), ((7, 1), 'ok'), ((7, 2), 'ok'), ((7, 3), 'ok'), ((7, 4), 'ok'), ((7, 5), 'ok'), ((7, 6), 'ok'), ((7, 7), 'ok'), ((7, 8), 'ok'), ((7, 9), 'ok'), ((7, 10), 'ok'), ((7, 11), 'ok'), ((7, 12), 'ok'), ((7, 13), 'ok'), ((7, 14), 'ok'), ((7, 15), 'ok'), ((8, 0), 'ok'), ((8, 1), 'ok'), ((8, 2), 'ok'), ((8, 3), 'ok'), ((8, 4), 'ok'), ((8, 5), 'ok'), ((8, 6), 'ok'), ((8, 7), 'ok'), ((8, 8), 'ok'), ((8, 9), 'ok'), ((8, 10), 'ok'), ((8, 11), 'ok'), ((8, 12), 'ok'), ((8, 13), 'ok'), ((8, 14), 'ok'), ((8, 15), 'ok'), ((9, 0), 'ok'), ((9, 1), 'ok'), ((9, 2), 'ok'), ((9, 3), 'ok'), ((9, 4), 'ok'), ((9, 5), 'ok'), ((9, 6), 'ok'), ((9, 7), 'ok'), ((9, 8), 'ok'), ((9, 9), 'ok'), ((9, 10), 'ok'), ((9, 11), 'ok'), ((9, 12), 'ok'), ((9, 13), 'ok'), ((9, 14), 'ok'), ((9, 15), 'ok'), ((10, 0), 'ok'), ((10, 1), 'ok'), ((10, 2), 'ok'), ((10, 3), 'ok'), ((10, 4), 'ok'), ((10, 5), 'ok'), ((10, 6), 'ok'), ((10, 7), 'ok'), ((10, 8), 'ok'), ((10, 9), 'ok'), ((10, 10), 'ok'), ((10, 11), 'ok'), ((10, 12), 'ok'), ((10, 13), 'ok'), ((10, 14), 'ok'), ((10, 15), 'ok'), ((11, 0), 'ok'), ((11, 1), 'ok'), ((11, 2), 'ok'), ((11, 3), 'ok'), ((11, 4), 'ok'), ((11, 5), 'ok'), ((11, 6), 'ok'), ((11, 7), 'ok'), ((11, 8), 'ok'), ((11, 9), 'ok'), ((11, 10), 'ok'), ((11, 11), 'ok'), ((11, 12), 'ok'), ((11, 13), 'ok'), ((11, 14), 'ok'), ((11, 15), 'ok'), ((12, 0), 'ok'), ((12, 1), 'ok'), ((12, 2), 'ok'), ((12, 3), 'ok'), ((12, 4), 'ok'), ((12, 5), 'ok'), ((12, 6), 'ok'), ((12, 7), 'ok'), ((12, 8), 'ok'), ((12, 9), 'ok'), ((12, 10), 'ok'), ((12, 11), 'ok'), ((12, 12), 'ok'), ((12, 13), 'ok'), ((12, 14), 'ok'), ((12, 15), 'ok'), ((13, 0), 'ok'), ((13, 1), 'ok'), ((13, 2), 'ok'), ((13, 3), 'ok'), ((13, 4), 'ok'), ((13, 5), 'ok'), ((13, 6), 'ok'), ((13, 7), 'ok'), ((13, 8), 'ok'), ((13, 9), 'ok'), ((13, 10), 'ok'), ((13, 11), 'ok'), ((13, 12), 'ok'), ((13, 13), 'ok'), ((13, 14), 'ok'), ((13, 15), 'ok'), ((14, 0), 'ok'), ((14, 1), 'ok'), ((14, 2), 'ok'), ((14, 3), 'ok'), ((14, 4), 'ok'), ((14, 5), 'ok'), ((14, 6), 'ok'), ((14, 7), 'ok'), ((14, 8), 'ok'), ((14, 9), 'ok'), ((14, 10), 'ok'), ((14, 11), 'ok'), ((14, 12), 'ok'), ((14, 13), 'ok'), ((14, 14), 'ok'), ((14, 15), 'ok'), ((15, 0), 'ok'), ((15, 1), 'ok'), ((15, 2), 'ok'), ((15, 3), 'ok'), ((15, 4), 'ok'), ((15, 5), 'ok'), ((15, 6), 'ok'), ((15, 7), 'ok'), ((15, 8), 'ok'), ((15, 9), 'ok'), ((15, 10), 'ok'), ((15, 11), 'ok'), ((15, 12), 'ok'), ((15, 13), 'ok'), ((15, 14), 'ok'), ((15, 15), 'ok')])
>>> val=test1.values()
>>> for v in val:
	print(v)

	
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
ok
>>> val
dict_values(['ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok'])
>>> dir(random)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    dir(random)
NameError: name 'random' is not defined
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> random.__doc__()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    random.__doc__()
TypeError: 'str' object is not callable
>>> random.__doc__
'Random variable generators.\n\n    integers\n    --------\n           uniform within range\n\n    sequences\n    ---------\n           pick random element\n           pick random sample\n           pick weighted random sample\n           generate random permutation\n\n    distributions on the real line:\n    ------------------------------\n           uniform\n           triangular\n           normal (Gaussian)\n           lognormal\n           negative exponential\n           gamma\n           beta\n           pareto\n           Weibull\n\n    distributions on the circle (angles 0 to 2pi)\n    ---------------------------------------------\n           circular uniform\n           von Mises\n\nGeneral notes on the underlying Mersenne Twister core generator:\n\n* The period is 2**19937-1.\n* It is one of the most extensively tested generators in existence.\n* The random() method is implemented in C, executes in a single Python step,\n  and is, therefore, threadsafe.\n\n'
>>> liste2=[11,2,3,4,5]
>>> import random
>>> random(liste2)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    random(liste2)
TypeError: 'module' object is not callable
>>> for l in liste2:
	print(random(liste2))

	
Traceback (most recent call last):
  File "<pyshell#119>", line 2, in <module>
    print(random(liste2))
TypeError: 'module' object is not callable
>>> random
<module 'random' from 'C:\\Users\\Max\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\random.py'>
>>> str(random)
"<module 'random' from 'C:\\\\Users\\\\Max\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python36-32\\\\lib\\\\random.py'>"
>>> dir(random.random())
['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
>>> dir(random.random.__dir__)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
>>> dir(random.random.__doc__)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> random.choice(liste2)
11
>>> liste2=[11,pass]
SyntaxError: invalid syntax
>>> liste2=[11,None]
>>> liste2
[11, None]
>>> i,j=0,0
>>> random.choice(liste2)
11
>>> random.choice(liste2)
11
>>> liste2=[3,11,pass]
SyntaxError: invalid syntax
>>> liste2=[3,11,None]
>>> random.choice(liste2)
3
>>> random.choices(liste2)
[3]
>>> random.shuffle(liste2)
>>> r=random.shuffle(liste2)
>>> r
>>> choice(liste2)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    choice(liste2)
NameError: name 'choice' is not defined
>>> random.choice(liste2)
>>> liste2
[None, 11, 3]
>>> random.choice(liste2)
>>> random.choice(liste2)
11
>>> random.choice(liste2)
11
>>> random.choice(liste2)
11
>>> random.choice(liste2)
11
>>> random.choice(liste2)
11
>>> random.choice(liste2)
11
>>> random.choice(liste2)
3
>>> i
0
>>> test1=dict()
>>> wall=["m",None]
>>> for i in range(0,16):
	for j in range (0,16):
		test1[i,j]=random.choice(wall)
		j+=1
	i+=1

	
>>> test1
{(0, 0): None, (0, 1): None, (0, 2): 'm', (0, 3): 'm', (0, 4): None, (0, 5): 'm', (0, 6): 'm', (0, 7): None, (0, 8): None, (0, 9): 'm', (0, 10): None, (0, 11): 'm', (0, 12): 'm', (0, 13): 'm', (0, 14): 'm', (0, 15): None, (1, 0): 'm', (1, 1): 'm', (1, 2): 'm', (1, 3): 'm', (1, 4): 'm', (1, 5): 'm', (1, 6): 'm', (1, 7): None, (1, 8): None, (1, 9): None, (1, 10): None, (1, 11): 'm', (1, 12): None, (1, 13): 'm', (1, 14): None, (1, 15): 'm', (2, 0): 'm', (2, 1): None, (2, 2): 'm', (2, 3): 'm', (2, 4): 'm', (2, 5): None, (2, 6): 'm', (2, 7): None, (2, 8): None, (2, 9): None, (2, 10): None, (2, 11): None, (2, 12): 'm', (2, 13): 'm', (2, 14): None, (2, 15): 'm', (3, 0): None, (3, 1): 'm', (3, 2): 'm', (3, 3): 'm', (3, 4): 'm', (3, 5): 'm', (3, 6): 'm', (3, 7): 'm', (3, 8): None, (3, 9): None, (3, 10): None, (3, 11): None, (3, 12): None, (3, 13): None, (3, 14): None, (3, 15): None, (4, 0): None, (4, 1): 'm', (4, 2): 'm', (4, 3): None, (4, 4): 'm', (4, 5): 'm', (4, 6): None, (4, 7): 'm', (4, 8): None, (4, 9): 'm', (4, 10): None, (4, 11): None, (4, 12): 'm', (4, 13): 'm', (4, 14): 'm', (4, 15): 'm', (5, 0): None, (5, 1): None, (5, 2): None, (5, 3): 'm', (5, 4): None, (5, 5): None, (5, 6): None, (5, 7): None, (5, 8): None, (5, 9): 'm', (5, 10): None, (5, 11): None, (5, 12): None, (5, 13): 'm', (5, 14): 'm', (5, 15): None, (6, 0): 'm', (6, 1): 'm', (6, 2): 'm', (6, 3): 'm', (6, 4): None, (6, 5): 'm', (6, 6): None, (6, 7): 'm', (6, 8): None, (6, 9): 'm', (6, 10): 'm', (6, 11): 'm', (6, 12): None, (6, 13): 'm', (6, 14): None, (6, 15): None, (7, 0): None, (7, 1): 'm', (7, 2): None, (7, 3): None, (7, 4): 'm', (7, 5): 'm', (7, 6): 'm', (7, 7): 'm', (7, 8): None, (7, 9): None, (7, 10): 'm', (7, 11): 'm', (7, 12): None, (7, 13): 'm', (7, 14): 'm', (7, 15): None, (8, 0): 'm', (8, 1): 'm', (8, 2): None, (8, 3): None, (8, 4): 'm', (8, 5): 'm', (8, 6): None, (8, 7): 'm', (8, 8): None, (8, 9): None, (8, 10): None, (8, 11): None, (8, 12): None, (8, 13): 'm', (8, 14): None, (8, 15): 'm', (9, 0): None, (9, 1): 'm', (9, 2): 'm', (9, 3): 'm', (9, 4): 'm', (9, 5): 'm', (9, 6): None, (9, 7): 'm', (9, 8): 'm', (9, 9): None, (9, 10): 'm', (9, 11): 'm', (9, 12): None, (9, 13): None, (9, 14): 'm', (9, 15): None, (10, 0): 'm', (10, 1): 'm', (10, 2): None, (10, 3): 'm', (10, 4): 'm', (10, 5): 'm', (10, 6): 'm', (10, 7): None, (10, 8): 'm', (10, 9): None, (10, 10): 'm', (10, 11): 'm', (10, 12): None, (10, 13): 'm', (10, 14): None, (10, 15): 'm', (11, 0): 'm', (11, 1): None, (11, 2): None, (11, 3): 'm', (11, 4): 'm', (11, 5): None, (11, 6): None, (11, 7): None, (11, 8): 'm', (11, 9): None, (11, 10): 'm', (11, 11): 'm', (11, 12): None, (11, 13): None, (11, 14): None, (11, 15): 'm', (12, 0): None, (12, 1): None, (12, 2): None, (12, 3): 'm', (12, 4): 'm', (12, 5): None, (12, 6): None, (12, 7): None, (12, 8): None, (12, 9): None, (12, 10): None, (12, 11): None, (12, 12): None, (12, 13): 'm', (12, 14): 'm', (12, 15): 'm', (13, 0): 'm', (13, 1): None, (13, 2): 'm', (13, 3): 'm', (13, 4): 'm', (13, 5): 'm', (13, 6): None, (13, 7): 'm', (13, 8): None, (13, 9): 'm', (13, 10): None, (13, 11): 'm', (13, 12): 'm', (13, 13): 'm', (13, 14): None, (13, 15): None, (14, 0): None, (14, 1): None, (14, 2): None, (14, 3): 'm', (14, 4): None, (14, 5): 'm', (14, 6): 'm', (14, 7): None, (14, 8): None, (14, 9): None, (14, 10): 'm', (14, 11): None, (14, 12): None, (14, 13): 'm', (14, 14): None, (14, 15): 'm', (15, 0): 'm', (15, 1): None, (15, 2): None, (15, 3): None, (15, 4): None, (15, 5): 'm', (15, 6): None, (15, 7): None, (15, 8): None, (15, 9): None, (15, 10): 'm', (15, 11): None, (15, 12): 'm', (15, 13): 'm', (15, 14): None, (15, 15): 'm'}
>>> i,j=0,0
>>> test1=dict()
>>> for i in range(0,16):
	for j in range (0,16):
		if (i==0 and j==0) or (i==15 and j==15) :
			test1[i,j]=None
		else:
			test1[i,j]=random.choice(wall)
		j+=1
	i+=1

	
>>> test1
{(0, 0): None, (0, 1): 'm', (0, 2): None, (0, 3): None, (0, 4): None, (0, 5): 'm', (0, 6): 'm', (0, 7): 'm', (0, 8): 'm', (0, 9): None, (0, 10): 'm', (0, 11): 'm', (0, 12): 'm', (0, 13): None, (0, 14): None, (0, 15): 'm', (1, 0): None, (1, 1): None, (1, 2): 'm', (1, 3): 'm', (1, 4): 'm', (1, 5): 'm', (1, 6): 'm', (1, 7): None, (1, 8): None, (1, 9): 'm', (1, 10): None, (1, 11): None, (1, 12): 'm', (1, 13): 'm', (1, 14): None, (1, 15): None, (2, 0): None, (2, 1): None, (2, 2): 'm', (2, 3): 'm', (2, 4): 'm', (2, 5): None, (2, 6): None, (2, 7): None, (2, 8): None, (2, 9): None, (2, 10): None, (2, 11): None, (2, 12): None, (2, 13): None, (2, 14): None, (2, 15): None, (3, 0): 'm', (3, 1): None, (3, 2): None, (3, 3): None, (3, 4): None, (3, 5): 'm', (3, 6): None, (3, 7): None, (3, 8): 'm', (3, 9): None, (3, 10): None, (3, 11): 'm', (3, 12): None, (3, 13): 'm', (3, 14): 'm', (3, 15): 'm', (4, 0): 'm', (4, 1): None, (4, 2): None, (4, 3): 'm', (4, 4): 'm', (4, 5): 'm', (4, 6): 'm', (4, 7): None, (4, 8): 'm', (4, 9): 'm', (4, 10): None, (4, 11): 'm', (4, 12): None, (4, 13): None, (4, 14): 'm', (4, 15): None, (5, 0): 'm', (5, 1): 'm', (5, 2): 'm', (5, 3): None, (5, 4): 'm', (5, 5): 'm', (5, 6): None, (5, 7): None, (5, 8): 'm', (5, 9): None, (5, 10): None, (5, 11): None, (5, 12): 'm', (5, 13): None, (5, 14): 'm', (5, 15): 'm', (6, 0): 'm', (6, 1): None, (6, 2): 'm', (6, 3): 'm', (6, 4): None, (6, 5): None, (6, 6): None, (6, 7): 'm', (6, 8): None, (6, 9): None, (6, 10): 'm', (6, 11): None, (6, 12): 'm', (6, 13): 'm', (6, 14): 'm', (6, 15): None, (7, 0): None, (7, 1): None, (7, 2): 'm', (7, 3): None, (7, 4): None, (7, 5): 'm', (7, 6): 'm', (7, 7): None, (7, 8): None, (7, 9): None, (7, 10): 'm', (7, 11): None, (7, 12): None, (7, 13): 'm', (7, 14): 'm', (7, 15): 'm', (8, 0): 'm', (8, 1): 'm', (8, 2): None, (8, 3): 'm', (8, 4): None, (8, 5): 'm', (8, 6): 'm', (8, 7): 'm', (8, 8): 'm', (8, 9): 'm', (8, 10): None, (8, 11): 'm', (8, 12): 'm', (8, 13): None, (8, 14): 'm', (8, 15): None, (9, 0): None, (9, 1): 'm', (9, 2): 'm', (9, 3): None, (9, 4): None, (9, 5): None, (9, 6): 'm', (9, 7): None, (9, 8): 'm', (9, 9): None, (9, 10): 'm', (9, 11): None, (9, 12): 'm', (9, 13): None, (9, 14): 'm', (9, 15): 'm', (10, 0): None, (10, 1): None, (10, 2): None, (10, 3): None, (10, 4): None, (10, 5): None, (10, 6): 'm', (10, 7): None, (10, 8): 'm', (10, 9): None, (10, 10): 'm', (10, 11): 'm', (10, 12): None, (10, 13): 'm', (10, 14): 'm', (10, 15): None, (11, 0): None, (11, 1): 'm', (11, 2): None, (11, 3): None, (11, 4): None, (11, 5): 'm', (11, 6): 'm', (11, 7): None, (11, 8): 'm', (11, 9): None, (11, 10): None, (11, 11): None, (11, 12): 'm', (11, 13): None, (11, 14): 'm', (11, 15): 'm', (12, 0): None, (12, 1): None, (12, 2): None, (12, 3): None, (12, 4): 'm', (12, 5): 'm', (12, 6): None, (12, 7): 'm', (12, 8): None, (12, 9): None, (12, 10): 'm', (12, 11): None, (12, 12): None, (12, 13): 'm', (12, 14): None, (12, 15): 'm', (13, 0): None, (13, 1): None, (13, 2): None, (13, 3): 'm', (13, 4): None, (13, 5): None, (13, 6): 'm', (13, 7): None, (13, 8): None, (13, 9): None, (13, 10): None, (13, 11): 'm', (13, 12): 'm', (13, 13): None, (13, 14): 'm', (13, 15): None, (14, 0): 'm', (14, 1): 'm', (14, 2): 'm', (14, 3): None, (14, 4): None, (14, 5): 'm', (14, 6): 'm', (14, 7): None, (14, 8): None, (14, 9): 'm', (14, 10): 'm', (14, 11): None, (14, 12): 'm', (14, 13): 'm', (14, 14): 'm', (14, 15): None, (15, 0): 'm', (15, 1): None, (15, 2): 'm', (15, 3): None, (15, 4): 'm', (15, 5): 'm', (15, 6): 'm', (15, 7): None, (15, 8): 'm', (15, 9): 'm', (15, 10): 'm', (15, 11): 'm', (15, 12): None, (15, 13): 'm', (15, 14): None, (15, 15): None}
>>> for t in test1:
	if t.values()!="m":
		print(t)

		
Traceback (most recent call last):
  File "<pyshell#164>", line 2, in <module>
    if t.values()!="m":
AttributeError: 'tuple' object has no attribute 'values'
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> for t in test1:
	if t.contains()!="m":
		print(t)

		
Traceback (most recent call last):
  File "<pyshell#167>", line 2, in <module>
    if t.contains()!="m":
AttributeError: 'tuple' object has no attribute 'contains'
>>> for t in test1:
	print(t)

	
(0, 0)
(0, 1)
(0, 2)
(0, 3)
(0, 4)
(0, 5)
(0, 6)
(0, 7)
(0, 8)
(0, 9)
(0, 10)
(0, 11)
(0, 12)
(0, 13)
(0, 14)
(0, 15)
(1, 0)
(1, 1)
(1, 2)
(1, 3)
(1, 4)
(1, 5)
(1, 6)
(1, 7)
(1, 8)
(1, 9)
(1, 10)
(1, 11)
(1, 12)
(1, 13)
(1, 14)
(1, 15)
(2, 0)
(2, 1)
(2, 2)
(2, 3)
(2, 4)
(2, 5)
(2, 6)
(2, 7)
(2, 8)
(2, 9)
(2, 10)
(2, 11)
(2, 12)
(2, 13)
(2, 14)
(2, 15)
(3, 0)
(3, 1)
(3, 2)
(3, 3)
(3, 4)
(3, 5)
(3, 6)
(3, 7)
(3, 8)
(3, 9)
(3, 10)
(3, 11)
(3, 12)
(3, 13)
(3, 14)
(3, 15)
(4, 0)
(4, 1)
(4, 2)
(4, 3)
(4, 4)
(4, 5)
(4, 6)
(4, 7)
(4, 8)
(4, 9)
(4, 10)
(4, 11)
(4, 12)
(4, 13)
(4, 14)
(4, 15)
(5, 0)
(5, 1)
(5, 2)
(5, 3)
(5, 4)
(5, 5)
(5, 6)
(5, 7)
(5, 8)
(5, 9)
(5, 10)
(5, 11)
(5, 12)
(5, 13)
(5, 14)
(5, 15)
(6, 0)
(6, 1)
(6, 2)
(6, 3)
(6, 4)
(6, 5)
(6, 6)
(6, 7)
(6, 8)
(6, 9)
(6, 10)
(6, 11)
(6, 12)
(6, 13)
(6, 14)
(6, 15)
(7, 0)
(7, 1)
(7, 2)
(7, 3)
(7, 4)
(7, 5)
(7, 6)
(7, 7)
(7, 8)
(7, 9)
(7, 10)
(7, 11)
(7, 12)
(7, 13)
(7, 14)
(7, 15)
(8, 0)
(8, 1)Traceback (most recent call last):
  File "<pyshell#170>", line 2, in <module>
    print(t)
KeyboardInterrupt
>>> for t in test1.values:
	print(t)

	
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    for t in test1.values:
TypeError: 'builtin_function_or_method' object is not iterable
>>> for t in test1.values():
	print(t)

	
None
m
None
None
None
m
m
m
m
None
m
m
m
None
None
m
None
None
m
m
m
m
m
None
None
m
None
None
m
m
None
None
None
None
m
m
m
None
None
None
None
None
None
None
None
None
None
None
m
None
None
None
None
m
None
None
m
None
None
m
None
m
m
m
m
None
None
m
m
m
m
None
m
Traceback (most recent call last):
  File "<pyshell#174>", line 2, in <module>
    print(t)
KeyboardInterrupt
>>> for t in test1.items():
	if t.items()!="m":
		print(t)

		
Traceback (most recent call last):
  File "<pyshell#176>", line 2, in <module>
    if t.items()!="m":
AttributeError: 'tuple' object has no attribute 'items'
>>> for t in test1.items():
	if t!="m":
		print(t)

		
((0, 0), None)
((0, 1), 'm')
((0, 2), None)
((0, 3), None)
((0, 4), None)
((0, 5), 'm')
((0, 6), 'm')
((0, 7), 'm')
((0, 8), 'm')
((0, 9), None)
((0, 10), 'm')
((0, 11), 'm')
((0, 12), 'm')
((0, 13), None)
((0, 14), None)
((0, 15), 'm')
((1, 0), None)
((1, 1), None)
((1, 2), 'm')
((1, 3), 'm')
((1, 4), 'm')
((1, 5), 'm')
((1, 6), 'm')
((1, 7), None)
((1, 8), None)
((1, 9), 'm')
((1, 10), None)
((1, 11), None)
((1, 12), 'm')
((1, 13), 'm')
((1, 14), None)
((1, 15), None)
((2, 0), None)
((2, 1), None)
((2, 2), 'm')
((2, 3), 'm')
((2, 4), 'm')
((2, 5), None)
((2, 6), None)
((2, 7), None)
((2, 8), None)
((2, 9), None)
((2, 10), None)
((2, 11), None)
((2, 12), None)
((2, 13), None)
((2, 14), None)
((2, 15), None)
((3, 0), 'm')
((3, 1), None)
((3, 2), None)
((3, 3), None)
((3, 4), None)
((3, 5), 'm')
((3, 6), None)
((3, 7), None)
((3, 8), 'm')
((3, 9), None)
((3, 10), None)
((3, 11), 'm')
((3, 12), None)
((3, 13), 'm')
((3, 14), 'm')
((3, 15), 'm')
((4, 0), 'm')
((4, 1), None)
Traceback (most recent call last):
  File "<pyshell#178>", line 3, in <module>
    print(t)
KeyboardInterrupt
>>> for t in test1.items():
	if t<>"m":
		print(t)
		
SyntaxError: invalid syntax
>>> 
