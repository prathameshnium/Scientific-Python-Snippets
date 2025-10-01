# Unit Prefix converter (mini-program)

prefixes = {
    'T': 10**12,   # tera
    'G': 10**9,    # giga
    'M': 10**6,    # mega
    'k': 10**3,    # kilo
    'h': 10**2,    # hecto
    'da': 10**1,   # deca
    'none': 10**0, # none
    'd': 10**(-1), # deci
    'c': 10**(-2), # centi
    'm': 10**(-3), # milli
    'micro': 10**(-6), # micro (μ)
    'n': 10**(-9), # nano
    'p': 10**(-12) # pico
}


#prefixes['T'] will give you its value


# Take user input (eg: 10,k,T)
print('write input as "number,from_prefix,to_prefix"' )
user_input = input("Enter values separated by commas: ")

# Split the input string by commas
values = user_input.split(',')

# Remove any leading or trailing whitespace from each value
values = [value.strip() for value in values]

# does find the Coefficient in new unt   
converted = eval(values[0]) * float(prefixes[values[1]]) / float(prefixes[values[2]])
#output
print(f"The {values[0]} {values[1]} is : {converted:.2e} {values[2]}")
