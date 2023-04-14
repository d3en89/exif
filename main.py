from exif import Image

with open("./Горы.jpg", "rb") as palm_1_file:
    palm_1_image = Image(palm_1_file)

images = [palm_1_image]

for index, image in enumerate(images):
    if image.has_exif:
        status = f"contains EXIF (version {image.exif_version}) information."
        for atribute in image.get_all():
               print(f'{atribute} : {image.get(atribute)}')
    else:
        status = "does not contain any EXIF information."