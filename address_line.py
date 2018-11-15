import json
import re


def read_input_file(input_file):
    address_list = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        print('Reading addresses from file:', input_file)
        for line in infile:
            address_list.append(line)
    return address_list


def parse_input_addresses(address_list):
    string_inc: str = ''
    for i in address_list:

        match_first_digit = re.match(r'^\d+', i, re.I)
        match_house_label = re.search(r'\b(no \d+).*$|\b(no\.\d+).*$|\b(no\. \d+).*$|\b(no\d+).*$|'
                                      r'\b(d \d+).*$|\b(d\.\d+).*$|\b(d\. \d+).*$|\b(d\d+).*$|'
                                      r'\b(bud \d+).*$|\b(bud\.\d+).*$|\b(bud\. \d+).*$|\b(bud\d+).*$',
                                      i, re.I)

        if match_first_digit and not match_house_label:
            house_number = (i[:i.index(', ')] if (i.find(', ') != -1) else i[:i.index(' ')])
            street_wo_house = i[len(house_number):]
            start = street_wo_house.index(' ') + len(' ')
            string_inc += '{"street": ' + '"' + street_wo_house[start:street_wo_house.index('\n')] + '",' + \
                          '"housenumber": ' + '"' + house_number + '"},'

        elif match_house_label:
            try:
                house_number = match_house_label.group()
                string_inc += address_starts_from_letter(i, house_number)
            except AttributeError as e:
                print('Address "{}" is incorrect'.format(i[:i.index('\n')]), e)

        else:
            try:
                house_number = re.search(r'\b(\d+).*$', i, re.I).group()
                string_inc += address_starts_from_letter(i, house_number)
            except AttributeError as e:
                print('Address "{}" is incorrect'.format(i[:i.index('\n')]), e)

    return string_inc


def address_starts_from_letter(i, house_number):
    street_wo_house = i[:i.index(house_number)].rstrip()
    if street_wo_house.endswith(','):
        street_wo_house = street_wo_house[:len(street_wo_house) - 1]
    string_inc = '{"street": ' + '"' + street_wo_house + '",' + \
                 '"housenumber": ' + '"' + house_number + '"},'
    return string_inc


def write_to_output_file(new_file, data):
    result_string = parse_input_addresses(data)
    json_output = '{"addresses": [' + result_string[:len(result_string) - 1] + ']}'
    try:
        json.loads(json_output)
    except ValueError:
        print('Json object is not correct!', json_output)
        return
    with open(new_file, 'w') as outfile:
        outfile.write(json.dumps(json.loads(json_output), indent=4, ensure_ascii=False))
        print('Output file:', new_file)


addresses_list = read_input_file('addresses')
write_to_output_file('parsed_file', addresses_list)
