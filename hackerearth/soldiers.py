
size = int(input())
ar = []
for i in range(size):
    ar.append(int(input()))

turns = int(input())
while turns>0:
    _scount = 0
    _psum = 0
    _power = int(input())

    for val in ar:
        if val <= _power:
            _scount+=1
            _psum+= val

    print('{} {}'.format(_scount,_psum))
    turns-=1