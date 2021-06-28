
# Function to calculate membership fee
def calculate_memebership_fee(rent_amount, rent_period, Organisation_unit):
    rent_amount = rent_amount/100

    # Check rent period and check if value is in range
    if rent_period == "week":
        if rent_amount < 25 or rent_amount > 2000:
            raise ValueError("Rent amount outside acceptable range")

    elif rent_period == "month":
        if (rent_amount < 110 or rent_amount > 8660):
            raise ValueError("Rent amount outside acceptable range")

    else:
        raise ValueError("Invalid value as 'rent period'")

    # Convert rent to weekly
    if rent_period == "month":
        rent_amount = rent_amount / 4

    # Calculate fee as rent amount plus 20% VAT (120% of rent amount or 1.2*rent amount)
    # Use 120 as minimum possible rent amount
    if rent_amount < 120:
        fee = 1.2 * 120
    else:
        fee = 1.2 * rent_amount

    # Find config from find_config function
    config_obj = find_config(Organisation_unit)

    # If config has membership fee, replace calculated fee with value
    if config_obj[0]:
        fee = config_obj[1]

    return fee


# Function assumes that client must always have a config object
# Recursively find config if not in current organisation unit
def find_config(Organisation_unit):
    if not Organisation_unit.config:
        return find_config(Organisation_unit.parent)
    else:
        return (Organisation_unit.config.has_fixed_memebership_fee, Organisation_unit.config.fixed_memebership_amount)