from data.data import Person
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