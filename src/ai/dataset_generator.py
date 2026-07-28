import os
import random

import pandas as pd

OUTPUT_FOLDER = "data/datasets"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "cbc_dataset.csv")


def random_gender():

    return random.choice([
        "Male",
        "Female"
    ])


def generate_record(condition):

    age = random.randint(18, 80)
    gender = random_gender()

    if condition == "Normal":

        hemoglobin = round(random.uniform(13.5, 17.5), 1)
        wbc = random.randint(4500, 11000)
        rbc = round(random.uniform(4.5, 5.8), 2)
        platelets = random.randint(150000, 450000)

    elif condition == "Anemia":

        hemoglobin = round(random.uniform(6.5, 11.5), 1)
        wbc = random.randint(4500, 11000)
        rbc = round(random.uniform(3.0, 4.3), 2)
        platelets = random.randint(150000, 450000)

    elif condition == "Leukocytosis":

        hemoglobin = round(random.uniform(13.5, 17.5), 1)
        wbc = random.randint(12000, 25000)
        rbc = round(random.uniform(4.5, 5.8), 2)
        platelets = random.randint(150000, 450000)

    elif condition == "Leukopenia":

        hemoglobin = round(random.uniform(13.5, 17.5), 1)
        wbc = random.randint(1500, 4000)
        rbc = round(random.uniform(4.5, 5.8), 2)
        platelets = random.randint(150000, 450000)

    elif condition == "Thrombocytopenia":

        hemoglobin = round(random.uniform(13.5, 17.5), 1)
        wbc = random.randint(4500, 11000)
        rbc = round(random.uniform(4.5, 5.8), 2)
        platelets = random.randint(50000, 140000)

    hematocrit = round(rbc * 9, 1)
    mcv = random.randint(80, 100)
    mch = round(random.uniform(27, 33), 1)
    mchc = round(random.uniform(32, 36), 1)

    return {

        "Age": age,
        "Gender": gender,
        "Hemoglobin": hemoglobin,
        "WBC": wbc,
        "RBC": rbc,
        "Platelets": platelets,
        "Hematocrit": hematocrit,
        "MCV": mcv,
        "MCH": mch,
        "MCHC": mchc,
        "Condition": condition

    }


def create_dataset():

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    conditions = [
        "Normal",
        "Anemia",
        "Leukocytosis",
        "Leukopenia",
        "Thrombocytopenia"
    ]

    dataset = []

    for condition in conditions:

        for _ in range(1000):

            dataset.append(
                generate_record(condition)
            )

    random.shuffle(dataset)

    dataframe = pd.DataFrame(dataset)

    dataframe.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(f"Dataset saved to: {OUTPUT_FILE}")
    print(f"Total records: {len(dataframe)}")


if __name__ == "__main__":

    create_dataset()