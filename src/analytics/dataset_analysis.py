from collections import Counter
from statistics import mean


def analyze_dataset(reports):

    print("\n" + "=" * 60)
    print("DATASET ANALYTICS")
    print("=" * 60)

    print(f"Total Reports : {len(reports)}")

    gender_counts = Counter()

    condition_counts = Counter()

    severity_counts = Counter()

    abnormal_counts = Counter()

    ages = []

    for report in reports:

        gender_counts[report.patient["gender"]] += 1

        condition_counts[report.condition] += 1

        severity_counts[report.severity] += 1

        ages.append(report.patient["age"])

        abnormal_counts.update(report.abnormal_parameters)

    print("\nGender Distribution")

    for gender, count in gender_counts.items():
        print(f"{gender:10}: {count}")

    print("\nCondition Distribution")

    for condition, count in condition_counts.items():
        print(f"{condition:20}: {count}")

    print("\nSeverity Distribution")

    for severity, count in severity_counts.items():
        print(f"{severity:10}: {count}")

    print("\nAge Statistics")

    print(f"Minimum Age : {min(ages)}")
    print(f"Maximum Age : {max(ages)}")
    print(f"Average Age : {mean(ages):.1f}")

    print("\nMost Common Abnormal Parameters")

    if abnormal_counts:

        for parameter, count in abnormal_counts.most_common():
            print(f"{parameter:15}: {count}")

    else:

        print("None")

    print("=" * 60)