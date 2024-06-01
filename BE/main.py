import pandas as pd
from sklearn.preprocessing import LabelEncoder

import sys
sys.path.append('../DogMatch')
from BE.seed_data import seedData
from BE.database import createConnection
from BE.configuration import BREED_TRAITS_PATH, MODEL_PATH
from BE.ask_model import predict, prepare_model


def main():
    sessionmaker = createConnection()
    session = sessionmaker()

    seedData(session, BREED_TRAITS_PATH)

    data = pd.read_csv("./data/breed_traits.csv")

    label_col = "Breed"
    cat_features = ["Coat Type", "Coat Length"]
    for cat in cat_features:
        data[cat] = LabelEncoder().fit_transform(data[cat])
    data[label_col] = data[label_col].astype("category").cat.codes

    model = prepare_model(MODEL_PATH)
    model.fit(data.drop(columns=[label_col]), data[label_col])

    row = data.iloc[[0]]

    print(row["Breed"])

    row = row.drop(columns=["Breed"])

    prediction_values = [5, 3, 3, 3, 3, 3, 1, 1, 3, 4, 3, 4, 4, 3, 3, 3]

    row.loc[:, :] = prediction_values

    prediction = predict(model, row)

    print(prediction)

    session.close()


if __name__ == "__main__":
    main()
