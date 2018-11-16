import json
import re


def read_input_file(input_file):
    string_inc: str = ''
    with open(input_file, 'r', encoding='utf-8') as infile:
        print('Reading addresses from file:', input_file)
        for line in infile:
            string_inc += parse_input_addresses(line)
    return string_inc


def parse_input_addresses(line):
    json_address: str = ''

    match_first_digit = re.match(r'^\d+', line, re.I)
    match_house_label = re.search(r'\b(no \d+).*$|\b(no\.\d+).*$|\b(no\. \d+).*$|\b(no\d+).*$|'
                                  r'\b(d \d+).*$|\b(d\.\d+).*$|\b(d\. \d+).*$|\b(d\d+).*$|'  # Russian address
                                  r'\b(bud \d+).*$|\b(bud\.\d+).*$|\b(bud\. \d+).*$|\b(bud\d+).*$',  # Ukraine address
                                  line, re.I)

    if match_first_digit and not match_house_label:
        try:
            house_number = (line[:line.index(', ')] if (line.find(', ') != -1) else line[:line.index(' ')])
            street_wo_house = line[len(house_number):]
            start = street_wo_house.index(' ') + len(' ')
            json_address = '{"street": ' + '"' + street_wo_house[start:street_wo_house.rindex('\n')] + '",' + \
                           '"housenumber": ' + '"' + house_number + '"},'
        except (AttributeError, ValueError) as e:
            last_symbol = (line.rindex('\n') if line.endswith('\n') else len(line))
            print('Address "{}" is incorrect.'.format(line[:last_symbol]), e)

    elif match_house_label:
        try:
            house_number = match_house_label.group()
            json_address = address_starts_from_letter(line, house_number)
        except (AttributeError, ValueError) as e:
            last_symbol = (line.rindex('\n') if line.endswith('\n') else len(line))
            print('Address "{}" is incorrect.'.format(line[:last_symbol]), e)

    else:
        try:
            house_number = re.search(r'\b(\d+).*$', line, re.I).group()
            json_address = address_starts_from_letter(line, house_number)
        except (AttributeError, ValueError) as e:
            last_symbol = (line.rindex('\n') if line.endswith('\n') else len(line))
            print('Address "{}" is incorrect.'.format(line[:last_symbol]), e)

    return json_address


def address_starts_from_letter(i, house_number):
    street_wo_house = i[:i.index(house_number)].rstrip()
    if street_wo_house.endswith(','):
        street_wo_house = street_wo_house[:len(street_wo_house) - 1]
    json_address = '{"street": ' + '"' + street_wo_house + '",' + \
                   '"housenumber": ' + '"' + house_number + '"},'
    return json_address


def write_to_output_file(input_file, new_file):
    result_string = read_input_file(input_file)
    json_output = '{"addresses": [' + result_string[:len(result_string) - 1] + ']}'
    try:
        json.loads(json_output)
    except ValueError:
        print('Json object is not correct!', json_output)
        return
    with open(new_file, 'w') as outfile:
        outfile.write(json.dumps(json.loads(json_output), indent=4, ensure_ascii=False))
        print('Output file:', new_file)


write_to_output_file('addresses', 'addresses.json')
