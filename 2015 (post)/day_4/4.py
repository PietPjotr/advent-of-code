import hashlib


def solve(check):
    lines = 'bgvyzdsv'
    i = 0
    while True:
        encode = lines + str(i).strip()
        result = hashlib.md5(encode.encode('ascii'))
        if result.hexdigest().startswith(check):

            print(i)
            break
        i += 1


solve('00000')
solve('000000')
