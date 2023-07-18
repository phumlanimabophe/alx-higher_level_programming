#!/usr/bin/python3
"""Unittest for base({..]) after task 1"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test case for the `Base` class."""

    @classmethod
    def setUpClass(cls):
        """Alerts the user if there are any instances of tested classes or subclasses that have not been cleaned up."""
        # Get the number of objects and assigned ids from the Base class
        b_obj = Base._Base__nb_objects
        b_tobj = Base._Base__true_nb_objects
        b_ids = Base._Base__assigned_ids

        # Check if the Base counter needs to be reset
        if b_obj > 1:
            print('TestBase: Previous Base counter not reset. Now at: {}'.format(b_obj))

        # Check if the total Base counter needs to be reset
        if b_tobj > 1:
            print('TestBase: Previous total Base counter not reset. Now at: {}'.format(b_tobj))

        # Check if there are any remaining assigned ids
        if len(b_ids) > 0:
            print('TestBase: Previous Base ids still potentially in use: {}'.format(b_ids))

    def tearDown(self):
        """Reinitializes the object iterator and set of assigned ids."""
        # Get the assigned ids from the Base class
        b_ids = Base._Base__assigned_ids

        # Reset the object counters to zero
        Base._Base__nb_objects = 0
        Base._Base__true_nb_objects = 0

        # Clear the assigned ids set
        b_ids.clear()

        # Check if the Base counter needs to be reset
        if Base._Base__nb_objects > 1:
            print('TestBase: Base counter not reset. Now at: {}'.format(Base._Base__nb_objects))

        # Check if the total Base counter needs to be reset
        if Base._Base__true_nb_objects > 1:
            print('TestBase: Total Base counter not reset. Now at: {}'.format(Base._Base__true_nb_objects))

        # Check if there are any remaining assigned ids
        if len(b_ids) > 0:
            print('TestBase: Base ids still potentially in use: {}'.format(b_ids))


def test_id(self):
    """Tests the `id` attribute of the Base class.

    According to the project specifications, `id` can be assumed to be an integer,
    so TypeError testing is omitted.
    """
    # Test for ValueError when id is 0 or negative
    self.assertRaises(ValueError, Base, 0)
    self.assertRaises(ValueError, Base, -5)

    # Test the id and serial attributes of Base instances
    b1 = Base(2)
    self.assertEqual(b1.id, 2)
    self.assertEqual(b1.serial, 1)

    b2 = Base()
    self.assertEqual(b2.id, 1)
    self.assertEqual(b2.serial, 2)

    b3 = Base()
    self.assertEqual(b3.id, 2)
    self.assertEqual(b3.serial, 3)

    b4 = Base(2)
    self.assertEqual(b1.id, 2)
    self.assertEqual(b1.serial, 1)
    self.assertEqual(b3.id, 2)
    self.assertEqual(b3.serial, 3)
    self.assertEqual(b4.id, 2)
    self.assertEqual(b4.serial, 4)


def test_to_json_string(self):
    """Tests the 'to_json_string' method of the Base class.

    15. Dictionary to JSON string
    """
    d_list = [{'id': 10}, {'id': 15}]
    self.assertEqual(Base.to_json_string(d_list), '[{"id": 10}, {"id": 15}]')
    self.assertEqual(Base.to_json_string([]), '[]')
    self.assertEqual(Base.to_json_string(None), '[]')

    lst = [2, 3, 4]
    self.assertEqual(Base.to_json_string(lst), '[2, 3, 4]')

    # Test for TypeError when no argument is provided
    self.assertRaises(TypeError, Base.to_json_string)

    d_list2 = [{'id': 20}]
    # Test for TypeError when multiple arguments are provided
    self.assertRaises(TypeError, Base.to_json_string, d_list, d_list2)


def test_save_to_file(self):
    """Tests the 'save_to_file' method of the Base class.

    16. JSON string to file

    AttributeError: 'to_dictionary()' is not in `Base`, only in Square/Rectangle.

    Testing of 'save_to_file' is done in 'TestRectangle' and 'TestSquare'.
    """
    pass


def test_from_json_string(self):
    """Tests the 'from_json_string' method of the Base class.

    17. JSON string to dictionary
    """
    a = Base.from_json_string('[{"id": 10}, {"id": 15}]')
    self.assertEqual(a, [{'id': 10}, {'id': 15}])

    b = Base.from_json_string('')
    self.assertEqual(b, [])

    c = Base.from_json_string(None)
    self.assertEqual(c, [])

    # Test for TypeError when no argument is provided
    self.assertRaises(TypeError, Base.from_json_string)

    # Test for TypeError when multiple arguments are provided
    self.assertRaises(TypeError, Base.from_json_string, a, b)


def test_create(self):
    """Tests the 'create' method of the Base class.

    18. Dictionary to Instance

    TypeError: '__init__' for `Base` takes 1 argument, but 'create' uses 2 to make 'temp'.

    Testing of 'create' is done in 'TestRectangle' and 'TestSquare'.
    """
    pass


def test_load_from_file(self):
    """Tests the 'load_from_file' method of the Base class.

    'load_from_file' uses 'create', so it must be tested in subclasses.

    Testing of 'create' is done in 'TestRectangle' and 'TestSquare'.
    """
    pass


if __name__ == '__main__':
    unittest.main()
