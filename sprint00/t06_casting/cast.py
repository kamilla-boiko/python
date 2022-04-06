a = 3
b = 10
c = -14.8
d = True
print(f"""Available variables:
a = {a}
b = {b}
c = {c}
d = {d}
""")
print("Result:")
print(f"{a} + {b} =", float(a) + float(b))
print(f"{c} - {b} =", int(c) - int(b))
print(f"{c} + {b} =", str(c) + str(b))
print(f"{a} - {a} =", bool(a - a))