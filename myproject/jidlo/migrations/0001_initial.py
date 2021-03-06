# Generated by Django 3.2 on 2021-05-02 08:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaceni_kategorie', models.CharField(help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný', max_length=50, unique=True, verbose_name='Označení kategorie jídel')),
                ('oblast', models.CharField(blank=True, choices=[('pálivé', 'Pálivé'), ('minutka', 'Minutka'), ('česká kuchyně', 'Česká kuchyně'), ('asijské', 'Asijské'), ('mexické', 'Mexické'), ('bez lepku', 'Bez lepku'), ('vegetariánské', 'Vegetariánské')], default='pálivé', help_text='Vyberte označení oblasti', max_length=20, verbose_name='Oblast')),
            ],
            options={
                'verbose_name': 'Kategorie jídla',
                'verbose_name_plural': 'Kategorie jídla',
                'ordering': ['oznaceni_kategorie'],
            },
        ),
        migrations.CreateModel(
            name='Jidlo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(help_text='Zadejte text o maximální délce 100 znaků', max_length=100, verbose_name='Název jídla')),
                ('popis', models.TextField(blank=True, null=True, verbose_name='Popis jídla')),
                ('cena', models.FloatField(help_text='Zadejte nezáporné desetinné číslo', null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Cena')),
                ('hodnocení', models.IntegerField(blank=True, choices=[(5, 'mňamina'), (4, 'dobré jídlo'), (3, 'průměrné jídlo'), (2, 'nic moc jídlo'), (1, 'špatné jídlo')], default=3, help_text='Vyberte označení hodnocení', verbose_name='Hodnocení jídla')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='Jidlo/%Y/%m/%d/', verbose_name='Fotka jídla')),
                ('kategorie', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='jidlo.kategorie')),
            ],
            options={
                'verbose_name': 'jídlo',
                'verbose_name_plural': 'jídla',
                'ordering': ['cena', 'nazev'],
            },
        ),
    ]
