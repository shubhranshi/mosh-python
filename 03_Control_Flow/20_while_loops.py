# while continues iterating until the condition is true
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")

## example 2
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# while can go in infinite loop if the breaking condition is not met
while True:
    command = input(">")
    print("Echo", command)
    if command.lower() == "quit":
        break