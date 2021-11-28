from bite import Num


def test_initialization():
    n = Num(23)
    assert n.num == 23
    assert n.bin == "0b10111"
    #assert n.oct == "0o27"
    #assert n.hex == "0x17"
    assert n.size == 5

def test_base_arg():
    n = Num("12", base=16)
    assert n.num == 18
    assert n.bin == "0b10010"

def test_size_arg():
    n = Num(193)
    assert n.size == 8

    n = Num(193, size = 12)
    assert n.size == 12 

    n = Num(193, size = 4)
    assert n.size == 8

def test_size_arg_ext():
    n = Num(1, size=8)
    assert n.bin == "0b00000001"

def test_len():
    n = Num(193)
    assert len(n) == 8

def test_repr(capsys):
    n = Num(231)
    print(n, end="")
    out, err = capsys.readouterr()
    assert out == "231"
    assert err == ""

def test_indexing():
    n = Num(1, size=4)
    assert n[0] == "1"
    assert n[1] == "0"
    assert n[2] == "0"
    assert n[3] == "0"

def test_slicing():
    n = Num(1, size=4)
    assert n[3:1] == "000"
    assert n[1:0] == "01"