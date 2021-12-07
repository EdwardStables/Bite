from typing import Union

class Num:
    def __init__(self, num: Union[int, str], base=16, size=None):
        if type(num) == int:
            self.num = num
        elif type(num) == str:
            self.num = int(num, base=base)

        default_bin = bin(self.num)
        default_size = len(default_bin) - 2
        if size is not None and default_size > size:
            self.num = truncate(self.num, default_size - size)
            self.size = size
        elif size is not None and default_size <= size:
            self.size = size
        elif size is None:
            self.size = default_size
        
        self.bin = get_bin(self.num, self.size)
        self.hex = hex(self.num)
        self.oct = oct(self.num)
        self.dec = "0d" + str(self.num)

    def __len__(self):
        return self.size

    def __repr__(self):
        return str(self.num)

    def __getitem__(self, i):
        access = lambda ind: self.bin[len(self.bin) - 1 - ind]
        if type(i) == int:
            return access(i)
        else: #otherwise assume it is a slice
            return "".join([access(j) for j in range(i.start, i.stop-1, -1)])

    def __add__(self, other):
        return Num(self.num + other.num)

    def __sub__(self, other):
        return Num(self.num - other.num)

    def __lshift__(self, shift):
        return Num(self.bin[2:][shift:]+"0"*shift,base=2)

    def __rshift__(self, shift):
        return Num("0"*shift + self.bin[2:][: (-shift) if shift else len(self.bin)-1],base=2)

def get_bin(num: int, length: int):
    bin_num = bin(num)[2:]
    if length > (current := len(bin_num)):
        bin_num = "0"*(length-current) + bin_num
    return "0b" + bin_num

def truncate(num: int, bits: int):
    as_bits = bin(num)[2:]
    if bits > len(as_bits):
        raise Exception(f"Trying to truncate binary number {as_bits} by {bits} bits.")
    return int(as_bits[bits:], base=2)