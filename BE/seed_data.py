from database import row_exists
from animal import Animal, DictCoatLength, DictCoatType


def seedData(session) -> None:
    animals_to_add = [
        Animal(
            "Timmy",
            "French Bulldogs",
            137,
            5,
            5,
            4,
            3,
            1,
            3,
            "Smooth",
            "Short",
            5,
            5,
            3,
            5,
            4,
            3,
            1,
            3,
        )
    ]
    for animal in animals_to_add:
        if not row_exists(session, "name", animal.name, Animal):
            session.add(animal)

    coat_types_to_add = [
        DictCoatType("Double"),
        DictCoatType("Smooth"),
        DictCoatType("Curly"),
        DictCoatType("Silky"),
        DictCoatType("Wavy"),
        DictCoatType("Wiry"),
        DictCoatType("Hairless"),
        DictCoatType("Rough"),
        DictCoatType("Corded"),
    ]

    for coat_type in coat_types_to_add:
        if not row_exists(session, "token", coat_type.token, DictCoatType):
            session.add(coat_type)

    session.commit()

    coat_lengths_to_add = [
        DictCoatLength("Short"),
        DictCoatLength("Medium"),
        DictCoatLength("Long"),
    ]

    for coat_length in coat_lengths_to_add:
        if not row_exists(session, "token", coat_length.token, DictCoatLength):
            session.add(coat_length)

    session.commit()
