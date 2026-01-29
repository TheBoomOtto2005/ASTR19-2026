
import numpy as np
import math

def main():

    def sin_x(x):

        return math.sin(x)

    def cos_x(x):

        return math.cos(x)

    the_values = np.linspace(0, 2, 1000)

    sin_value = [sin_x(x) for x in the_values]
    cos_value = [cos_x(x) for x in the_values]

    print(f"{'x':>10} {'sin(x)':>10} {'cos(x)':>10}")
    print("-" * 34)

    for i in range(len(the_values)):
        print(f"{the_values[i]:10.4f} {sin_value[i]:10.4f} {cos_value[i]:10.4f}")

if __name__ == "__main__":
    main()



