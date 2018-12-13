def pythagorean(a,b):
    c_2 = a**2 + b**2
    c = c_2**.5
    print(f"Side C: {c}")

a = int(input("Side A: "))
b = int(input("Side B: "))
pythagorean(a,b)