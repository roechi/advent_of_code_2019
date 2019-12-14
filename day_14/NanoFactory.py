from functools import reduce
import math
from collections import defaultdict

class NanoFactory:
    def __init__(self, dependencies: [str]) -> None:
        self.reaction_table = dict()

        for d in dependencies:
            s = d.split('=>')
            r = s[-1][1:]
            r_s = r.split(' ')
            result = r_s[1]
            resulting_amount = r_s[0]

            if ', ' in s[:-1][0]:
                required = s[:-1][0].split(', ')
            else:
                required = [str(s[0][:-1])]

            entry = {'res': int(resulting_amount)}
            req = list()
            for r in required:
                req.append((r.split(' ')[1], int(r.split(' ')[0])))

            entry['req'] = req
            self.reaction_table[result] = entry

    def solve(self):
        req_for_fuel = self.reaction_table['FUEL']

        assert req_for_fuel['res'] == 1
        return self.calc_ore('FUEL', 1)

    def calc_ore(self, target: str, target_amount: int, surplus: dict = None):
        if surplus is None:
            surplus = defaultdict(int)
        if target == 'ORE':
            return target_amount
        elif target_amount <= surplus[target]:
            surplus[target] -= target_amount
            return 0

        target_amount -= surplus[target]
        surplus[target] = 0
        ore = 0
        req_chems = self.reaction_table[target]
        output_amount = req_chems['res']
        copies = math.ceil(target_amount / output_amount)

        for chem in req_chems['req']:
            input_amount = chem[1]
            input_amount *= copies
            ore += self.calc_ore(chem[0], input_amount, surplus)
        surplus[target] += output_amount * copies - target_amount
        return ore

    def produce_fuel(self, total_ore):
        ore_per_fuel = self.solve()
        fuel_to_produce = total_ore // ore_per_fuel
        max_fuel = 0
        surplus = defaultdict(int)

        while total_ore and fuel_to_produce:
            ore_used = self.calc_ore('FUEL', fuel_to_produce, surplus)
            if ore_used > total_ore:
                fuel_to_produce //= 2
            else:
                total_ore -= ore_used
                max_fuel += fuel_to_produce
        return max_fuel
