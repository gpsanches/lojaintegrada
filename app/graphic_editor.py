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
        w = int(self.array.__len__())
        h = int(self.array[0].__len__())

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

        self.array[y][x] = color

        return self.array

    def clear_array(self):
        """
        Get current array and clean
        :return: array
        """
        w, h = self.size_array()

        return self.create_array(w, h)

    def named_array(self, name):
        self.out[name] = self.array
        self.clear_array()


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

        elif command.upper() == 'L' and commands.__len__() == 4:
            table.paints_coordinated(commands[1], commands[2], commands[3])
            print(table.show_formatted_array())

        elif command.upper() == 'S' and commands.__len__() == 2:
            table.named_array(commands[1])
            print(commands[1])
            print(table.show_formatted_array())

        elif command.upper() == 'X' and commands.__len__() == 1:
            for name, data in table.out.items():
                print(name)
                print(table.show_formatted_array(data))

            print("Bye Bye see you son!")
            break

if __name__ == '__main__':
    main()
