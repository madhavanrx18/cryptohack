a1 = 2
a2 = 3
a3 = 5

m1 = 5
m2 = 11
m3 = 17

M = m1*m2*m3

M1 = M/m1
M2 = M/m2
M3 = M/m3

def mul_inverse(m,M):
    for i in range(M):
        if(i*m % M ==1):
            return i
M1_1 = mul_inverse(m1,M)
M1_2 = mul_inverse(m2,M)
M1_3 = mul_inverse(m3,M)

print((a1*M1*M1_1 +a2*M2*M1_2+a3*M3*M1_3 )%M)
