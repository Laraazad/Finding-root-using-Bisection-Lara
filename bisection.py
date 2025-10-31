def f(x):
    return x**2 - 7

a = 2
b = 3

if f(a) * f(b) > 0:
    print("Invalid interval: f(a) and f(b) must have opposite signs.")
else:
    print(f"{'Iter':<5}{'a':<10}{'b':<10}{'p':<10}{'f(p)':<10}")
    print("-" * 45)
    iteration = 1

    while abs(b - a) > 1e-4:
        p = (a + b) / 2
        print(f"{iteration:<5}{a:<10.6f}{b:<10.6f}{p:<10.6f}{f(p):<10.6f}")
        
        if f(a) * f(p) < 0:
            b = p
        else:
            a = p
        iteration += 1

    print("\nApproximate root:", round(p, 6))