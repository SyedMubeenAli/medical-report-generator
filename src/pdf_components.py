from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer


def create_diagnosis_section(report):

    styles = getSampleStyleSheet()

    heading = styles["Heading2"]
    normal = styles["BodyText"]

    story = []

    story.append(
        Paragraph("<b>Diagnosis Summary</b>", heading)
    )

    story.append(
        Paragraph(
            f"<b>Condition:</b> {report.condition}",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Severity:</b> {report.severity}",
            normal
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            "<b>Abnormal Parameters</b>",
            normal
        )
    )

    if report.abnormal_parameters:

        for parameter in report.abnormal_parameters:

            story.append(
                Paragraph(
                    f"• {parameter}",
                    normal
                )
            )

    else:

        story.append(
            Paragraph(
                "None",
                normal
            )
        )

    story.append(Spacer(1, 15))

    return story