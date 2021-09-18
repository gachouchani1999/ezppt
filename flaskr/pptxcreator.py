from pptx import Presentation
from flask import url_for


THEME_PATH = {
    1: 'themes/gallery.pptx'
    2: 'themes/ion.pptx'
    3: 'themes/ion-boardroom.pptx'
    4: 'themes/organic.pptx'
    5: 'themes/slice.pptx'
}


def create_slides(theme, title, summaries):

    """
    Inputs:
        theme -- (int) the theme number
        title -- (str) presentation title
        summaries -- (list[list]) slide content
    """

    path = url_for('static', filename=THEME_PATH[theme])
    prs = Presentation(path)

    title_slide_layout = prs.slide_layouts[0]
    bullet_slide_layout = prs.slide_layouts[1]

    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    title.text = title
    subtitle = slide.placeholders[1]
    subtitle.text = "Made by TBD"

    for summary in summaries:

        slide = prs.slides.add_slide(bullet_slide_layout)

        title_shape = slide.shapes.title
        body_shape = slide.shapes.placeholders[1]
        tf = body_shape.text_frame

        for index, point in enumerate(summary):
            if index == 0:
                title_shape.text = point
            elif index == 1:
                tf.text = point
            else:
                p = tf.add_paragraph()
                p.text = point

    prs.save(title + '.pptx')
