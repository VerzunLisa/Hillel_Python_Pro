class BinaryNumber(object):
    def __init__(self, value):
        """Initialization value"""
        self.value = int(value)

    def __and__(self, other):
        """AND operation between two binary numbers"""
        return self.value & other.value

    def __or__(self, other):
        """OR operation between two binary numbers"""
        return self.value | other.value

    def __xor__(self, other):
        """XOR operation between two binary numbers"""
        return self.value ^ other.value

    def __invert__(self):
        """NOT operation"""
        return ~self.value & 0xff

    def __repr__(self):
        """Returns the binary representation of a number"""
        return f"{bin(self.value)[2:]:0>8}"


def test_binary():
    """Test operations"""
    number1 = BinaryNumber("11001100")
    number2 = BinaryNumber("10101011")
    result_and = number1 & number2
    print(f"AND: {result_and}")
    result_or = number1 | number2
    print(f"OR: {result_or}")
    result_xor = number1 ^ number2
    print(f"XOR: {result_xor}")
    result_not = ~number1
    print(f"NOT: {result_not}")


test_binary()
