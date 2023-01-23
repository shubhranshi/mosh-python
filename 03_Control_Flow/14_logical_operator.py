# AND, OR, NOT - logical operators

has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("eligible for E loan")

if has_high_income or has_good_credit:
    print("eligible for D loan")

if has_good_credit and not has_criminal_record:
    print("eligible for loan")

if (has_good_credit or has_high_income) and not has_criminal_record:
    print("eligible for loan")

# boolean operators are short circuit which means that the evaluation of condition starts
# from left to right.
# In case of AND - as soon as it hits a false condition, it will not evaluate the rest
# of the condition. This is short-circuit evaluation.
# In case of OR - as soon as it hits a true condition, it will not evaluate the rest
# of the condition.