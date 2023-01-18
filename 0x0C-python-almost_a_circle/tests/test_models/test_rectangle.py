#!/usr/bin/python3
""" Test module for the almost a circle project """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test Class rectangle """

    def test_Rectangle(self):
        """ define the test Method """

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 5)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 6)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)

        with self.assertRaises(TypeError) as cm:
            Rectangle(10, "2")
        self.assertEqual(cm.exception.__str__(), "height must be an integer")

        with self.assertRaises(TypeError) as cm:
            Rectangle(10, [1])
        self.assertEqual(cm.exception.__str__(), "height must be an integer")

        with self.assertRaises(TypeError) as cm:
            Rectangle("10", 1)
        self.assertEqual(cm.exception.__str__(), "width must be an integer")

        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 1, 3.5, 5)
        self.assertEqual(cm.exception.__str__(), "x must be an integer")

        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 1, 3, 5.65)
        self.assertEqual(cm.exception.__str__(), "y must be an integer")

        with self.assertRaises(ValueError) as cm:
            Rectangle(-10, 1)
        self.assertEqual(cm.exception.__str__(), "width must be > 0")

        with self.assertRaises(ValueError) as cm:
            Rectangle(10, -1)
        self.assertEqual(cm.exception.__str__(), "height must be > 0")

        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 1, -1, 3)
        self.assertEqual(cm.exception.__str__(), "x must be >= 0")

        with self.assertRaises(ValueError) as cm:
            Rectangle(10, 1, 1, -3)
        self.assertEqual(cm.exception.__str__(), "y must be >= 0")

        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(cm.exception.__str__(), "width must be > 0")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, 2)
            r.width = "3"
        self.assertEqual(cm.exception.__str__(), "width must be an integer")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(10, 2)
            r.height = "3"
        self.assertEqual(cm.exception.__str__(), "height must be an integer")

        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 2)
            r.height = -10
        self.assertEqual(cm.exception.__str__(), "height must be > 0")

        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 2)
            r.x = -10
        self.assertEqual(cm.exception.__str__(), "x must be >= 0")

        with self.assertRaises(ValueError) as cm:
            r = Rectangle(10, 2)
            r.y = -10
        self.assertEqual(cm.exception.__str__(), "y must be >= 0")

        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         '[Rectangle] (12) 2/1 - 4/6')
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         '[Rectangle] (24) 1/0 - 5/5')
        self.assertEqual(str(Rectangle(10, 12)),
                         '[Rectangle] (25) 0/0 - 10/12')
        self.assertEqual(str(Rectangle(12, 10)),
                         '[Rectangle] (26) 0/0 - 12/10')
        self.assertEqual(str(Rectangle(12, 10, 3)),
                         '[Rectangle] (27) 3/0 - 12/10')
        self.assertEqual(str(Rectangle(12, 10, 3, 6, 8)),
                         '[Rectangle] (8) 3/6 - 12/10')
