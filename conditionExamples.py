is_hot = False
is_cold = False

if is_hot:
    print("It is a hot day.")
elif is_cold:
    print("It is cold day.")
else:
    print("It is lovely day.")
print("Enjoy your day")

has_high_income = True
has_good_credit = True
has_criminal_records = False

if has_good_credit and has_high_income:
    print("eligible for loan. with and")

if has_good_credit or has_high_income:
    print("eligible for loan. also With Or")

if has_high_income and has_good_credit and not has_criminal_records:
    print("eligible for loan. with Not criminal record")

temperature = 8

if temperature > 29:
    print("It is a hot day.")
elif 30 > temperature > 10:
    print("It is a normal day")
else:
    print("it is cold day")


