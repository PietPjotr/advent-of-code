import hashlib


def solve():
    code1 = ''
    code2 = ['-' for _ in range(8)]
    inp = 'wtnhxymk'
    i = 0
    while len(code1) < 8 or '-' in code2:
        to_hash = inp + str(i)
        hashed = hashlib.md5(to_hash.encode()).hexdigest()
        if hashed.startswith('00000'):
            code1 += hashed[5]
            if hashed[5].isdigit():
                index = int(hashed[5])
                if 0 <= index <= 7 and code2[index] == '-':
                    code2[index] = hashed[6]
        i += 1
    print(code1[:8])
    print(''.join(code2))


solve()