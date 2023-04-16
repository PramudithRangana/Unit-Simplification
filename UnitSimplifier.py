from itertools import groupby
from AccessoriesFile import scriptChanger as scrC, listFormatter as lF, DivisionSolving as devS
import re

unit_list = ['K', 'm', 's', 'km', 'N', 'J', 'kg', 'cm']


class UnitSimplifying:
    def __init__(self, unit):
        self.unit = unit
        self.result = None

        self.main()

    def items_group(self):
        # unit string set grouping as alphabets and powers
        return lF.str_grouper(self.unit)

    def unit_separate(self):
        # power set to the grouped units
        return lF.power_setter(self.items_group())()

    def unit_group(self):
        separating_units = self.unit_separate()

        # Units grouping with their (super scripted) powers as a nested list
        for itm in separating_units:
            groupedList = [''.join(g) for _, g in groupby(itm, str.isalpha)]

            # grab index number
            idx = separating_units.index(itm)

            # assign value to the related index
            separating_units[idx] = groupedList

        return separating_units

    def ResultFinalize(self):
        # scripted values change as a normal values
        nom_list = [[s[0]] + [(scrC.supScr_to_norm(s[1]))] if len(s) > 1 else [s[0], 1] for s in self.unit_group()]

        # scripted to normal values
        powCal = [s[0] if s[1] == 1 else [s[0]] + [(scrC.norm_to_supScr(s[1]))] for s in lF.Simplifier(nom_list)]

        # alternate from nested style to flat style
        ResultInList = [element for innerList in powCal for element in innerList]

        return ''.join([i for i in ResultInList])

    def main(self):
        cal_list = []

        try:
            # control the function
            for st in [item.strip() for item in re.split(r" ", self.unit)]:
                if st != '+' and st != '-':
                    if '/' in st:
                        split_str = st.split('/')

                        divide = devS.division_solve(split_str[1])
                        self.unit = split_str[0] + divide

                        # get simplified result
                        cal_list.append(self.ResultFinalize())

                    else:
                        self.unit = st

                        # get simplified result
                        cal_list.append(self.ResultFinalize())
                else:
                    # Append operators if existing
                    cal_list.append(st)

        except Exception as e:
            raise e

        finally:
            # get simplified result
            self.result = ' '.join(u for u in cal_list)

    def __str__(self):
        return self.result
