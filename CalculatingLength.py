print("Welcome to Line Comparision Computation Program")

"""
Calculating The Two Length of the Points (X,Y) co-ordinating using Cartesian System
"""


def calculating_length(x_first_point, x_second_point, y_first_point, y_second_point):
    length = ((((x_second_point - x_first_point) ** 2) + ((y_second_point - y_first_point) ** 2)) ** 0.5)
    print("length value:", length)


if __name__ == '__main__':
    x_first_point = int(input("enter x_point1 value"))
    x_second_point = int(input("enter x_point2 value"))
    y_first_point = int(input("enter y_point1 value"))
    y_second_point = int(input("enter y_point2 value"))
    calculating_length(x_first_point, x_second_point, y_first_point, y_second_point)
