import itertools

def evaluate_left_to_right(expression):
    tokens = []
    num = ""
    for char in expression:
        if char.isdigit():
            num += char
        else:
            if num:
                tokens.append(int(num))
                num = ""
            tokens.append(char)
    if num:
        tokens.append(int(num))

    result = tokens[0]
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        next_number = tokens[i + 1]
        if operator == "+":
            result += next_number
        elif operator == "*":
            result *= next_number
        elif operator == "-":
            result = result * (10**len(str(next_number))) + next_number
        i += 2

    return result

lists = [line.strip().split(":") for line in open(0)]
total = 0

for tests in lists:
    target = int(tests[0])
    nums = tests[1].strip()
    spaces = nums.count(" ")

    combinations = itertools.product("+*-", repeat=spaces)

    for combination in combinations:
        expression = nums
        for operator in combination:
            expression = expression.replace(" ", operator, 1)
            
        value = evaluate_left_to_right(expression)
        if value == target:
            total += target
            break

print(total)
