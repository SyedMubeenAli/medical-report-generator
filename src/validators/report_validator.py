from cbc_reference import CBC_REFERENCE


class ValidationError(Exception):
    """Raised when a report contains invalid data."""


def validate_age(age):

    if not isinstance(age, int):
        raise ValidationError("Age must be an integer.")

    if age < 0 or age > 120:
        raise ValidationError(
            f"Invalid age: {age}"
        )


def validate_gender(gender):

    if gender not in ["Male", "Female"]:
        raise ValidationError(
            f"Invalid gender: {gender}"
        )


def validate_cbc(report):

    gender = report.patient["gender"]

    for parameter, value in report.cbc.items():

        key = parameter.lower()

        if key not in CBC_REFERENCE:
            continue

        reference = CBC_REFERENCE[key]

        if isinstance(reference, dict):

            if gender.lower() in reference:

                _, high = reference[
                    gender.lower()
                ]["normal"]

            else:

                _, high = reference["normal"]

        else:

            continue

        if value < 0:

            raise ValidationError(

                f"{parameter} cannot be negative."

            )

        if value > high * 5:

            raise ValidationError(

                f"{parameter} value looks unrealistic ({value})."

            )


def validate_report(report):

    validate_age(
        report.patient["age"]
    )

    validate_gender(
        report.patient["gender"]
    )

    validate_cbc(report)

    return True