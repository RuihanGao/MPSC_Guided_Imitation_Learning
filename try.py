import pickle
import numpy as np 

# filename = 'pickle_testing.p'
# f = open(filename, 'wb')

# X1 = np.array([1, 2])
# Y1 = np.array([3, 4])

# pickle.dump((X1, Y1), f)
# # f.close()

# # X, Y = pickle.load(open(filename, 'rb'))
# # print(X, Y)

# X2 = np.array([5, 6])
# Y2 = np.array([7, 8])

# # f = open(filename, 'wb')
# pickle.dump((X2, Y2), f)


# X3 = np.array([9, 10])
# Y3 = np.array([11, 12])

# pickle.dump((X3, Y3), f)

# f.close()


# objs = []
# f = open(filename, 'rb')

# while 1:
# 	try:
# 		c = pickle.load(f)
# 		print(c)
# 		objs.append(c)
# 	except EOFError:
# 		break
# print("objs")
# print(objs)

x = [([  9.70177156e+01,   1.08404271e+01,   1.10434980e+01,
         3.62914103e-02]), 92.307692307692307, 10.0, 10, 0.0, 92.809364548494983, 10.0, 10, 0.0,]
print(x)
x = np.asarray(x)
print(type(x))
print(x.ravel())
