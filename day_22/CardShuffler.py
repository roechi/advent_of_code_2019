from sympy.core.numbers import mod_inverse

class CardShuffler:
    def __init__(self, deck_size: int) -> None:
        self.deck = [i for i in range(deck_size)]

    def deal_into_new_stack(self):
        self.deck.reverse()

    def cut(self, n: int):
        new_deck = self.deck[n:]
        new_deck.extend(self.deck[:n])
        self.deck = new_deck

    def deal_with_increment(self, n: int):
        new_deck = [None for i in range(len(self.deck))]

        for i in range(len(self.deck)):
            new_deck[(i * n) % len(new_deck)] = self.deck[i]

        self.deck = new_deck

    def perform(self, operations: [str]):
        cleaned_ops = list(map(lambda s: s.rstrip(), operations))

        for o in cleaned_ops:
            if 'deal into' in o:
                self.deal_into_new_stack()
            elif 'cut' in o:
                o = o.split(' ')
                self.cut(int(o[-1]))
            elif 'deal with' in o:
                o = o.split(' ')
                self.deal_with_increment(int(o[-1]))


class CardShuffler2:
    def __init__(self, number_of_cards: int, card_to_track: int) -> None:
        self.cards = number_of_cards
        self.pos = card_to_track

    def deal_into_new_stack(self):
        self.pos = self.cards - 1 - self.pos

    def cut(self, c: int, inverse: bool = False):
        if not inverse:
            self.pos = (self.pos - c) % self.cards
        else:
            self.pos = (self.pos + c) % self.cards

    def deal_with_increment(self, i: int, inverse: bool = False):
        if not inverse:
            self.pos = (self.pos * i) % self.cards
        else:
            self.pos = (mod_inverse(i, self.cards) * self.pos) % self.cards

    def perform(self, operations: [str], inverse: bool = False):
        cleaned_ops = list(map(lambda s: s.rstrip(), operations))

        for o in cleaned_ops:
            if 'deal into' in o:
                self.deal_into_new_stack()
            elif 'cut' in o:
                o = o.split(' ')
                self.cut(int(o[-1]), inverse)
            elif 'deal with' in o:
                o = o.split(' ')
                self.deal_with_increment(int(o[-1]), inverse)
