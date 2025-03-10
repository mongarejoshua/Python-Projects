# arithmetic formatter program
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

first_line = []
second_line = []
dashes = []
result = []

for i in problems:
    parts = i.split()

    num1, op, num2 = parts

    width = max(len(num1), len(num2)) + 2
    first_line.append(num1.rjust(width))
    second_line.append(op + " " + num2.rjust(width - 2))
    dashes.append('-' * width)

    arranged_problems = "\n".join([
        "    ".join(first_line),
        "    ".join(second_line),
        "    ".join(dashes),
    ])

    print(arranged_problems)
