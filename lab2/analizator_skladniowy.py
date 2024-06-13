# Analizator składniowy - Lingwistyka Matematyczna
# Autor: Mikołaj Rajczyk 254403

class InvalidSymbolException(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

first_S = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
first_W = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
first_O = ['+', '-', '*', ':', '^']
first_C = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
curr_char_index = 0

def parse_S(input_str):
    global curr_char_index
    try:
        # check if input character belongs to S first symbols
        if input_str[curr_char_index] in first_S:
            # check if next symbol is (, then parse for w
            if input_str[curr_char_index] == '(':
                curr_char_index += 1
                # go into function W paring
                res = parse_W(input_str)
                if not res:
                    raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected one of symbols {first_W}, but encountered: {input_str[curr_char_index]}")
                elif input_str[curr_char_index] != ')':
                    raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected symbol ')', but encountered: {input_str[curr_char_index]}")
                curr_char_index += 1
            else:
                # go into function C parsing for digits
                res = parse_C(input_str)
                if res is False:
                    raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected one of symbols {first_C}, but encountered: {input_str[curr_char_index]}")
                # parse all following digits
                while res:
                    curr_char_index += 1
                    # if we encounter empty symbol instead of ;, string is partially-OK
                    if len(input_str) == curr_char_index:
                        raise InvalidSymbolException("String was not terminated with symbol ;, but belongs to grammar.")
                    res = parse_C(input_str)
                # if encountered dot check for following digits in the decimal part
                if input_str[curr_char_index] == '.':
                    curr_char_index += 1
                    res = parse_C(input_str)
                    if res is False:
                        raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected one of symbols {first_C}, but encountered: {input_str[curr_char_index]}")
                    while res:
                        curr_char_index += 1
                        # if string ends on empty symbol when expecting ;, it partly belongs to grammar
                        if len(input_str) == curr_char_index:
                            raise InvalidSymbolException("String was not terminated with symbol ;, but belongs to grammar.")
                        # go into function C parsing for digits
                        res = parse_C(input_str)
            # check if next symbol is operation sign (function O)
            res = parse_O(input_str)
            if res == False:
                # if last symbol is ;, end of parsing
                if input_str[curr_char_index] == ';':
                    curr_char_index += 1
                    if len(input_str) == curr_char_index:
                        return True
                    else:
                        return parse_S(input_str)
                # if space instead of ;, string is partly OK, continue parsing
                elif input_str[curr_char_index] == ' ':
                    if len(input_str) == curr_char_index:
                        raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected ;, but encountered: ' '")
                    else:
                        print(f"Parser found symbol ' ' instead of ; at index {curr_char_index}, but continues to work")
                else:
                    raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected one of symbols {first_C}, but encountered: {input_str[curr_char_index]}")
            curr_char_index += 1
            return parse_S(input_str)
        else:
            raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected one of symbols {first_S}, but encountered: {input_str[curr_char_index]}")
    except IndexError:
        # catch empty symbol when it should not be one
        raise InvalidSymbolException(f"Error at index {curr_char_index}, unexpected string end")


def parse_W(input_str):
    global curr_char_index
    # check if next symbol belongs to W first set
    if input_str[curr_char_index] in first_W:
        # check if next symbol is (, then parse for w
        if input_str[curr_char_index] == '(':
            curr_char_index += 1
            # go into function w parsing
            res = parse_W(input_str)
            if not res:
                raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected one of symbols {first_W}, but encountered: {input_str[curr_char_index]}")
            elif input_str[curr_char_index] != ')':
                raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected symbol ')', but encountered: {input_str[curr_char_index]}")
            curr_char_index += 1
        else:
            # go into function C parsing for digit
            res = parse_C(input_str)
            if res is False:
                raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected one of symbols {first_C}, but encountered: {input_str[curr_char_index]}")
            # parse all following digits
            while res:
                curr_char_index += 1
                res = parse_C(input_str)
            # if encountered dot check for following digits in the decimal part
            if input_str[curr_char_index] == '.':
                curr_char_index += 1
                res = parse_C(input_str)
                if res is False:
                    raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected one of symbols {first_C}, but encountered: {input_str[curr_char_index]}")
                while res:
                    curr_char_index += 1
                    res = parse_C(input_str)         
        res = parse_O(input_str)
        if res == False:
            return True
        else:
            curr_char_index += 1
            return parse_W(input_str)
    else:
        return False

def parse_O(input_str):
    global curr_char_index
    if input_str[curr_char_index] in first_O:
        return True
    return False

def parse_C(input_str):
    global curr_char_index
    if input_str[curr_char_index] in first_C:
        return True
    return False

input_string = str(input("Enter symbols string: "))

if len(input_string) < 1:
    print("Empty string was given")
    exit(1)

try:
    if parse_S(input_string) == True:
        print("Entered string belongs to grammar")
except Exception as e:
    print(str(e))

