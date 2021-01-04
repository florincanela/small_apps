from collections import OrderedDict,Counter,defaultdict

li = [1,2,3,4,5,6,7,7,7,7]

test = 'Si era una la parinti si mandra in toate cele'

x = Counter(test)

x = defaultdict(lambda: 0, x)


d = OrderedDict()
d['a'] = 1
d['c'] = 3
d['b'] = 2

d2 = OrderedDict()
d2['c'] = 3
d2['a'] = 1
d2['b'] = 2


print(d == d2)