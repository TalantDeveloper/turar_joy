from django.db import models

Genders = (
    ('M', 'Erkak'),
    ('F', 'Ayol'),
)


Courses = (
    ('1-kurs', '1-Kurs'),
    ('2-kurs', '2-Kurs'),
    ('3-kurs', '3-Kurs'),
    ('4-kurs', '4-Kurs'),
    ('5-kurs', '5-Kurs'),
)


class Faculties(models.Model):
    name = models.CharField(max_length=200, verbose_name='Fakultet ismi')
    link_name = models.CharField(max_length=200, verbose_name='fakultet link')

    def __str__(self):
        return self.name


class Application(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='F.I.O.')

    birthday = models.DateField(verbose_name="Tug'ilgan kun")
    gender = models.CharField(max_length=10, choices=Genders)
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=50, verbose_name='Telefon nomer')

    faculty = models.ForeignKey(Faculties, verbose_name='Fakultet', on_delete=models.CASCADE)
    course = models.CharField(max_length=20, verbose_name='Kurs', choices=Courses)
    student_id = models.CharField(max_length=20, verbose_name='student_id')
    image = models.ImageField(upload_to="./student_image/", verbose_name='Image')

    def __str__(self):
        return self.full_name
