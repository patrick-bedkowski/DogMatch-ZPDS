from sqlalchemy import CheckConstraint, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    breed = Column(String, nullable=False)
    owner_id = Column(Integer, nullable=False)
    affectionate_with_family = Column(Integer, nullable=False)
    good_with_young_children = Column(Integer, nullable=False)
    good_with_other_dogs = Column(Integer, nullable=False)
    shedding_level = Column(Integer, nullable=False)
    coat_grooming_frequency = Column(Integer, nullable=False)
    drooling_level = Column(Integer, nullable=False)
    coat_type = Column(String, nullable=False)
    coat_length = Column(String, nullable=False)
    openness_to_strangers = Column(Integer, nullable=False)
    playfulness_level = Column(Integer, nullable=False)
    watchdog_protective_nature = Column(Integer, nullable=False)
    adaptability_level = Column(Integer, nullable=False)
    trainability_level = Column(Integer, nullable=False)
    energy_level = Column(Integer, nullable=False)
    barking_level = Column(Integer, nullable=False)
    mental_stimulation_needs = Column(Integer, nullable=False)

    # CheckConstraint to enforce values between 1 and 5
    __table_args__ = (
        CheckConstraint("affectionate_with_family BETWEEN 1 AND 5"),
        CheckConstraint("good_with_young_children BETWEEN 1 AND 5"),
        CheckConstraint("good_with_other_dogs BETWEEN 1 AND 5"),
        CheckConstraint("shedding_level BETWEEN 1 AND 5"),
        CheckConstraint("coat_grooming_frequency BETWEEN 1 AND 5"),
        CheckConstraint("drooling_level BETWEEN 1 AND 5"),
        CheckConstraint("openness_to_strangers BETWEEN 1 AND 5"),
        CheckConstraint("playfulness_level BETWEEN 1 AND 5"),
        CheckConstraint("watchdog_protective_nature BETWEEN 1 AND 5"),
        CheckConstraint("adaptability_level BETWEEN 1 AND 5"),
        CheckConstraint("trainability_level BETWEEN 1 AND 5"),
        CheckConstraint("energy_level BETWEEN 1 AND 5"),
        CheckConstraint("barking_level BETWEEN 1 AND 5"),
        CheckConstraint("mental_stimulation_needs BETWEEN 1 AND 5"),
    )

    def __init__(
        self,
        name: str,
        breed: str,
        owner_id: int,
        affectionate_with_family: int,
        good_with_young_children: int,
        good_with_other_dogs: int,
        shedding_level: int,
        coat_grooming_frequency: int,
        drooling_level: int,
        coat_type: str,
        coat_length: str,
        openness_to_strangers: int,
        playfulness_level: int,
        watchdog_protective_nature: int,
        adaptability_level: int,
        trainability_level: int,
        energy_level: int,
        barking_level: int,
        mental_stimulation_needs: int,
    ):
        self.name = name
        self.breed = breed
        self.owner_id = owner_id
        self.affectionate_with_family = affectionate_with_family
        self.good_with_young_children = good_with_young_children
        self.good_with_other_dogs = good_with_other_dogs
        self.shedding_level = shedding_level
        self.coat_grooming_frequency = coat_grooming_frequency
        self.drooling_level = drooling_level
        self.coat_type = coat_type
        self.coat_length = coat_length
        self.openness_to_strangers = openness_to_strangers
        self.playfulness_level = playfulness_level
        self.watchdog_protective_nature = watchdog_protective_nature
        self.adaptability_level = adaptability_level
        self.trainability_level = trainability_level
        self.energy_level = energy_level
        self.barking_level = barking_level
        self.mental_stimulation_needs = mental_stimulation_needs

    def __repr__(self):
        return (
            f"<Animal(name='{self.name}', breed='{self.breed}', owner_id={self.owner_id}, "
            f"affectionate_with_family={self.affectionate_with_family}, "
            f"good_with_young_children={self.good_with_young_children}, good_with_other_dogs={self.good_with_other_dogs}, "
            f"shedding_level={self.shedding_level}, coat_grooming_frequency={self.coat_grooming_frequency}, "
            f"drooling_level={self.drooling_level}, coat_type='{self.coat_type}', coat_length='{self.coat_length}', "
            f"openness_to_strangers={self.openness_to_strangers}, "
            f"playfulness_level={self.playfulness_level}, watchdog_protective_nature={self.watchdog_protective_nature}, "
            f"adaptability_level={self.adaptability_level}, trainability_level={self.trainability_level}, "
            f"energy_level={self.energy_level}, barking_level={self.barking_level}, "
            f"mental_stimulation_needs={self.mental_stimulation_needs})>"
        )


class DictCoatType(Base):
    __tablename__ = "dict_coat_type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String, nullable=False)

    def __init__(self, token: str):
        self.token = token

    def __repr__(self):
        return f"<DictCoatType(token='{self.token}')>"


class DictCoatLength(Base):
    __tablename__ = "dict_coat_length"
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String, nullable=False)

    def __init__(self, token: str):
        self.token = token

    def __repr__(self):
        return f"<DictCoatLength(token='{self.token}')>"
