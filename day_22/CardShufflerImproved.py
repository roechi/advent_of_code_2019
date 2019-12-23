from sympy.core import numbers


class CardShufflerImproved:

    @staticmethod
    def mod_inverse(n, k):
        return numbers.mod_inverse(k, n)

    @staticmethod
    def mod(n, *coeffs):
        return tuple(coeff % n for coeff in coeffs)

    @staticmethod
    def deal_new_stack(n, a, b, inverse=False):
        if not inverse:
            return CardShufflerImproved.mod(n, -1 * a, -1 * b - 1)
        else:
            return CardShufflerImproved.mod(n, -1 * a, -1 * b - 1)

    @staticmethod
    def cut(n, k, a, b, inverse=False):
        if not inverse:
            return CardShufflerImproved.mod(n, a, b - k)
        else:
            return CardShufflerImproved.mod(n, a, b + k)

    @staticmethod
    def deal_with_increment(n, k, a, b, inverse=False):
        if not inverse:
            return CardShufflerImproved.mod(n, a * k, b * k)
        else:
            return CardShufflerImproved.mod(n, a * CardShufflerImproved.mod_inverse(n, k),
                                            b * CardShufflerImproved.mod_inverse(n, k))

    @staticmethod
    def get_coeffs(n, operations, inverse=False):
        if inverse:
            operations = operations[::-1]

        coeffs = (1, 0)
        for operation in operations:
            if 'deal into' in operation:
                coeffs = CardShufflerImproved.deal_new_stack(n, coeffs[0], coeffs[1], inverse)
            elif 'cut' in operation:
                o = operation.split(' ')
                k = int(o[-1])
                coeffs = CardShufflerImproved.cut(n, k, coeffs[0], coeffs[1], inverse)
            elif 'deal with' in operation:
                o = operation.split(' ')
                k = int(o[-1])
                coeffs = CardShufflerImproved.deal_with_increment(n, k, coeffs[0], coeffs[1], inverse)

        return coeffs

    @staticmethod
    def shuffle(n, card, coeffs, rounds=1):
        a, b = coeffs
        return (pow(a, rounds, n) * card + b * (pow(a, rounds, n) - 1) * CardShufflerImproved.mod_inverse(n, a - 1)) % n


