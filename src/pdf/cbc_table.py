from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

from report_formatter import format_report


def create_cbc_table(report):

    formatted_report = format_report(report)

    cbc_data = [
        ["Test", "Result", "Reference", "Unit", "Status"]
    ]

    for row in formatted_report:

        reference = f"{row['reference'][0]} - {row['reference'][1]}"

        cbc_data.append([
            row["parameter"],
            str(row["value"]),
            reference,
            row["unit"],
            row["status"]
        ])

    table = Table(cbc_data)

    table_style = [
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
    ]

    for row_index, row in enumerate(cbc_data[1:], start=1):

        status = row[4]

        if status == "Low":

            table_style.extend([
                ("TEXTCOLOR", (1, row_index), (1, row_index), colors.orange),
                ("TEXTCOLOR", (4, row_index), (4, row_index), colors.orange),
                ("BACKGROUND", (0, row_index), (-1, row_index), colors.HexColor("#FFF3CD"))
            ])

        elif status == "High":

            table_style.extend([
                ("TEXTCOLOR", (1, row_index), (1, row_index), colors.red),
                ("TEXTCOLOR", (4, row_index), (4, row_index), colors.red),
                ("BACKGROUND", (0, row_index), (-1, row_index), colors.HexColor("#F8D7DA"))
            ])

    table.setStyle(TableStyle(table_style))

    return table