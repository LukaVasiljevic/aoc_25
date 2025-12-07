homework = []
with open("in.txt") as f:
    for line in f.readlines():
        homework.append(line.strip("\n").split(" "))

    hw = []
    for i in range(len(homework) - 1):
        result = [
            ("" if n == "" else int(ch))
            for n in homework[i]
            for ch in ([""] if n == "" else list(n))
        ]
        hw.append(result)
    hw.append(homework[-1])

    for i in range(len(hw)):
        print(hw[i])

    n = len(hw)
    m = len(hw[0])

    operators = []
    grand_total = 0

    for j in range(m - 1, -1, -1):
        num = ""
        local_total = 1
        for i in range(n):
            if hw[i][j] in ["+", "*"]:
                operators.append(int(num))
                if hw[i][j] == "+":
                    grand_total += sum(operators)
                else:
                    local_total = 1
                    for o in operators:
                        local_total *= o
                    grand_total += local_total
                operators = []
            else:
                num += str(hw[i][j])
        if hw[i][j] not in ["+", "*"]:
            operators.append(int(num))

print(grand_total)
