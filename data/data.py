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



SUBJECTS_LIST = [
        "Hindi", "English", "Maths", "Physics", "Chemistry", "Biology",
        "Computer Science", "Commerce", "Accounting", "Economics",
        "Arts", "Social Studies", "History", "Civics"
]
       