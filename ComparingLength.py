"""
Calculating The Length of Point(X,Y) of the Two Lines
Compare The Two Lines Using The Equals Method
equal Methods write the value equal or not
"""


def calculating_length(x_point1, x_point2, y_point1,
                       y_point2, x_point3, x_point4, y_point3, y_point4):
    line_1_length = ((((x_point2 - x_point1) ** 2) + ((y_point2 - y_point1) ** 2)) ** 0.5)
    line_2_length = ((((x_point4 - x_point3) ** 2) + ((y_point4 - y_point3) ** 2)) ** 0.5)
    print("1st line value:", line_1_length, "\n",
          "2nd line value", line_2_length)
    if line_1_length == line_2_length:
        print("equal")
    else:
        print("not equal")


if __name__ == '__main__':
    x_point1 = int(input("enter x_point1 value"))
    x_point2 = int(input("enter x_point2 value"))
    y_point1 = int(input("enter y_point1 value"))
    y_point2 = int(input("enter y_point2 value"))
    x_point3 = int(input("enter x_point3 value"))
    x_point4 = int(input("enter x_point4 value"))
    y_point3 = int(input("enter y_point3 value"))
    y_point4 = int(input("enter y_point4 value"))

    calculating_length(x_point1, x_point2, y_point1,
                       y_point2, x_point3, x_point4, y_point3, y_point4)
