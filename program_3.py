# Author: Andrew Bittner
# Date: 10/10/2024

# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

def exit_sequence():
    # Function to keep console/window open until user ends program
    input('\nPress any key to exit... ')

def validate_inp_type(inp, out_type, err_msg, inp_msg):
    # Check whether input type  matches desired output type
    while type(inp) != out_type:
        try:
            inp = out_type(inp)
        except:
            print(err_msg, end = '')
            inp = input(inp_msg)
    return inp

def get_income_tax(income, tax_rates_list):
    tax_total = 0.0
    tax_list = []
    for tax_rate in tax_rates_list:
        tax_total += float(income) * tax_rate
        tax_list.append(float(income) * tax_rate)
    return tax_total, tax_list

def main():
    TAX_RATES_LIST = [0.05, 0.025]
    TAX_TYPES_LIST = ['state', 'county']
    income = input('Enter monthly dollar income, in numerical form (no signs): ')
    income = validate_inp_type(income, float, 'Invalid input entered (was it formatted correctly?). ', 'Please re-enter your monthly income: ')
    tax_total, tax_list = get_income_tax(income, TAX_RATES_LIST)
    for tax_num in range(len(TAX_RATES_LIST)):
        print(f'Your monthly {TAX_TYPES_LIST[tax_num]} tax is $ {tax_list[tax_num]:.2f}', end = '.\n')
    print(f'Your total monthly tax is {tax_total:.2f}', end = '.\n')
    exit_sequence()
main()