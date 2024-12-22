
from sympy.ntheory import discrete_log

a = 288260533169915
p = 1007621497415251

with open(r"D:\CRYPTO\Cryptohack\modular\output.txt",'r') as output:
    data = output.read().split(', ')

for i in range(len(data)):
    data[i] = int(data[i])

# plaintext = ''
# for i in range(len(data)):
#     print("processing..,",data[i])
#     n=data[i]
#     try:
#         e=discrete_log(p,n,a)
#     except:
#         n= -data[i]%p
#         e=discrete_log(p,n,a)
#     n_new = pow(a,e,p)
#     if n_new == data[i]:
#         plaintext += '1'
#     else:
#         plaintext += '0'
#     print(plaintext)

plaintext = "01100011011100100111100101110000011101000110111101111011011100000011010001110100011101000110010101110010011011100111001101011111001100010110111001011111011100100110010100110101011010010110010001110101001100110111001101111101"

plaintext = [plaintext[i:i+8] for i in range(0,len(plaintext),8)]

print(plaintext)

characters = ''.join(chr(int(b,2)) for b in plaintext)

print(characters)