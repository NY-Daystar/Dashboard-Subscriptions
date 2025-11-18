"""test core module
To execute: python -m unittest -v core
"""

import unittest
import warnings


class TestSimple(unittest.TestCase):
    def setUp(
        self,
    ) -> None:
        warnings.simplefilter("ignore")

    def test_valid(
        self,
    ) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
