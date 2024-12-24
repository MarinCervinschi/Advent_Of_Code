import re
if __name__ == "__main__":

    with open("puzzle.txt") as f:
        operations = []
        wires = {}
        highest_z = "z00"
        for row in f:
            match = re.match(r'(\w+): (\d+)', row.strip())
            if match:
                key, value = match.groups()
                wires[key] = int(value)
            else:
                pattern = re.compile(r'(\w+)\s+(AND|XOR|OR)\s+(\w+)\s+->\s+(\w+)')
                match = pattern.match(row.strip())
                if match:
                    operand1, operation, operand2, result = match.groups()
                    operations.append((operand1, operation, operand2, result))

                    if result.startswith('z') and int(result[1:]) > int(highest_z[1:]) :
                        highest_z = result

        def part_1(wires):
            while True:
                if all(res in wires.keys() for _, _,_, res in operations):
                    break
                
                for op1, op, op2, res in operations:
                    if op1 not in wires or op2 not in wires:
                        continue

                    if op == 'AND':
                        wires[res] = wires[op1] and wires[op2]
                    elif op == 'XOR':
                        wires[res] = wires[op1] ^ wires[op2]
                    elif op == 'OR':
                        wires[res] = wires[op1] or wires[op2]


            wires = dict(sorted(wires.items()))
            decimal = ''
            for k, v in wires.items():
                if k.startswith('z'):
                    decimal += str(v)

            decimal_value = int(decimal[::-1], 2)
            print(f"Decimal value: {decimal_value}")

        def part_2():
            wrong = set()
            for op1, op, op2, res in operations:
                if res.startswith('z') and op != "XOR" and res != highest_z:
                    wrong.add(res)
                if (
                    op == "XOR"
                    and res[0] not in ["x", "y", "z"]
                    and op1[0] not in ["x", "y", "z"]
                    and op2[0] not in ["x", "y", "z"]
                ):
                    wrong.add(res)
                if op == "AND" and "x00" not in [op1, op2]:
                    for subop1, subop, subop2, _ in operations:
                        if (res == subop1 or res == subop2) and subop != "OR":
                            wrong.add(res)
                if op == "XOR":
                    for subop1, subop, subop2, _ in operations:
                        if (res == subop1 or res == subop2) and subop == "OR":
                            wrong.add(res)


            print(",".join(sorted(wrong)))

        part_1(wires)
        part_2()


            


        
        
       