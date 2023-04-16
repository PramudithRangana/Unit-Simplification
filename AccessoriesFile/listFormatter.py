from itertools import groupby

unit_list = ['K', 'm', 's', 'km', 'N', 'J', 'kg', 'cm']
separating_units = []


# input --> 'Nm⁻²⁴kJs⁻¹km²¹m'
def str_grouper(input_string):
    # unit string set grouping as alphabets and powers
    grouped_list = [''.join(g) for _, g in groupby(input_string, str.isalpha)]

    return grouped_list
# output --> ['Nm', '⁻²⁴', 'kJs', '⁻¹', 'km', '²¹', 'm', '⁻²']


# input --> ['Nm', '⁻²⁴', 'kJs', '⁻¹', 'km', '⁻²¹', 'm', '⁻²']
def unit_separator(grouped_list):
    temp_stored = ''
    separating_units.clear()

    # separate items and powers severally
    for grouped_item in grouped_list:
        # print(grouped_item)
        if grouped_item in unit_list:
            # grab proper units normally
            separating_units.append(grouped_item)

        elif grouped_item not in unit_list:
            # re correcting grouping mistakes

            if not grouped_item.isalpha():
                # grab superscript alpha
                separating_units.append(grouped_item)
            else:
                for su in grouped_item:
                    if temp_stored:
                        # reset temporary stored alpha as a unit
                        reset_unit = temp_stored + su
                        separating_units.append(reset_unit)

                        # clean the variable for the next one
                        temp_stored = ''

                    elif su in unit_list:
                        # grab proper units normally
                        separating_units.append(su)
                    else:
                        # grab alpha not in unit list
                        temp_stored = su

    return separating_units
# output --> ['N', 'm', '⁻²⁴', 'kJ', 's', '⁻¹', 'km', '⁻²¹', 'm', '⁻²']


# input --> ['N', 'm', '⁻²⁴', 'kJ', 's', '⁻¹', 'km', '⁻²¹', 'm', '⁻²']
def power_setter(grouped_list): return lambda sep='\n': ''.join((sep + x if x.isalpha() else x)
                                                                for x in unit_separator(grouped_list)).split(sep)[1:]

# output --> ['N', 'm⁻²⁴', 'kJ', 's⁻¹', 'km⁻²¹', 'm⁻²']


# input --> ['A', 'B', '2', 'C', '3', 'D', '4', 'E', 'B', '2', 'F', '6', 'D', 'C', '3', 'B']
def default_value_setter(my_list):
    def_setter = []
    i = 0
    while i < len(my_list):
        # if last item is a letter, then set (super scripted) 1 as an indices
        if i + 1 == len(my_list):
            if my_list[i].isalpha():
                def_setter.append([my_list[i], '¹'])
                break
        prev, cur = my_list[i], my_list[i + 1]

        if cur.isalpha():
            # set default value as (super scripted) 1
            def_setter.append([prev, '¹'])
            i += 1
        else:
            # set numeric values belongs to the letter together for creating nested list
            def_setter.append([prev, cur])
            i += 2
    return def_setter
# output --> [['A', '*'], ['B', '2'], ['C', '3'], ['D', '4'], ['E', '*'], ['B', '2'], ['F', '6'], ['D', '*'], ['C',
#                                                                                                      '3'], ['B', '*']]


# input --> [['N', '1'], ['m', '-24'], ['km', '-1'], ['s', '-1'], ['m', '2'], ['N', '-1'], ['s', '-1'], ['m', '2']]
def Simplifier(toSimple):
    measuring_unit_dict = {}

    for item in toSimple:
        key = item[0]
        value = '1' if len(item) == 1 else item[1]
        # print(f"key {key} | value {value}")

        # check either item exist or not in dictionary
        if key not in measuring_unit_dict.keys():
            measuring_unit_dict[key] = value

        else:
            # indices calculation
            value = int(measuring_unit_dict[key]) + int(value)

            if value == 0:
                # if the result is zero, then no need it furthermore
                measuring_unit_dict.pop(key)
            else:
                # append calculated result to the dictionary as a key - value pair
                measuring_unit_dict[key] = value

    return list(measuring_unit_dict.items())

# input --> [('m', -20), ('km', '-1'), ('s', -2)]
