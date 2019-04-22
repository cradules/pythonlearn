my_dict = {'key1': 'value1', 'key2': 'value2'}

print(my_dict['key1'])

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.88}

print(prices_lookup['apple'])

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}

print(d['k3']['insideKey'])

print(d['k2'][2].bit_length())

d['k3'] = 300

print(d)
print(d['k3'])

d['k1'] = "NEW VALUE"

print(d['k1'])

print(d.keys())
print(d.values())

