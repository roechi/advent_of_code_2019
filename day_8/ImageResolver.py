from functools import reduce


class ImageResolver:

    def __init__(self) -> None:
        self.layers = []

    def decode(self, values: [int], width: int, height: int):
        layers = list()

        for l in range(int(len(values) / (width * height))):
            layer = [[None for i in range(height)] for j in range(width)]
            x = 0
            y = 0
            for val in values[l * width * height:(l + 1) * width * height]:
                layer[x][y] = val
                x += 1
                if x == width:
                    x = 0
                    y += 1
            layers.append(layer)

        self.layers = layers

    def layer_with_fewest_occurrences(self, digit: int):
        ls = self.layers.copy()
        ls.sort(key=lambda layer: ImageResolver.count_digit_on_layer(digit, layer))
        return ls[0]

    def render(self):
        ls = self.layers.copy()

        stacked = reduce(ImageResolver.stack_layers, ls)

        return stacked

    @staticmethod
    def stack_layers(l1, l2):
        width = len(l1)
        height = len(l1[0])
        result = [[None] * height for i in range(width)]
        for x in range(width):
            for y in range(height):
                if l1[x][y] == 2:
                    result[x][y] = l2[x][y]
                else:
                    result[x][y] = l1[x][y]
        return result

    @staticmethod
    def count_digit_on_layer(digit, layer):
        return sum(x.count(digit) for x in layer)

    def print_layer(self, layer):
        for y in range(len(layer[0])):
            line = ''
            for x in range(len(layer)):
                line += str(layer[x][y]) + ' '
            print(line)
        print()

    def print_layer_ASCII(self, layer):
        for y in range(len(layer[0])):
            line = ''
            for x in range(len(layer)):
                line += '0' if layer[x][y] == 1 else ' '
            print(line)
        print()

    def print_layers(self):
        layer_count = 0
        for l in self.layers:
            print('Layer {}:'.format(layer_count))
            self.print_layer(l)
            layer_count += 1

