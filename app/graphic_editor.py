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
        self.out[name] = self.array
        array = self.clear_array()

        return array

    def drawing_vertical(self, x, y1, y2, color):
        for idx, i in enumerate(self.array):
            if idx == int(x):
                for idx2, i2 in enumerate(i):
                    if int(y1) <= idx2 <= int(y2):
                        self.paints_coordinated(idx, idx2, color)

    def drawing_horizontal(self, x1, x2, y, color):
        for idx, i in enumerate(self.array):
            if idx == int(y):
                for idx2, i2 in enumerate(i):
                    if int(x1) <= idx2 <= int(x2):
                        self.paints_coordinated(idx2, idx, color)


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
            print(table.show_formatted_array())

        elif command.upper() == 'C' and commands.__len__() == 1:
            table.clear_array()
            print(table.show_formatted_array())

        elif command.upper() == 'L' and commands.__len__() == 4:
            table.paints_coordinated(commands[1], commands[2], commands[3])
            print(table.show_formatted_array())

        elif command.upper() == 'V' and commands.__len__() == 5:
            table.drawing_vertical(commands[1], commands[2], commands[3], commands[4])
            print(table.show_formatted_array())

        elif command.upper() == 'H' and commands.__len__() == 5:
            table.drawing_horizontal(commands[1], commands[2], commands[3], commands[4])
            print(table.show_formatted_array())

        elif command.upper() == 'S' and commands.__len__() == 2:
            table.named_array(commands[1])
            print(commands[1])
            print(table.show_formatted_array())

        elif command.upper() == 'X' and commands.__len__() == 1:
            for name, data in table.out.items():
                print(name)
                print(table.show_formatted_array(data))

            print("Bye Bye see you soon!")
            break

if __name__ == '__main__':
    main()
