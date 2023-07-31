from django.db import models


class Faculties(models.Model):
    name = models.CharField(max_length=200, verbose_name='Fakultet ismi')  # Translation
    link_name = models.CharField(max_length=200, verbose_name='fakultet link')

    def __str__(self):
        return self.name


class Application(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='F.I.O.')
    birthday = models.DateField(verbose_name="Tug'ilgan kun")
    gender = models.CharField(max_length=10, verbose_name='Jinsi')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=50, verbose_name='Telefon nomer')

    faculty = models.ForeignKey(Faculties, verbose_name='Fakultet', on_delete=models.CASCADE, null=True, blank=True)
    course = models.CharField(max_length=20, verbose_name='Kurs', null=True, blank=True)
    image = models.ImageField(upload_to="./image/", verbose_name='Image')

    # ijtimoiy holati
    i_va_ii = models.FileField(upload_to='./i_va_ii/', verbose_name='I va II guruh nogiron', null=True, blank=True)
    temir_daftar = models.FileField(upload_to='./temir_daftar/', verbose_name='Temir daftar', null=True, blank=True)
    yetim = models.FileField(upload_to='./yetim/', verbose_name='Yetim', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Ariza vaqti')

    is_qabul = models.BooleanField(default=False, verbose_name='Qabul qilindi')
    is_radetildi = models.BooleanField(default=False, verbose_name='Rad etildi')
    commit = models.TextField(verbose_name='Sababi', null=True, blank=True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return self.full_name
