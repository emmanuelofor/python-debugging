import sys
import pdb; pdb.set_trace()

def area_of_rectangle(height, width=None):
    """
    Returns the area of a rectangle.
    """

    if width is None:
        width = height

    area = height * width

    return area

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        message = (
            "{script_name}: Expecting one or two command-line arguments:\n"
            "\tthe height of a square or the height and width of a "
            "rectangle".format(script_name=sys.argv[0]))
        sys.exit(message)

    height = float(sys.argv[1])
    width = height

    if len(sys.argv) > 2:
        width = float(sys.argv[2])

    area = area_of_rectangle(height, width)

    message = "The area of a {h} x {w} rectangle is {a}".format(
        h=height, w=width, a=area)
    print(message)


