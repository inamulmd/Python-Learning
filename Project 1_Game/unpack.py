my_tuple = (1, 2, 3, 4, 5)
a, *b, c = my_tuple
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

#indexing
my_tuple1 = ('a', 'b', 'c', 'd')

print(my_tuple1[0])   # 'a' (1st element)
print(my_tuple1[-1])  # 'd' (last element)

#indexing
my_tuple2 = (10, 20, 30, 40, 50)

print(my_tuple2[1:4])     # (20, 30, 40)
print(my_tuple2[:3])      # (10, 20, 30)
print(my_tuple2[::2])     # (10, 30, 50)
print(my_tuple2[::-1])    # (50, 40, 30, 20, 10)  # Reversed
