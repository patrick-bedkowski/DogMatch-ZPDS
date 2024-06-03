import sys
sys.path.append('../DogMatch')
from BE import database
from BE import configuration
from BE import seed_data

sessionmaker = database.createConnection()
session = sessionmaker()

seed_data.seedData(session, configuration.BREED_TRAITS_PATH)

# breeds = database.get_table(session, seed_data.DogBreed)
# breeds = database.get_table(session, seed_data.DictDogBreed)
# for breed in breeds:
#     print(breed.id)
# print(breeds)

# print(database.get_table(session, seed_data.DogBreed))

# for x in database.get_table(session, seed_data.Trait):
#     print(x.name_en)

# breeds = database.get_table(session, seed_data.DictDogBreed)

# for breed in breeds:
#     print(breed.token)

# database.get_table("animals")
# engine = db.create_engine("sqlite:///test_database.sqlite")
# conn = engine.connect()
# metadata = db.MetaData()
# print(metadata.tables.keys())

# Student = db.Table(
#     'Student', metadata,
#     db.Column('Id', db.Integer(), primary_key=True),
#     db.Column('Name', db.String(255), nullable=False),
#     db.Column('Major', db.String(255), default="Math"),
#     db.Column('Pass', db.Boolean(), default=True)
# )
