from reportlab.platypus import (
    Table,
    TableStyle
)

from reportlab.lib import colors


def create_patient_table(report):

    patient = report.patient

    data = [

        ["Patient Name", patient["name"]],

        ["Patient ID", patient["patient_id"]],

        ["Report ID", patient["report_id"]],

        ["Age", patient["age"]],

        ["Gender", patient["gender"]],

        ["Doctor", patient["doctor"]]

    ]

    table = Table(

        data,

        colWidths=[120, 250]

    )

    table.setStyle(

        TableStyle([

            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

            ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EAF2F8")),

            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),

            ("BOTTOMPADDING", (0, 0), (-1, -1), 8)

        ])

    )

    return table