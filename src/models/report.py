from dataclasses import dataclass


@dataclass
class Report:

    patient: dict

    condition: str

    severity: str

    abnormal_parameters: list[str]

    cbc: dict