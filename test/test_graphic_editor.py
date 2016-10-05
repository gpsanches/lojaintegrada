# -*- coding: utf8 -*-

import unittest
from app.graphic_editor import GraphicEditor


class Tdd(unittest.TestCase):

    COMMANDS = ["I", "C", "L", "V", "H", "K", "F", "S", "X"]

    def setUp(self):
        self.array = GraphicEditor()

    # def test_validate_commands(self):
    #
    #     result = False
    #     self.assertTrue(result)

    def test_array_size(self):
        array = self.array.create_array(8, 10)
        w, h = self.array.size_array(array)

        self.assertEqual(10, w)
        self.assertEqual(8, h)


if __name__ == '__main__':
    unittest.main()
