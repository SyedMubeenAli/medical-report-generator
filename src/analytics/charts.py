import os
from collections import Counter

import matplotlib.pyplot as plt


def generate_charts(reports):

    os.makedirs("output/charts", exist_ok=True)

    conditions = Counter()
    genders = Counter()

    for report in reports:
        conditions[report.condition] += 1
        genders[report.patient["gender"]] += 1

    plt.figure(figsize=(8, 5))

    plt.bar(
        conditions.keys(),
        conditions.values()
    )

    plt.title("Condition Distribution")
    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.savefig(
        "output/charts/condition_distribution.png"
    )

    plt.close()

    plt.figure(figsize=(6, 6))

    plt.pie(
        genders.values(),
        labels=genders.keys(),
        autopct="%1.1f%%"
    )

    plt.title("Gender Distribution")

    plt.savefig(
        "output/charts/gender_distribution.png"
    )

    plt.close()

    print("Charts generated successfully.")