import re


def read_input_file(old_file):
    addresses_list = []
    with open(old_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            addresses_list.append(line)
    print('read_input_file addresses_list', addresses_list)
    return addresses_list


def parse_input_addresses(address_list):
    print('parse_input_addresses begin addresses_list', address_list)
    result_string = '{"addresses": ['
    for i in address_list:
        match_obj = re.match(r'\d+', i, re.I)
        if match_obj:
            street_wo_house = i[len(match_obj.group(0)):]
            start = street_wo_house.index(' ') + len(' ')
            string_inc = '{"street":' + '"' + street_wo_house[start:street_wo_house.index('\n')] + '",'
            if street_wo_house.startswith(' '):
                result_string += string_inc
            elif street_wo_house.startswith(', '):
                result_string += string_inc
            result_string += '"housenumber":' + '"' + str(match_obj.group(0)) + '"}'
        else:
            print("No match!!")
    print(result_string)
    print('parse_input_addresses end addresses_list', address_list)


def write_to_output_file(new_file, data):
    with open(new_file, 'w') as outfile:
        outfile.write(data)


print('19')
addresses_list1 = read_input_file('addresses')
print('21')
parse_input_addresses(addresses_list1)
# write_to_output_file('parsed_file', data1)

# go by input file
# wright strings to list
# go through list and parse it depending on the class
# put result to list of strings or explicitly to file like
# line = '{"addresses": [' + str(result.update({'line': i, 'street': line.split(), "home": 'd'}))

# if it starts with digit -> started digit is housenumber, after space is street
# if 'No' in the string -> Before 'No' is street , after 'No till end of line' is housenumber,
# if there is a digit -> everything started from digit to end is housenumber, other part is street
