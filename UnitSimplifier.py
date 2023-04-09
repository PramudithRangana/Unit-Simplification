from itertools import groupby
from AccessoriesFile import scriptChanger as scrC, listFormatter as lF, DivisionSolving as devS

unit_list = ['K', 'm', 's', 'km', 'N', 'J', 'kg', 'cm']


class UnitSimplifying:
    def __init__(self, unit):
        self.unit = unit
        self.result = None

        self.simplified()

    def items_grouping(self):
        # unit string set grouping as alphabets and powers
        return lF.str_grouper(self.unit)

    def unit_separate(self):
        # get grouped string
        gl = self.items_grouping()

        # power set to the grouped units
        return lF.power_setting(gl)

    def unit_grouping(self):
        separating_units = self.unit_separate()

        # Units grouping with their (super scripted) powers as a nested list
        for itm in separating_units:
            groupedList = [''.join(g) for _, g in groupby(itm, str.isalpha)]

            # grab index number
            idx = separating_units.index(itm)

            # assign value to the related index
            separating_units[idx] = groupedList

        return separating_units

    def unit_simple(self):
        nested_li = self.unit_grouping()

        # scripted values change as a normal values
        nm_l = [[s[0]] + [(scrC.supScr_to_norm(s[1]))] if len(s) > 1 else [s[0], 1] for s in nested_li]

        # units simplification
        simplify = lF.unit_simplifier(nm_l)

        # scripted to normal values
        return [s[0] if s[1] == 1 else [s[0]] + [(scrC.norm_to_supScr(s[1]))] for s in simplify]

    def item_joining(self):
        us = self.unit_simple()

        # alternate from nested style to flat style
        flatList = [element for innerList in us for element in innerList]

        return ''.join([i for i in flatList])

    def simplified(self):
        # control the function
        if '/' in self.unit:
            split_str = self.unit.split('/')

            divide = devS.division_solve(split_str[1])
            self.unit = split_str[0] + divide

            self.result = self.item_joining()

        else:
            self.result = self.item_joining()

    def __str__(self):
        return self.result
