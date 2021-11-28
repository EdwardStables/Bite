from typing import Union

class Num:
    def __init__(self, num: Union[int, str], base=16, size=0):
        if type(num) == int:
            self.num = num
        elif type(num) == str:
            self.num = int(num, base=16)

        self.bin = bin(self.num)
        self.size = None
        self.set_size(size)
        self.bin = get_bin(self.num, self.size)

    def set_size(self, size):
        self.size = max(size, len(self.bin)-2)

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

def get_bin(num: int, length: int):
    bin_num = bin(num)[2:]
    if length > (current := len(bin_num)):
        bin_num = "0"*(length-current) + bin_num
    return "0b" + bin_num

