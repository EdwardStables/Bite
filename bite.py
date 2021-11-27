from typing import Union

class Num:
    def __init__(self, num: Union[int, str], base=16, size=0):
        if type(num) == int:
            self.num = num
        elif type(num) == str:
            self.num = int(num, base=16)

        self.set_conversions()
        self.set_size(size)

    def set_conversions(self):
        self.bin = bin(self.num)
        self.oct = oct(self.num)
        self.hex = hex(self.num)

    def set_size(self, size):
        self.size = max(size, len(self.bin)-2)

    def __len__(self):
        return self.size

    def __repr__(self):
        return str(self.num)

    def __getitem__(self, i):
        return self.bin[len(self.bin) - 1 - i]