from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from config import *


styles = getSampleStyleSheet()


def add_header(story):

    title = styles["Title"]
    normal = styles["BodyText"]

    story.append(

        Paragraph(

            f"<font size=20><b>{LAB_NAME}</b></font>",

            title

        )

    )

    story.append(

        Paragraph(

            LAB_TAGLINE,

            normal

        )

    )

    story.append(

        Paragraph(

            LAB_ADDRESS,

            normal

        )

    )

    story.append(

        Paragraph(

            f"{LAB_PHONE} | {LAB_EMAIL}",

            normal

        )

    )

    story.append(

        Spacer(1, 20)

    )