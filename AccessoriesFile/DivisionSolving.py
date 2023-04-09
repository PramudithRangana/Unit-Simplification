from AccessoriesFile import listFormatter as lsF


def division_solve(input_string):
    def default_setter():
        # unit string set grouping as alphabets and powers
        grouped_list = lsF.str_grouper(input_string)

        pow_set_list = lsF.power_setting(grouped_list)

        # Highlight - 1 -
        def_setter = [
            pow_set_list[i] + '¹' if len(pow_set_list[i]) < 3 and pow_set_list[i].isalpha() else pow_set_list[i]
            for i in range(0, len(pow_set_list))]

        # convert normal values to scripts to join as a string
        return ''.join([i for i in def_setter])

    def operate_changer():
        ds = default_setter()

        # unit string set grouping as alphabets and powers
        grouped_list = lsF.str_grouper(ds)

        # Operate changing (in scripted mode)
        op_changed = [
            grouped_list[i][1:] if grouped_list[i][0] == '⁻' else ('⁻' + grouped_list[i])
            if not grouped_list[i].isalpha() else grouped_list[i] for i in range(len(grouped_list))]

        # convert normal values to scripts to join as a string
        return ''.join([i for i in op_changed])

    return operate_changer()
