from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Report:

    patient: Dict

    condition: str

    severity: str

    abnormal_parameters: List[str]

    cbc: Dict