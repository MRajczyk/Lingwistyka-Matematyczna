class InvalidSymbolException(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

first_S = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
first_W = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
first_O = ['+', '-', '*', '/', '^']
first_C = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
curr_char_index = 0

def parse_S(input_str):
    global curr_char_index
    try:
        if input_str[curr_char_index] in first_S:
            if input_str[curr_char_index] == '(':
                curr_char_index += 1
                res = parse_W(input_str)
                if not res or input_str[curr_char_index] != ')':
                    raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected symbol ')', but encountered: {input_str[curr_char_index]}")
                curr_char_index += 1
            else:
                res = parse_C(input_str)
                if res is False:
                    raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected one of symbols {first_C}, but encountered: {input_str[curr_char_index]}")
                while res:
                    curr_char_index += 1
                    res = parse_C(input_str)
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
                if input_str[curr_char_index] == ';':
                    curr_char_index += 1
                    # tu mozna ogarnac poprawe jakichs bledow typu spacja ig
                    if len(input_str) == curr_char_index:
                        return True
                    else:
                        return parse_S(input_str)
            curr_char_index += 1
            return parse_S(input_str)
        else:
            return False
    except IndexError:
        raise InvalidSymbolException(f"Error at index {curr_char_index}, unexpected string end")


def parse_W(input_str):
    global curr_char_index
    if input_str[curr_char_index] in first_W:
        if input_str[curr_char_index] == '(':
            curr_char_index += 1
            res = parse_W(input_str)
            if not res or input_str[curr_char_index] != ')':
                raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected symbol ')', but encountered: {input_str[curr_char_index]}")
            curr_char_index += 1
        else:
            res = parse_C(input_str)
            if res is False:
                raise InvalidSymbolException(f"Error at index {curr_char_index}, parser expected one of symbols {first_C}, but encountered: {input_str[curr_char_index]}")
            while res:
                curr_char_index += 1
                res = parse_C(input_str)
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
    return

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
        print("Entered strings belongs to grammar")
except Exception as e:
    print(str(e))

