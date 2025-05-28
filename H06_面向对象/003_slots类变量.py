import sys

class WithoutSlots:    
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):        
        self.a = a        
        self.b = b        
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.o = o
        self.p = p
        self.q = q
        self.r = r  
        self.s = s
        self.t = t
        self.u = u
        self.v = v
        self.w = w
        self.x = x
        self.y = y
        self.z = z

class WithSlots:    
    __slots__ = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")    
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):        
        self.a = a        
        self.b = b        
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.o = o
        self.p = p
        self.q = q
        self.r = r  
        self.s = s
        self.t = t
        self.u = u
        self.v = v
        self.w = w
        self.x = x
        self.y = y
        self.z = z

# 测试内存占用
obj1 = WithoutSlots(1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
obj2 = WithSlots(1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)

print(f"Without slots: {sys.getsizeof(obj1)} bytes")  # 约80 bytes
print(f"With slots: {sys.getsizeof(obj2)} bytes")     # 约48 bytes