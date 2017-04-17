import sys
from drawer import Drawer

WIDTH = 1024
HEIGHT = 768


def main():
    points = generate_points()

    drawer = Drawer(WIDTH, HEIGHT, b"Mandelbrot")
    drawer.init_screen()

    count = 0
    for point in points:
        drawer.draw_point(point['r'], point['i'], point['color'], point['color'], point['color'])
        count += 1
        if count % 1000 == 0:
            print("{0} tys punktów".format(count/1000))

    drawer.refresh()
    drawer.wait()


def get_score_for_point(point):
    threshold = 25
    z = 0 + 0j
    for i in range(threshold):
        z = z**2 + point
        if abs(z) > 2:
            return i
    return threshold


def generate_points():
    x1 = -2
    x2 = 2
    y1 = -1.2
    y2 = 1.2
    precision = 300
    color_step = 10

    points = []
    for x in range(int(x1*precision), int(x2*precision), 1):
        for y in range(int(y1*precision), int(y2*precision), 1):
            point = dict()
            c = complex(x/precision, y/precision)
            point['r'] = c.real
            point['i'] = c.imag
            score = get_score_for_point(c)
            if score > 0:
                point['color'] = score * color_step
                points.append(point)

    return points

if __name__ == "__main__":
    sys.exit(main())
