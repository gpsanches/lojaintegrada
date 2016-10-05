# -*- coding: utf8 -*-

import unittest
from app.graphic_editor import GraphicEditor


class Tdd(unittest.TestCase):

    def setUp(self):
        self.array = GraphicEditor()

    # def test_validate_commands(self):
    #
    #     result = False
    #     self.assertTrue(result)

    def test_array_size(self):
        self.array.create_array(8, 10)
        w, h = self.array.size_array()

        self.assertEqual(10, w)
        self.assertEqual(8, h)

    def test_create_array(self):
        array = self.array.create_array(2, 2)

        self.assertIsNotNone(array)

    def test_clean_array(self):
        self.array.create_array(3, 3)
        array_size = self.array.size_array()
        self.array.paints_coordinated(0, 0, 'A')
        self.array.paints_coordinated(1, 0, 'A')
        self.array.paints_coordinated(2, 0, 'A')
        array_clear = self.array.clear_array()
        array_clear_size = self.array.size_array()

        self.assertEqual(0, array_clear[0][0])
        self.assertEqual(0, array_clear[1][0])
        self.assertEqual(0, array_clear[2][0])
        self.assertEqual(array_size, array_clear_size)

    def test_paints_a_coordinated(self):
        self.array.create_array(2, 2)
        array = self.array.paints_coordinated(2, 2, 'C')

        self.assertEqual(0, array[0][0])
        self.assertEqual(0, array[0][1])
        self.assertEqual(0, array[1][0])
        self.assertEqual('C', array[1][1])

    def test_array_name(self):
        self.assertEqual([], self.array.array)
        self.array.create_array(3, 4)
        self.assertIsNotNone(self.array.array)
        self.assertEqual({}, self.array.out)
        self.array.paints_coordinated(2, 3, 'A')
        self.array.named_array('guilherme.bmp')

        for i in self.array.array:
            for j in i:
                self.assertEqual(0, j)


if __name__ == '__main__':
    unittest.main()
