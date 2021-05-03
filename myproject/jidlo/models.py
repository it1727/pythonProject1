from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.

class Kategorie(models.Model):
    oznaceni_kategorie = models.CharField(max_length=50, unique=True, verbose_name="Označení kategorie jídel",
                                          help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný')
    OBLAST = (
        ('pálivé', 'Pálivé'),
        ('minutka', 'Minutka'),
        ('česká kuchyně', 'Česká kuchyně'),
        ('asijské', 'Asijské'),
        ('mexické', 'Mexické'),
        ('bez lepku', 'Bez lepku'),
        ('vegetariánské', 'Vegetariánské'),
    )
    oblast = models.CharField(max_length=20, choices=OBLAST, blank=True, default='pálivé', verbose_name="Oblast",
                              help_text='Vyberte označení oblasti')

    class Meta:
        ordering = ["oznaceni_kategorie"]
        verbose_name = 'Kategorie jídla'
        verbose_name_plural = 'Kategorie jídla'

    def __str__(self):
        return f"{self.oznaceni_kategorie}, {self.oblast}"


class Jidlo(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název jídla",
                             help_text='Zadejte text o maximální délce 100 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Popis jídla")
    cena = models.FloatField(validators=[MinValueValidator(0.0)], null=True,
                             help_text="Zadejte nezáporné desetinné číslo", verbose_name="Cena")
    HODNOCENÍ = (
        (5, 'mňamina'),
        (4, 'dobré jídlo'),
        (3, 'průměrné jídlo'),
        (2, 'nic moc jídlo'),
        (1, 'špatné jídlo'),
    )
    hodnocení = models.IntegerField(choices=HODNOCENÍ, blank=True, default=3, verbose_name="Hodnocení jídla",
                                    help_text='Vyberte označení hodnocení')
    foto = models.ImageField(upload_to='Jidlo/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka jídla")
    kategorie = models.ForeignKey(Kategorie, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["cena", "nazev"]
        verbose_name = 'jídlo'
        verbose_name_plural = 'jídla'

    def __str__(self):
        return f"{self.nazev}, {self.cena}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


from django.db import models

# Create your models here.
