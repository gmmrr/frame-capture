import os
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

base_path = os.path.expanduser("~/Desktop/frames/20. 林冠銘/")

page_width, page_height = A4
page_width /= cm
page_height /= cm

photo_width = 3.5
photo_height = 4.5
margin_top_bottom = 0.85
margin_left_right = 0.99
spacing_horizontal = 0.38
spacing_vertical = 0.20

dpi = 300
photos = [Image.open(os.path.join(base_path, f'frame_{i+1}.jpg')) for i in range(300)]
resized_photos = [
    photo.resize((int(photo_width * dpi / 2.54), int(photo_height * dpi / 2.54)), Image.LANCZOS)
    for photo in photos
]

for pdf_index in range(10):
    pdf_file = os.path.join(base_path, f"../file/20_{pdf_index + 1}.pdf")
    c = canvas.Canvas(pdf_file, pagesize=A4)

    start_x = margin_left_right
    start_y = page_height - margin_top_bottom - photo_height

    for row in range(6):
        for col in range(5):
            photo_index = pdf_index * 30 + row * 5 + col
            if photo_index < len(resized_photos):
                x = start_x + col * (photo_width + spacing_horizontal)
                y = start_y - row * (photo_height + spacing_vertical)
                photo = resized_photos[photo_index]
                c.drawInlineImage(photo, x * cm, y * cm, photo_width * cm, photo_height * cm)

    c.showPage()
    c.save()
    print(f"PDF saved as {pdf_file}")
