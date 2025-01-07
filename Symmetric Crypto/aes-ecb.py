import requests

def get_request(param):
    r = requests.get("https://aes.cryptohack.org/ecb_oracle/encrypt/"+param)
    data = r.json()
    data = data['ciphertext']
    return data

# list with hex values from 01 to ff
byte_list = []
for i in range(1,256):
    a = hex(i)[2:]
    if len(a)==1:
        a='0'+a
    byte_list.append(a)

def get_padding(r):
    return byte_list[r-1]

payload = '00'*7
ciphertext = get_request(payload)
last_block = ciphertext[-32:]
pad_count = 15
flag = ''

while len(flag) < 32 :
    payload += '00'
    ciphertext = get_request(payload)
    last_block = ciphertext[-32:]
    

    for b in byte_list:
        input_param = b + flag + get_padding(pad_count)*pad_count
        result = get_request(input_param)
        first_block = result[:32]
        print(first_block)
        if first_block == last_block:
            print("found",b)
            flag = b + flag
            break
    print(flag)

