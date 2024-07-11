def decimal_to_hexadecimal(decimal_number):
    if decimal_number == 0:
        return '0'

    hexadecimal_digits = ''
    while decimal_number > 0:
        remainder = decimal_number % 16
        if remainder < 10:
            hexadecimal_digits = str(remainder) + hexadecimal_digits
        else:
            hexadecimal_digits = chr(ord('A') + remainder - 10) + hexadecimal_digits
        decimal_number //= 16

    return hexadecimal_digits

def decimal_to_octal(decimal_number):
    if decimal_number == 0:
        return '0'

    octal_digits = ''
    while decimal_number > 0:
        remainder = decimal_number % 8
        octal_digits = str(remainder) + octal_digits
        decimal_number //= 8

    return octal_digits

def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return '0'
    
    binary_digits = ''
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_digits = str(remainder) + binary_digits
        decimal_number //= 2
    
    return binary_digits

def print_formatted(number):
    for i in range(1, number + 1):
        width = len("{0:b}".format(number))
        print("{i:{width}d} {decimal_to_octal(i):{width}s} {decimal_to_hexadecimal(i):{width}s} {decimal_to_binary(i):{width}s}")
def print_formatted2(number):
    # your code goes here
    for i in range(1,number+1):
        l=len("{0:b}".format(i))
        print("{0:{w}d} {0:{w}o} {0:{w}x} {0:{w}b}".format(i,w=l))
