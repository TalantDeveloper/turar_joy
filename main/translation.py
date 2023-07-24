from modeltranslation.translator import TranslationOptions, register
from .models import Faculties


@register(Faculties)
class FacultiesTranslationOptions(TranslationOptions):
    fields = ('name',)

