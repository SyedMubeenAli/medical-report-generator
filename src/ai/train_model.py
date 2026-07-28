import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

DATASET_PATH = "data/datasets/cbc_dataset.csv"

MODEL_FOLDER = "src/models"

MODEL_PATH = os.path.join(
    MODEL_FOLDER,
    "cbc_model.pkl"
)

GENDER_ENCODER_PATH = os.path.join(
    MODEL_FOLDER,
    "gender_encoder.pkl"
)

ENCODER_PATH = os.path.join(
    MODEL_FOLDER,
    "label_encoder.pkl"
)


def train():

    dataframe = pd.read_csv(DATASET_PATH)

    X = dataframe.drop(columns=["Condition"])

    gender_encoder = LabelEncoder()

    X["Gender"] = gender_encoder.fit_transform(
        X["Gender"]
    )

    encoder = LabelEncoder()

    y = encoder.fit_transform(
        dataframe["Condition"]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("\nAccuracy:", round(accuracy * 100, 2), "%\n")

    print(
        classification_report(
            y_test,
            predictions,
            target_names=encoder.classes_
        )
    )

    os.makedirs(
        MODEL_FOLDER,
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    joblib.dump(
        encoder,
        ENCODER_PATH
    )

    joblib.dump(
        gender_encoder,
        GENDER_ENCODER_PATH
    )

    print("\nModel Saved:", MODEL_PATH)
    print("Encoder Saved:", ENCODER_PATH)


if __name__ == "__main__":

    train()