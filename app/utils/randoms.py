from random import SystemRandom
from string import ascii_letters, digits

from django.utils.text import slugify


def random_letters(k=5):
    return ''.join(SystemRandom().choices(
        ascii_letters + digits, k=k
    ))


def new_slugify(text, k=5):
    return slugify(text) + '-' + random_letters(k)
