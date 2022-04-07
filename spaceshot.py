import random
a = str(random.randint(0, 10000000000000000))

f = open(a + '.txt', 'w+')

for i in range(1000000000):
    f.write('llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll')

f.close()
