from seed_data import seedData
from database import createConnection


def main():
    sessionmaker = createConnection()
    session = sessionmaker()

    seedData(session)

    session.close()


if __name__ == "__main__":
    main()
