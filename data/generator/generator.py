from data.data import Person, Data, PracticeFormData
from faker import Faker
import os
import random
from pathlib import Path

faker = Faker('ru_Ru')
Faker.seed()

def person_genarated():
    yield Person(

        full_name = f'{faker.first_name()} {faker.last_name()} {faker.middle_name()}',  
        email = faker.email(),
        current_address = faker.address(),
        permanent_address = faker.address(),

    )


def data_genarated():
    yield Data(

        first_name = faker.first_name(),
        last_name = faker.last_name(),  
        email = faker.email(),
        age = faker.random_int(min = 0, max = 99),
        salary=faker.random_int(min = 0, max = 9999999999),
        department = faker.text(max_nb_chars=25)

    )




def get_project_root() -> Path:
    """Возвращает корневую папку проекта (где лежат .gitignore или requirements.txt)."""
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".gitignore").exists() or (parent / "requirements.txt").exists():
            return parent
    return current  # если маркеры не найдены, вернуть текущую папку



def file_generated():
    data_dir = get_project_root() / "data"
    data_dir.mkdir(exist_ok=True)
    file_name = f"file{random.randint(0, 999)}.txt"
    file_path = data_dir / file_name
    file_path.write_text("Hi, I hope you have Windows.", encoding='utf-8')
    return file_name, str(file_path)


def practice_form_data_generated():
    yield PracticeFormData(
        first_name = faker.first_name(),
        last_name = faker.last_name(),
        email = faker.email(),
        mobile_number = faker.numerify(text='##########'),
        current_address = faker.street_address()
        

    )