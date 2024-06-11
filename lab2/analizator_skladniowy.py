class InvalidSymbolException(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

def parse_S(input_str):
    if input_str[0] == '(':
        parse_W()
        return
    else:
        index = 0
        res = parse_C(input_str[index:])
        if res is False:
            raise InvalidSymbolException(f"Błąd na pozycji {index}, parser oczekiwal jednego z symboli [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], a jest: {input_str[index]}")
        while res:
            index += 1
            res = parse_C(input_str[index:])
        if input_str[index] == '.':
            # go onto looping for decimal part
            return


def parse_W(input_char):
    return True

def parse_O(input_char):
    return

def parse_C(input_char):
    if input_char in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    return False

input_string = str(input("Enter symbols string: "))

if len(input_string) < 1:
    print("Empty string was given")
    exit(1)

try:
    parse_S(input_string)
except Exception as e:
    print(str(e))

