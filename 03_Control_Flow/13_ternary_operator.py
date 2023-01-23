age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)

# There is a different cleaner way to write the same code, and achieve the same result.
# shorter way to write the above code using ternary operator
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
