import pandas as pd

import sys
sys.path.append('../DogMatch')
from BE.database import get_foreign_key_id, row_exists
from BE.animal import (
    DictCoatLength, DictCoatType, DictDogBreed, DogBreed, Trait, Animal
)
from BE.configuration import (
    TRAITS_DESCRIPTION_PATH, TRAITS_TRANSLATION_PATH, BREED_RANK_PATH
)


def seedDataDictBreeds(session, data_path) -> None:
    data = pd.read_csv(data_path)
    code_to_breed = {code: breed for code, breed in enumerate(data["Breed"].unique())}

    breeds = [DictDogBreed(key, value) for key, value in code_to_breed.items()]

    for breed in breeds:
        if not row_exists(session, "token", breed.token, DictDogBreed):
            session.add(breed)
    session.commit()


def seedDataDictCoatLength(session, data_path) -> None:
    data = pd.read_csv(data_path)
    code_to_coat_length = {
        code: coat_length
        for code, coat_length in enumerate(data["Coat Length"].unique())
    }

    coat_lengths = [
        DictCoatLength(key, value) for key, value in code_to_coat_length.items()
    ]

    for coat_length in coat_lengths:
        if not row_exists(session, "token", coat_length.token, DictCoatLength):
            session.add(coat_length)
    session.commit()


def seedDataDictCoatType(session, data_path) -> None:
    data = pd.read_csv(data_path)
    code_to_coat_type = {
        code: coat_type for code, coat_type in enumerate(data["Coat Type"].unique())
    }

    # TODO: improve it
    pl_dict = {
        "Double": "Podwójna",
        "Smooth": "Gładka",
        "Curly": "Kręcona",
        "Silky": "Jedwabna",
        "Wavy": "Falowana",
        "Wiry": "Szorstka (EN: Wiry)",
        "Hairless": "Bezwłosy",
        "Rough": "Szorstka (EN: Rough)",
        "Corded": "Sznurowana"
    }

    coat_types = [DictCoatType(key, value, pl_dict[value]) for key, value in code_to_coat_type.items()]

    for coat_type in coat_types:
        if not row_exists(session, "token", coat_type.token, DictCoatType):
            session.add(coat_type)
    session.commit()


def seedDataDogBreed(session, data_path, data_path_2) -> None:
    data = pd.read_csv(data_path)
    data_2 = pd.read_csv(data_path_2)

    for i, row in data.iterrows():
        dict_breed_id = get_foreign_key_id(session, DictDogBreed, row["Breed"])
        coat_type_id = get_foreign_key_id(session, DictCoatType, row["Coat Type"])
        coat_length_id = get_foreign_key_id(session, DictCoatLength, row["Coat Length"])

        dog_breed = DogBreed(
            dict_breed_id=dict_breed_id,
            photo_url=data_2.iloc[i]["Image"],
            info_url=data_2.iloc[i]["links"],
            affectionate_with_family=row["Affectionate With Family"],
            good_with_young_children=row["Good With Young Children"],
            good_with_other_dogs=row["Good With Other Dogs"],
            shedding_level=row["Shedding Level"],
            coat_grooming_frequency=row["Coat Grooming Frequency"],
            drooling_level=row["Drooling Level"],
            coat_type=coat_type_id,
            coat_length=coat_length_id,
            openness_to_strangers=row["Openness To Strangers"],
            playfulness_level=row["Playfulness Level"],
            watchdog_protective_nature=row["Watchdog/Protective Nature"],
            adaptability_level=row["Adaptability Level"],
            trainability_level=row["Trainability Level"],
            energy_level=row["Energy Level"],
            barking_level=row["Barking Level"],
            mental_stimulation_needs=row["Mental Stimulation Needs"],
        )

        if not row_exists(session, "dict_breed_id", dog_breed.dict_breed_id, DogBreed):
            session.add(dog_breed)
    session.commit()


def seedDataTrait(session, data_path, description_data_path) -> None:
    df = pd.read_csv(data_path)
    names_en = df["en"].values.tolist()
    names_pl = df["pl"].values.tolist()

    df_descriptions = pd.read_csv(description_data_path)
    descriptions_en = df_descriptions["Description"].values.tolist()

    traits = [
        Trait(name_en, name_pl, descriptions_en)
        for name_en, name_pl, descriptions_en
        in zip(names_en, names_pl, descriptions_en)
    ]

    for trait in traits:
        if not row_exists(session, "name_en", trait.name_en, Trait):
            session.add(trait)
    session.commit()


def seedAnimal(session) -> None:
    def read_photo(path):
        with open(path, 'rb') as file:
            return file.read()

    dogs = []

    dogs.append(Animal(
        name="Szarik",
        breed="German Shepherd Dogs",
        location="T-34-85 Rudy, między Studziankami a Berlinem",
        description="Choć jest owczarkiem niemieckim, niemcy się go boją. Nie wymaga dużej uwagi, zje cokolwiek mu podasz.\
              Jak pokażesz się z nim w parku, wszystkie radzieckie łączniczki będą na Ciebie leciały, a gruzińscy mechanicy będą mieli do Ciebie respekt. \
              Dobry do polowania na tygrysy syberyjskie",
        photo=read_photo("data/photos/szarik.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Alex",
        breed="German Shepherd Dogs",
        location="Łódź",
        description="Gwiazda polskiego serialu, zawsze gotowy do akcji. \
            z takim psem na pewno polecą na Ciebie młode rude aspirantki. Szacunek na komendzie gwarantowany.",
        photo=read_photo("data/photos/alex.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="K-9000",
        breed="Rottweilers",
        location="Yara Island",
        description="Wcielony diabeł, odgryzie jajca każdemu, kto zagraża jego panu. \
            Legenda głosi, że Anton Castillo zachorował na gruźlicę jak go spotkał. \
            Posiada dziwną dolegliwość, mianowicie jego sierść jest tytanowa, a oczy świecą mu się na czerwono. \
            Podobno jego pierwszym właścicielem był T-1000",
        photo=read_photo("data/photos/k9000.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Lampo",
        breed="Anatolian Shepherd Dogs",
        location="Piombino, Włochy",
        description="Miłośnik kolei (MIKOL), wiernu swojemu Panu, bohaterski. Uratował życie małej dziewczynki ryzykując swoje własne.",
        photo=read_photo("data/photos/pies koleją.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Lassie",
        breed="Collies",
        location="Szkocja",
        description="Najwierniejsza suka jaką mamy w bazie. Nawet jak ją sprzedasz,\
              wróci do Ciebie z powrotem choćby miała iść setki kilometrów przez góry.",
        photo=read_photo("data/photos/lassie.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Scooby Doo",
        breed="Pointers (German Shorthaired)",
        location="Warner Bros Studio",
        description="Trochę tchórzliwy, ale zawsze gotowy do pomocy. \
            Uwielbia chrupki, ale nie przepada za duchami.",
        photo=read_photo("data/photos/scooby.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Idefiks",
        breed="Miniature Schnauzers",
        location="Galia",
        description="Niezwykle przyjazny piesek, uwielbia szynkę. Nie przepada za Rzymianami.",
        photo=read_photo("data/photos/idefix.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Snoopy",
        breed="Beagles",
        location="Dach swojej budy",
        description="Snoopy to piesek o wielkiej wyobraźni i jeszcze większym sercu.\
            Uwielbia przesiadywać na dachu swojej budy i marzyć o byciu słynnym \
            pilotem myśliwca albo pisarzem bestsellerów.",
        photo=read_photo("data/photos/snoopy.png"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Clifford",
        breed="Cavalier King Charles Spaniels",
        location="Wielka Brytania",
        description="Charakterystyczny czerwony kolor to nie jedyna cecha dzięki której nigdy go nie zgubisz\
            Pomocny, choć często niezdarny. Pies koleżanki Twojej starej, Emily Elizabeth.",
        photo=read_photo("data/photos/cliford.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Reksio",
        breed="Fox Terriers (Wire)",
        location="wieś pod Bielsko-Białą",
        description="Uwielbia gonić ptaki, aktywnie włącza się w życie rodzinne i jest bardzo ambitny. \
            Jego szczekanie rozpoznasz zawsze i wszędzie.",
        photo=read_photo("data/photos/reksio.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Pankracy",
        breed="Spaniels (Cocker)",
        location="Warszawa, ul. Woronicza 17",
        description="Niech wygląd Cię nie zmyli, to bardzo inteligentny pies.\
            Teorie spiskowe mówią, że jego pojawienie i jednoczesne zniknięcie smoka Telesfora z anteny to nie przypadek.",
        photo=read_photo("data/photos/pankracy.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Saba",
        breed="Mastiffs",
        location="Chartum oraz okoliczne pustynie i puszcze",
        description="Radosny opiekuńczy pies, potrfi być bardzo waleczny. Przyjaźni się ze słoniami. \
            Odważy się biec pod lufy porywaczy aby uratować swoich właścicieli. Stawi też czoła gorylom, ale będzie potrzebował małej pomocy słonia.",
        photo=read_photo("data/photos/saba.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Tramp",
        breed="Brittanys",
        location="Midwest, USA",
        description="Na początku będzie oziębły i nieufny, ale z czasem stanie się najlepszym przyjacielem. \
            Lepiej trzymać go na smyczy bo lubi uciekać do swojej suczki.",
        photo=read_photo("data/photos/zakochany.jpg"),
        owner_id=0
    ))

    dogs.append(Animal(
        name="Beethoven",
        breed="St. Bernards",
        location="USA",
        description="Trochę niezdarny, bardzo silny i przyjazny. \
            Obroni rodzinę jeśli nadarzy się taka potrzeba. ",
        photo=read_photo("data/photos/bethoven.jpg"),
        owner_id=0
    ))
    for i in range(1, 102):
        dogs.append(Animal(
            name="Dalmatyńczyk " + str(i),
            breed="Dalmatians",
            location="Londyn, Wielka Brytania",
            description="Kolejny ze szczęśliwej rodzinki dalmatyńczyków. \
                Lubi dzieci, ale nie przepada za starszymi kobietami w futrach",
            photo=read_photo("data/photos/dalmatians.jpg"),
            owner_id=0
        ))

    for dog in dogs:
        if not row_exists(session, "name", dog.name, Animal):
            session.add(dog)
    session.commit()


def seedData(session, data_path) -> None:
    seedDataDictCoatType(session, data_path)
    seedDataDictCoatLength(session, data_path)
    seedDataDictBreeds(session, data_path)
    seedDataDogBreed(session, data_path, BREED_RANK_PATH)
    seedDataTrait(session, TRAITS_TRANSLATION_PATH, TRAITS_DESCRIPTION_PATH)
    seedAnimal(session)
