from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

from template_manager import create_patient_table
from pdf_components import create_diagnosis_section
from pdf.sections import add_header
from pdf.cbc_table import create_cbc_table

from reportlab.platypus import Image
from qr_generator import generate_qr
from pdf.footer import add_footer


def generate_pdf(report):

    filename = f"output/pdf/{report.patient['report_id']}.pdf"

    doc = SimpleDocTemplate(
        filename,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    heading = styles["Heading2"]

    story = []

    add_header(story)

    story.append(
        Paragraph(
            "<b>COMPLETE BLOOD COUNT (CBC)</b>",
            heading
        )
    )

    story.append(Spacer(1, 10))

    story.append(
        create_patient_table(report)
    )

    story.append(Spacer(1, 15))

    story.extend(
        create_diagnosis_section(report)
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "<b>CBC Results</b>",
            heading
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        create_cbc_table(report)
    )

    story.append(Spacer(1, 20))


    qr_path = generate_qr(report)

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "<b>Report Verification</b>",
            heading
        )
    )

    story.append(Spacer(1, 8))

    qr_image = Image(
        qr_path,
        width=80,
        height=80
    )

    story.append(qr_image)

    story.append(
        Paragraph(
            "Scan QR code to verify this report.",
            styles["BodyText"]
        )
    )

    add_footer(story)

    doc.build(story)