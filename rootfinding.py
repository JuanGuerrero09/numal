from typing import Callable


def bisection_method(a, b, func: Callable, obj, Nmax, e):
    xa = func(a)
    xb = func(b)

    count = 0
    solution_found = False

    def check_if_allows():
        if (xa * xb) < 0:
            return True
        else:
            return False

    if check_if_allows():
        while not solution_found and count < Nmax:
            half = (a + b) / 2
            xh = func(half)
            print(
                f"Current values \n f(a = {a}) = {
                    xa} \t f(half = {half}) = {xh}\t f(b = {b}){xb} "
            )
            if xh - obj > 0:
                b = half
            else:
                a = half
            xh = func(half)
            count = count + 1
            if abs(xh - obj) < e:
                solution_found = True
                print(f"Solution found in {Nmax} iterations")
                print(f"Solution: {xh}")
                return half
            xa = func(a)
            xb = func(b)
    else:
        print(f"No solution found in {Nmax} iterations")
        return 1
    return 0


def f(x):
    return pow(x, 3) + (2 * pow(x, 2)) - (3 * x) - 1


print(bisection_method(1, 2, f, 0, 15, 0.005))
