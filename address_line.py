import json

def filters(txt, old_file, new_file):
    result = {}
    i = 0
    with open(new_file, 'w') as outfile, open(old_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            line = '{"addresses": [' + str(result.update({'line': i, 'street': line.split(), "home": 'd'}))
            i += 1


filters('Winterallee', 'addresses', 'separate_addresses')
