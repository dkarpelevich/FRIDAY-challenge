import re, json


def read_input_file(old_file):
    addresses_list = []
    with open(old_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            addresses_list.append(line)
    print('read_input_file addresses_list', addresses_list)
    return addresses_list


def parse_input_addresses(address_list):
    result_list = []

    for i in address_list:

        match_first_digit = re.match(r'\d+', i, re.I)
        match_house_number = re.search(r' no.\d+.*$|d.\d+.*$', i, re.I)

        if match_first_digit and not match_house_number:
            if i.find(', ') != -1:
                house_number = i[:i.index(', ')]
            else:
                house_number = i[:i.index(' ')]
            street_wo_house = i[len(house_number):]
            start = street_wo_house.index(' ') + len(' ')
            string_inc = '{"street": ' + '"' + street_wo_house[start:street_wo_house.index('\n')] + '",' + \
                         '"housenumber": ' + '"' + house_number + '"}'
            if street_wo_house.startswith(' ') or street_wo_house.startswith(', '):
                result_list.append(string_inc)
            else:
                print('Match for {} failed'.format(i))



        else:
            print("No match!!")
    return result_list


def write_to_output_file(new_file, data):
    result_list = parse_input_addresses(data)
    json_output = '{"addresses": [' + ','.join(result_list) + ']}'
    try:
        json.loads(json_output)
    except ValueError:
        print('Json object is not correct!', json_output)
        return
    with open(new_file, 'w') as outfile:
        outfile.write(json.dumps(json.loads(json_output), indent=4))


addresses_list1 = read_input_file('addresses')
# parse_input_addresses(addresses_list1)
write_to_output_file('parsed_file', addresses_list1)

# go by input file
# wright strings to list
# go through list and parse it depending on the class
# put result to list of strings or explicitly to file like
# line = '{"addresses": [' + str(result.update({'line': i, 'street': line.split(), "home": 'd'}))

# if it starts with digit -> started digit is housenumber, after space is street
# if 'No' in the string -> Before 'No' is street , after 'No till end of line' is housenumber,
# if there is a digit -> everything started from digit to end is housenumber, other part is street
