from __future__ import division
import numpy

# Just some random code that uses numpy:
def calculate_pi(n):
    points = numpy.random.uniform(0, 1, size=(n, 2))
    points_in_unit_circle = numpy.sqrt(points[:, 0] ** 2 + points[:, 1] ** 2) < 1
    point_count = sum(points_in_unit_circle).astype("double")

    return point_count / n * 4


if __name__ == "__main__":
    print("Hello!")
    print(f"I calculated {calculate_pi(10**6)} with numpy")
