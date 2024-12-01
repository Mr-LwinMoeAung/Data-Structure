def alternate_length(s, symbol="*"):
    if s == "":
        return ""
    
    next_symbol = "~" if symbol == "*" else "*"
    return s[0] + symbol + alternate_length(s[1:], next_symbol)

input_string = input('Enter Input : ')
alternate_string = alternate_length(input_string)
string_length = alternate_string.count("*") + alternate_string.count("~")

print(alternate_string)
print(f"Length of '{input_string}' = {string_length}")