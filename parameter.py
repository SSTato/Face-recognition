import os
'''f = open(os.path.abspath('parameter.txt'), 'r')

ip = f.read().splitlines()[0].split('ip:')[1]
threhold = f.read().splitlines()[1].split(':')[1]
print(ip,threhold)
'''

a = open(os.path.abspath('parameter.txt'), 'r').read().splitlines()[0].split('ip:')[1]
b = open(os.path.abspath('parameter.txt'), 'r').read().splitlines()[1].split(':')[1]
print(a,b)