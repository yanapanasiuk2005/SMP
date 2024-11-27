# Classes/Test.py

import sys, math

from Data.Lab5.Constants.constants import COLOR_CODES

# Чому варто використовувати шаблон заводського методу?
#
#     Розширюваність: Якщо ми захочемо додати більше фігур (наприклад, сфер, пірамід) пізніше, ми можемо легко розширити програму, додавши нові класи фігур без зміни основної логіки.
#     Розділення завдань: Відокремлює код, який генерує 3D-фігури, від коду, який виконує взаємодію з користувачем та рендеринг, що робить програму більш модульною та зручною для підтримки.
#     Гнучкість: Користувачі можуть легко додавати нові типи фігур і налаштовувати їхню поведінку, зберігаючи при цьому послідовний інтерфейс.

class Shape:
    """Abstract class representing a 3D shape."""

    def __init__(self, w=80, h=24, scale=1.0, shift=(0, 0, 0), color='white'):
        self.w, self.h = w, h
        self.out = sys.stdout
        self.scale_factor = scale
        self.shift = shift
        self.color = COLOR_CODES.get(color, COLOR_CODES['white'])
        self.angle_x, self.angle_y, self.angle_z = 0.0, 0.0, 0.0

    def rotate(self):
        raise NotImplementedError

    def project(self):
        raise NotImplementedError

    def draw(self, to_file=False):
        raise NotImplementedError

    def set_rotation_angle(self, angle, axis):
        radians = math.radians(angle)
        if axis == 'x':
            self.angle_x = radians
        elif axis == 'y':
            self.angle_y = radians
        elif axis == 'z':
            self.angle_z = radians

    def set_color(self, color):
        self.color = COLOR_CODES.get(color, COLOR_CODES['white'])

    def set_scale(self, scale):
        try:
            self.scale_factor = float(scale)
        except ValueError:
            print("Invalid scale input! Using default scale.")

    def save_to_file(self, filename, ascii_art):
        try:
            with open(filename, 'w') as file:
                file.write(ascii_art)
            print(f"ASCII art saved to {filename}")
        except IOError as e:
            print(f"Error saving to file: {e}")


class Cube(Shape):
    def __init__(self, w=80, h=24, scale=1.0, shift=(0, 0, 0), color='white'):
        super().__init__(w, h, scale, shift, color)
        self.cube = [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]
        self.edges = [
            (0, 1), (1, 3), (3, 2), (2, 0), (4, 5), (5, 7), (7, 6), (6, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        self.ym = h / 3
        self.xm = 2 * self.ym

    def rotate(self):
        # Rotating cube vertices based on set angles
        self.cube = [(x, y * math.cos(self.angle_x) - z * math.sin(self.angle_x),
                      y * math.sin(self.angle_x) + z * math.cos(self.angle_x)) for x, y, z in self.cube]
        self.cube = [(x * math.cos(self.angle_y) + z * math.sin(self.angle_y), y,
                      -x * math.sin(self.angle_y) + z * math.cos(self.angle_y)) for x, y, z in self.cube]
        self.cube = [(x * math.cos(self.angle_z) - y * math.sin(self.angle_z),
                      x * math.sin(self.angle_z) + y * math.cos(self.angle_z), z) for x, y, z in self.cube]

    def project(self):
        # Projecting cube vertices onto 2D screen
        return [(round(self.w / 2 + self.xm * (x * self.scale_factor + self.shift[0]) / (z + 2 + self.shift[2])),
                 round(self.h / 2 + self.ym * (y * self.scale_factor + self.shift[1]) / (z + 2 + self.shift[2])))
                for x, y, z in self.cube]

    def draw(self, to_file=False):
        proj = self.project()
        # Adding lines (edges) between vertices
        for edge in self.edges:
            start, end = proj[edge[0]], proj[edge[1]]
            for i in range(1, 9):
                x = start[0] + i * (end[0] - start[0]) // 10
                y = start[1] + i * (end[1] - start[1]) // 10
                proj.append((x, y))

        # Constructing ASCII art
        art = '\n'.join(''.join(('*' if (x, y) in proj else ' ') for x in range(self.w)) for y in range(self.h))

        # Return ASCII art as string if saving to file
        if to_file:
            return art
        else:
            # Print to console with color
            self.out.write(self.color + '\033[H' + art + COLOR_CODES['reset'])
