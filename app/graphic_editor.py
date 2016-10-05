# -*- coding: utf8 -*-

from prettytable import PrettyTable


class GraphicEditor(object):

    array = []
    COMMANDS = ["I", "C", "L", "V", "H", "K", "F", "S", "X"]

    def create_array(self, w, h):
        """
        create the array
        :param w:
        :param h:
        :return:
        """
        self.array = [[0 for i in range(w)] for c in range(h)]

        return self.array

    def size_array(self):
        """
        return size of width and height
        :param array:
        :return: w int, h int
        """
        w = self.array.__len__()
        h = self.array[0].__len__()

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
        self.array[x][y] = color

        return self.array

    def clear_array(self):
        """
        Get current array and clean
        :return: array
        """
        w, h = self.size_array()

        return self.create_array(w, h)
