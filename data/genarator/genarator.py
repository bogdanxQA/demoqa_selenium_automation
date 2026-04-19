from data.data import Person, Data
from faker import Faker

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