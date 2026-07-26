from collections import Counter


def disease_distribution(reports):

    return Counter(
        report.condition
        for report in reports
    )


def gender_distribution(reports):

    return Counter(
        report.patient["gender"]
        for report in reports
    )


def severity_distribution(reports):

    return Counter(
        report.severity
        for report in reports
    )


def average_hemoglobin(reports):

    values = [

        report.cbc["Hemoglobin"]

        for report in reports

    ]

    return round(

        sum(values) / len(values),

        2

    )


def average_platelets(reports):

    values = [

        report.cbc["Platelets"]

        for report in reports

    ]

    return round(

        sum(values) / len(values),

        2

    )