from django.core.exceptions import ValidationError


def is_png_image(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError('The image must be in .png format.')
