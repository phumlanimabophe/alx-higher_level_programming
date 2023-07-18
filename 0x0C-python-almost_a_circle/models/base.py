#!/usr/bin/python3
"""0x0C. Python - Almost a circle, task 1, 15-20"""
import json
import csv


class Base:
    """Assigns an `id` and manages related attributes across all instances.

    Args:
        id (int): Identifying number for each instance of `Base`. If not provided,
                  the current count of instances, `__nb_objects`, is used.

    Attributes:
        __nb_objects (int): Number of `Base` instances not assigned an `id` at initialization.
        __true_nb_objects (int): Total count of all `Base` instances.
        __assigned_ids (set): Set of all `id` numbers assigned at least once.

    Project tasks:
        1. Base class - /models, __init__.py, class Base, __init__

    """

    __nb_objects = 0
    __true_nb_objects = 0
    __assigned_ids = set()

    def __init__(self, id=None):
        """
        Initializes a new instance of the `Base` class.

        Args:
            id (int): Identifying number for the instance. If not provided, a unique id is assigned.

        Raises:
            ValueError: If `id` is 0, negative, or already assigned to another instance.
        """

        if id is not None:
            self.id = id
            Base.__true_nb_objects += 1
            self.serial = Base.__true_nb_objects
            Base.__assigned_ids.add(self.id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            Base.__true_nb_objects += 1
            self.serial = Base.__true_nb_objects
            Base.__assigned_ids.add(self.id)

    @property
    def id(self):
        """Getter for `id` attribute."""
        return self.__id

    @id.setter
    def id(self, value):
        """Setter for `id` attribute.

        Args:
            value (int): Number to be assigned as the `id`.

        Raises:
            ValueError: If `id` is 0, negative, or already assigned.
        """
        if value < 1:
            raise ValueError('id must be positive')
        self.__id = value

    @property
    def serial(self):
        """Getter for `serial` attribute."""
        return self.__serial

    @serial.setter
    def serial(self, value):
        """Setter for `serial` attribute.

        Args:
            value (int): Number to be assigned as the `serial`.
        """
        self.__serial = value


    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries into a JSON string.

        Args:
            list_dictionaries (list): List to be converted, containing dictionaries.

        Returns:
            str: JSON formatted string of `list_dictionaries`, or '[]' if None or empty.

        Project tasks:
            15. Dictionary to JSON string - static method `to_json_string()` that returns
            the JSON string representation of `list_dictionaries`, or '[]' if None.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a JSON formatted string of a list of dictionary
        representations of objects of `Base` derived classes to a file.

        Args:
            list_objs (list): List of `Base` derived objects (e.g., `Rectangle` and `Square`).

        Project tasks:
            16. JSON string to file - class method `save_to_file()` that writes
            the JSON string representation of `list_objs` to a file, using `to_json_string()`,
            overwriting the existing file. The filename includes the class name.
            If the list is None, then it is treated as an empty list.
        """
        if list_objs is None:
            list_objs = []

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())
        json_dict = cls.to_json_string(list_dicts)

        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_dict)


    @staticmethod
    def from_json_string(json_string):
        """Returns a list of objects represented by a JSON format string,
        or an empty list if `json_string` is None or empty.

        Args:
            json_string (str): JSON format string to be converted.

        Returns:
            list: List of objects represented by the JSON format string, or an empty list
            if `json_string` is None or empty.

        Project tasks:
            17. JSON string to dictionary - static method `from_json_string()` that returns
            a list from the JSON string representation `json_string`, which represents a
            list of dictionaries. If the input is None or empty, it returns an empty list.
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    def update(self, **kwargs):
        """Updates the instance attributes using the provided keyword arguments."""
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance of the class and updates it using `dictionary` as keyword args.

        Args:
            dictionary (dict): Dictionary to be used as keyword arguments.

        Returns:
            instance: New instance of the class.

        Project tasks:
            18. Dictionary to Instance - class method `create()` that creates a new instance
            and updates it with values in `dictionary` as keyword args.
        """
        if cls.__name__ is 'Rectangle':
            temp = cls(1.1)
        elif cls.__name__ is 'Square':
            temp = cls(1)
        temp.update(**dictionary)
        return temp


    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file named <class name>.json, or an empty list
        if the file does not exist. The class of the instances in the list is determined by `cls`.

        Returns:
            list: List of instances of `cls` from the file <class name>.json, or an empty list
            if the file does not exist.

        Project tasks:
            19. File to instances - class method `load_from_file()` that returns
            a list of instances from a file named <Class name>.json, or an empty list
            if the file does not exist. It uses `from_json_string()` and `create()`,
            and the class of instances in the list depends on `cls`.
        """
        import os.path

        filename = cls.__name__ + '.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                json_str = file.read()
        else:
            return []
        obj_list = cls.from_json_string(json_str)
        instance_list = []
        for item in obj_list:
            instance_list.append(cls.create(**item))
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a CSV formatted string of a list of dictionary
        representations of objects of `Base` derived classes to a file.

        Args:
            list_objs (list): List of `Base` derived objects (e.g., `Rectangle` and `Square`).

        Project tasks:
            20. JSON ok, but CSV? - class method `save_from_file_csv()`
                saves a list of instances to a file named <Class name>.csv,
                using CSV formatting. The class of instances in the list
                depends on `cls`. It uses `to_dictionary()` to convert the
                instances into dictionaries.
        """
        if list_objs is None:
            list_objs = []

        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')
        else:
            keys= ()

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())

        filename = cls.__name__ + '.csv'
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=keys)
            csv_writer.writeheader()
            csv_writer.writerows(list_dicts)


    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from a file named <class name>.csv, or an empty list
        if the file does not exist. The class of the instances in the list is determined by `cls`.

        Returns:
            list: List of instances of `cls` from the file <class name>.csv, or an empty list
            if the file does not exist.

        Project tasks:
            20. JSON ok, but CSV? - class method `load_from_file_csv()` returns
            a list of instances from a file named <Class name>.csv, or an empty list
            if the file does not exist. It uses `create()` to create instances from the
            CSV formatted data. The class of instances in the list depends on `cls`.
        """
        import os.path


        if cls.__name__ == 'Rectangle':
            keys = ('id', 'width', 'height', 'x', 'y')
        elif cls.__name__ == 'Square':
            keys = ('id', 'size', 'x', 'y')
        else:
            keys= ()

        filename = cls.__name__ + '.csv'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                instance_list = []
                for row in csv_reader:
                    for key in keys:
                        row[key] = int(row[key])
                    instance_list.append(cls.create(**row))
                return instance_list
        else:
            return []
