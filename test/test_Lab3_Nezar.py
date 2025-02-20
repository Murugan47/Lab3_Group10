# File: test_Lab3_Nezar.py
# Author: Nezar Mazraie
# Date: February 19th 2025
# Description: Unit tests for the area calculation functions.

import unittest
from unittest.mock import patch
from app.Lab3_Nezar import area_circle, area_trapezium, area_ellipse, area_rhombus, main

class TestShapes(unittest.TestCase):
    def test_area_circle(self):
        self.assertAlmostEqual(area_circle(5), 78.5398, places=4)
        self.assertAlmostEqual(area_circle(0), 0)
        with self.assertRaises(ValueError):
            area_circle(-5)

    def test_area_trapezium(self):
        self.assertEqual(area_trapezium(3, 5, 4), 16)
        self.assertEqual(area_trapezium(0, 0, 10), 0)
        with self.assertRaises(ValueError):
            area_trapezium(-3, 5, 4)

    def test_area_ellipse(self):
        self.assertAlmostEqual(area_ellipse(3, 4), 37.6991, places=4)
        self.assertAlmostEqual(area_ellipse(0, 4), 0)
        with self.assertRaises(ValueError):
            area_ellipse(-3, 4)

    def test_area_rhombus(self):
        self.assertEqual(area_rhombus(6, 8), 24)
        self.assertEqual(area_rhombus(0, 8), 0)
        with self.assertRaises(ValueError):
            area_rhombus(-6, 8)

class TestMainFunction(unittest.TestCase):

    @patch("builtins.input", side_effect=["circle", "5"])
    @patch("builtins.print")
    def test_main_circle(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Area:", 78.53981633974483)

    @patch("builtins.input", side_effect=["trapezium", "3", "5", "4"])
    @patch("builtins.print")
    def test_main_trapezium(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Area:", 16.0)

    @patch("builtins.input", side_effect=["ellipse", "3", "4"])
    @patch("builtins.print")
    def test_main_ellipse(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Area:", 37.69911184307752)

    @patch("builtins.input", side_effect=["rhombus", "6", "8"])
    @patch("builtins.print")
    def test_main_rhombus(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Area:", 24.0)

    @patch("builtins.input", side_effect=["square"])
    @patch("builtins.print")
    def test_main_invalid_shape(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Invalid shape!")

if __name__ == "__main__":
    unittest.main()
