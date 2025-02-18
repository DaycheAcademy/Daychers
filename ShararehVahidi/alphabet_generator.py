

def alphabet_generator(start='c', end='x', step=2):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    i=alphabets.index(start)
    j=alphabets.index(end)
    for alphabet in alphabets[i:j:step]:
        yield alphabet

for a in alphabet_generator('l','w'):
    print(a)








