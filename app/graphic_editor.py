# -*- coding: utf8 -*-

from prettytable import PrettyTable


class GraphicEditor(object):

    array = []
    COMMANDS = ["I", "C", "L", "V", "H", "K", "F", "S", "X"]
    out = {}

    def create_array(self, w, h):
        """
        create the array
        :param w:
        :param h:
        :return:
        """
        self.array = [[0 for i in range(int(w))] for c in range(int(h))]

        return self.array

    def size_array(self):
        """
        return size of width and height
        :param array:
        :return: w int, h int
        """
        h = int(self.array.__len__())
        w = int(self.array[0].__len__())

        return w, h

    def show_formatted_array(self, array=None):
        """
        Convert list in formatted table
        :return: formatted table
        """
        if not array:
            array = self.array

        table = PrettyTable()

        for line in array:
            table.add_row(line)

        return table

    def paints_coordinated(self, x, y, color):
        """
        Paints a coordinated with the color
        :param x:
        :param y:
        :param color:
        :return:
        """
        # casting to int
        x = int(x)
        y = int(y)

        # sample start with 1
        if x != 0:
            x = x - 1

        if y != 0:
            y = y - 1

        self.array[y][x] = color.upper()

        return self.array

    def clear_array(self):
        """
        Get current array and clean
        :return: array
        """
        w, h = self.size_array()
        self.array = []
        array = self.create_array(w, h)

        return array

    def named_array(self, name):
        """
        Create a name, clear the array and save another array to output
        :param name:
        :return:
        """
        self.out[name] = self.array
        array = self.clear_array()

        return array

    def drawing_vertical(self, x, y1, y2, color):
        """
        Drawing line vertical
        :param x:
        :param y1:
        :param y2:
        :param color:
        :return:
        """
        for idx, i in enumerate(self.array, start=1):
            if idx == int(x):
                for idx2, i2 in enumerate(i, start=1):
                    if int(y1) <= idx2 <= int(y2):
                        self.paints_coordinated(idx, idx2, color)

    def drawing_horizontal(self, x1, x2, y, color):
        """
        drawing line horizontal
        :param x1:
        :param x2:
        :param y:
        :param color:
        :return:
        """
        for idx, i in enumerate(self.array, start=1):
            if idx == int(y):
                for idx2, i2 in enumerate(i, start=1):
                    if int(x1) <= idx2 <= int(x2):
                        self.paints_coordinated(idx2, idx, color)

    def drawing_rectangle(self, x1, x2, y1, y2, color):
        """
        drawing rectangle
        :param x1:
        :param x2:
        :param y1:
        :param y2:
        :param color:
        :return:
        """
        for idx, i in enumerate(self.array, start=1):
            if int(x2) <= idx <= int(y2):
                for idx2, i2 in enumerate(i, start=1):
                    if int(x1) <= idx2 <= int(y1):
                        self.paints_coordinated(idx2, idx, color)

    def drawing_area(self, x, y, color):
        x = int(x) - 1
        y = int(y) - 1
        color = color.upper()

        new_array = GraphicEditor.flood_fill(self.array, x, y, color)

        self.array = new_array

        return self.array

    @staticmethod
    def flood_fill(array, x, y, color, old_color=None):
        width = len(array[0]) - 1
        height = len(array) - 1

        if old_color == None:
            old_color = array[x][y]

        if array[x][y] != old_color:
            # Base case. If the current x, y character is not the old_color,
            # then do nothing.
            return

        # Change the character at array[x][y] to color
        array[x][y] = color

        # Recursive calls. Make a recursive call as long as we are not on the
        # boundary (which would cause an Index Error.)
        if y > 0:  # left
            GraphicEditor.flood_fill(array, x, y - 1, color, old_color)

        if x > 0:  # up
            GraphicEditor.flood_fill(array, x - 1, y, color, old_color)

        if y < width:  # right
            GraphicEditor.flood_fill(array, x, y + 1, color, old_color)

        if x < height:  # down
            GraphicEditor.flood_fill(array, x + 1, y, color, old_color)

        return array


def main():
    """
    start the app
    :return:
    """
    table = GraphicEditor()

    while True:
        choice = input("Insert the command > ")

        commands = choice.split(' ')
        command = commands[0]

        if not command.upper() in GraphicEditor.COMMANDS:
            continue

        elif command.upper() == 'I' and commands.__len__() == 3:
            table.create_array(commands[1], commands[2])

        elif command.upper() == 'C' and commands.__len__() == 1:
            table.clear_array()

        elif command.upper() == 'L' and commands.__len__() == 4:
            table.paints_coordinated(commands[1], commands[2], commands[3])

        elif command.upper() == 'V' and commands.__len__() == 5:
            table.drawing_vertical(commands[1], commands[2], commands[3], commands[4])

        elif command.upper() == 'H' and commands.__len__() == 5:
            table.drawing_horizontal(commands[1], commands[2], commands[3], commands[4])

        elif command.upper() == 'K' and commands.__len__() == 6:
            table.drawing_rectangle(commands[1], commands[2], commands[3], commands[4], commands[5])

        elif command.upper() == 'F' and commands.__len__() == 4:
            table.drawing_area(commands[1], commands[2], commands[3])

        elif command.upper() == 'S' and commands.__len__() == 2:
            table.named_array(commands[1])

        elif command.upper() == 'X' and commands.__len__() == 1:
            for name, data in table.out.items():
                print(name)
                print(table.show_formatted_array(data))

            print("Bye Bye see you soon!")
            break

if __name__ == '__main__':
    main()
