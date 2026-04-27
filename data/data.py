from dataclasses import dataclass


@dataclass
class Person():
    full_name : str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None


@dataclass
class Data():
    first_name : str = None
    last_name : str = None
    email : str = None
    age : int = None
    salary : int = None
    department : str = None


@dataclass
class PracticeFormData():

    first_name : str = None
    last_name : str = None
    email : str = None
    mobile_number : str = None
    current_address : str = None

@dataclass
class Date:
    day : str = None
    month : str = None
    year : str = None
    time : str = None
    year_short : str = None



SUBJECTS_LIST = [
        "Hindi", "English", "Maths", "Physics", "Chemistry", "Biology",
        "Computer Science", "Commerce", "Accounting", "Economics",
        "Arts", "Social Studies", "History", "Civics"
]

COLORS = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]

OPTIONS_FOR_VALUE = [
    "Group 1, option 1",
    "Group 1, option 2",
    "Group 2, option 1",
    "Group 2, option 2",
    "A root option",
    "Another root option"
]

OPTIONS_FOR_ONE = [
    "Dr.",
    "Mr.",
    "Mrs.",
    "Ms.",
    "Prof.",
    "Other"
]
       