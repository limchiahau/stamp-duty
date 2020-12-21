from math import ceil
import sys

# given the tenancy period in months and the monthly rental
# this function will return the stamp duty as a float.
def stamp_duty(tenancy_period_in_months, monthly_rental):
    tax_exemption = 2400
    block_size = 250
    tax_rate = calculate_tax_rate(tenancy_period_in_months / 12)
        
    return ceil((12 * monthly_rental - tax_exemption) 
                / block_size) * tax_rate

# given a float named years
# this function will return the applicable tax rate
# for the tenancy agreement.
def calculate_tax_rate(years):
    if years <= 1:
        return 1
    elif years <= 3:
        return 2
    else:
        return 3


def stamp_duty_in_years(monthly_rental, tenancy_period_in_years=2):
    '''
    given the tenancy period in months and the monthly rental
    this function will return the stamp duty as a float.
    '''
    return stamp_duty(tenancy_period_in_years * 12, monthly_rental)


def rm_str(amount):
	return f'RM{amount}'

def print_result(stamp_duty):
	#stamp duty
	print(f'Stamp Duty	: {rm_str(stamp_duty)}')

	#amount for copy
	print(f'Copy Amount	: {rm_str(10)}')

	#total amount
	print(f'Total		: {rm_str(stamp_duty + 10)}')


# MAIN
rental, tenure = [int(x) for x in sys.argv[1:]]
stamp_duty = stamp_duty_in_years(rental, tenure)
print_result(stamp_duty)

