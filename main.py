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
        drawer.draw_point(point['r'], point['i'])
        count += 1
        if count % 1000 == 0:
            print("{0} tys punktów".format(count/1000))

    drawer.refresh()
    drawer.wait()


def is_point_in_set(c):
    z = 0 + 0j
    for i in range(25):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True


def generate_points():
    points = []
    for x in range(-600, 300, 1):
        for y in range(-300, 300, 1):
            point = dict()
            c = complex(x/300, y/300)
            point['r'] = c.real
            point['i'] = c.imag
            if is_point_in_set(c):
                points.append(point)
    return points

if __name__ == "__main__":
    sys.exit(main())
