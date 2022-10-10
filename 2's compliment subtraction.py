# Program for using 2's compliment subtraction
import textwrap
from textwrap import wrap


def conv_binary(num, bas):
    if "-" in num:
        num = num.replace("-", "")
    if "+" in num:
        num = num.replace("+", "")
    quo = []
    rem = []
    org = num
    if bas == 10:
        num = str(num).split(".")
        while int(num[0]) != 0:
            quo.append(str(int(num[0]) % 2))
            num[0] = int(num[0]) // 2
        if len(num) == 2:
            jk = 0
            dec = int(num[1]) / pow(10, len(num[1]))
            while dec != 0 and jk <= 7:
                dec = dec * 2
                dec = str(dec).split(".")
                rem.append(str(dec[0]))
                dec = int(dec[1]) / pow(10, len(dec[1]))
                jk += 1
        org = org.split(".")
        if len(org) == 1:
            return ' '.join(textwrap.wrap(''.join(quo[::-1]).rjust(8, "0"), 4))
        else:
            return ''.join(quo[::-1]) + '.' + ''.join(rem)

    elif bas == 8:
        octal = {0: '000', 1: '001', 2: '010', 3: '011', 4: '100', 5: '101', 6: '110', 7: '111'}
        num = num.split(".")
        for i in num[0]:
            quo.append(octal[int(i)])
        if len(num) == 2:
            for j in num[1]:
                quo.append(octal[int(j)])
        return ' '.join(textwrap.wrap(''.join(quo).rjust(8, "0"), 4))

    elif bas == 16:
        hexa = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000',
                '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
        num = num.split(".")
        for i in num[0]:
            quo.append(hexa[str(i)])
        if len(num) == 2:
            for j in num[1]:
                quo.append(hexa[str(j)])
        return ' '.join(quo)


def getComp(num, bin):
    detect = False
    st = ""
    bina = list(bin)
    for i in list(reversed(bina[1:9])):
        if detect:
            if i == "1":
                st += "0"
            elif i == "0":
                st += "1"
        else:
            if i == "1":
                st += "1"
                detect = True
            elif i == "0":
                st += "0"
    return ' '.join(textwrap.wrap("1" + ''.join(list(reversed(st))), 4))


def add_bin(bt1, bt2):
    bt1 = list(reversed(bt1))
    bt2 = list(reversed(bt2))
    add = ""
    carry = False
    for i in zip(bt1, bt2):
        if carry is False:
            if i[0] == "0":
                if i[1] == "0":
                    add += "0"
                elif i[1] == "1":
                    add += "1"
            elif i[0] == "1":
                if i[1] == "1":
                    add += "0"
                    carry = True
                elif i[1] == "0":
                    add += "1"
        elif carry:
            if i[0] == "0":
                if i[1] == "0":
                    add += "1"
                    carry = False
                elif i[1] == "1":
                    add += "0"
                    carry = True
            elif i[0] == "1":
                if i[1] == "1":
                    add += "1"
                    carry = True
                elif i[1] == "0":
                    add += "0"
                    carry = True
    if carry:
        add += "1"
    return add[::-1]


def pos(add, bass):
    add = add.removeprefix("1")
    if add.startswith("1"):
        print(f"\nCarry is generated. Discarding carry we get,\n    {add}")
        print("Since magnitude is 1, the answer is negative and in 2's Compliment,")
        neg(add, base)
    else:
        print(
            "\nCarry is generated. Discarding carry we get,\n" + "  + " + ' '.join(textwrap.wrap(add.removeprefix('1'), 4)))
        if bass == 10:
            print(f"Since it is in decimal,")
            tot1 = 0
            x = 0
            for i in list(reversed(add)):
                tot1 += int(i)*(2**x)
                x += 1
            print(f"\n*****The final answer is {tot1} to base 10.*****")
        elif bass == 8:
            octal = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}
            print("For Octal conversion, grouping into 3, we get,")
            add = textwrap.wrap(add.rjust(((len(add) // 3) + 1) * 3, "0"), 3)
            print("    " + ' '.join(add))
            final_ans = ""
            for i in add:
                final_ans += octal[i]
            print(f"\n*****The final answer is ({final_ans}) to base 8.*****")
        elif bass == 16:
            hexa = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                    '1000': '8',
                    '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
            print("For Hexadecimal conversion, grouping into 4, we get,")
            add = textwrap.wrap(add, 4)
            print("    " + ' '.join(add))
            final_ans = ""
            for i in add:
                final_ans += hexa[i]
            print(f"\n*****The final answer is ({final_ans}) to base 16.*****")


def neg(add, bass):
    detect = False
    st = ""
    add = list(add)
    for i in list(reversed(add[0:8])):
        if detect:
            if i == "1":
                st += "0"
            elif i == "0":
                st += "1"
        else:
            if i == "1":
                st += "1"
                detect = True
            elif i == "0":
                st += "0"
    add = ''.join(list(reversed(st)))
    print("    " + add)
    if bass == 10:
        print(f"\nSince it is in decimal,")
        tot1 = 0
        x = 0
        for i in list(reversed(add)):
            tot1 += int(i) * (2 ** x)
            x += 1
        print(f"*****The final answer is -{tot1} to base 10.*****")
    elif bass == 8:
        octal = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}
        print("For Octal conversion, grouping into 3, we get,")
        add = textwrap.wrap(add.rjust(((len(add) // 3) + 1) * 3, "0"), 3)
        print("    " + ' '.join(add))
        final_ans = ""
        for i in add:
            final_ans += octal[i]
        print(f"\n*****The final answer is -({final_ans}) to base 8.******")
    elif bass == 16:
        hexa = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                '1000': '8',
                '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
        print("For Hexadecimal conversion, grouping into 4, we get,")
        add = textwrap.wrap(add, 4)
        print("    " + ' '.join(add))
        final_ans = ""
        for i in add:
            final_ans += hexa[i]
        print(f"\n*****The final answer is -({final_ans}) to base 16.*****")


def only_add(t1, t2, bass):
    print("\nNow for the addition part,")
    add = add_bin(t1, t2)
    print(' '.join(textwrap.wrap(''.join(t1), 1)).rjust(20, " "))
    print(' '.join(textwrap.wrap("+ " + ''.join(t2), 1)).rjust(20, " "))
    print(("-" * 17).rjust(20, " "))
    print(' '.join(textwrap.wrap(add, 1)).rjust(20, " "))
    if bass == 10:
        print(f"Since it is in decimal,")
        tot1 = 0
        x = 0
        for i in list(reversed(add)):
            tot1 += int(i)*(2**x)
            x += 1
        print(f"\n*****The final answer is {tot1} to base 10.*****")
    elif bass == 8:
        octal = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}
        print("For Octal conversion, grouping into 3, we get,")
        add = textwrap.wrap(add.rjust(((len(add) // 3) + 1) * 3, "0"), 3)
        print("    " + ' '.join(add))
        final_ans = ""
        for i in add:
            final_ans += octal[i]
        print(f"\n*****The final answer is ({final_ans}) to base 8.*****")
    elif bass == 16:
        hexa = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                '1000': '8',
                '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
        print("For Hexadecimal conversion, grouping into 4, we get,")
        add = textwrap.wrap(add.rjust(((len(add) // 4) + 1) * 4, "0"), 4)
        print("    " + ' '.join(add))
        final_ans = ""
        for i in add:
            final_ans += hexa[i]
        print(f"\n*****The final answer is ({final_ans}) to base 16.*****")


print("Enter the expression!")
n = list(map(str, input().split(" ")))
og = n
print("Enter the base of both the numbers!")
base = int(input())
print("\n" + "*" * 20 + "SOLUTION" + "*" * 20)
print(f"\nFor first number {n[0]} we get,")
bt1 = conv_binary(n[0], base)
print(n[0].rjust(4, " ") + ": " + bt1 + " " * 4 + "<---8bit")
print(f"\nFor second number {n[1]} we get,")
bt2 = conv_binary(n[1], base)
print(n[1].rjust(4, " ") + ": " + bt2 + " " * 4 + "<---8bit")
if "-" not in og[0] and "-" not in og[1]:
    only_add(bt1, bt2, base)
else:
    print("\nGetting 2's Compliments for Negative Numbers")
    if "-" in og[0]:
        bt1 = getComp(og[0], bt1)
        print(og[0].rjust(4, " ") + ": " + bt1 + " " * 4 + "<---2's Compliment MS-bit")
    if "-" in og[1]:
        bt2 = getComp(og[1], bt2)
        print(og[1].rjust(4, " ") + ": " + bt2 + " " * 4 + "<---2's Compliment MS-bit")
    print("\nNow for the addition part,")
    bt1 = bt1.replace(" ", "")
    bt2 = bt2.replace(" ", "")
    print(' '.join(textwrap.wrap(''.join(bt1), 1)).rjust(20, " "))
    print(' '.join(textwrap.wrap("+ " + ''.join(bt2), 1)).rjust(20, " "))
    print(("-" * 17).rjust(20, " "))
    suma = add_bin(bt1, bt2)
    print(' '.join(textwrap.wrap(suma, 1)).rjust(20, " "))
    if len(suma) == 9:
        pos(suma, base)
    elif len(suma) == 8:
        print("\nCarry is not generated. Answer is negative and in 2's Compliment,\n" + "    " + ' '.join(
            textwrap.wrap(suma, 4)))
        print("Converting the number in original form,")
        neg(suma, base)
