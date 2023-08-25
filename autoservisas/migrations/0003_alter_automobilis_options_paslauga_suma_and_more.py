# Generated by Django 4.2.4 on 2023-08-22 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0002_automobilis_paslauga_uzsakymas_uzsakymoeilute'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automobilis',
            options={'verbose_name': 'Automobilis', 'verbose_name_plural': 'Automobiliai'},
        ),
        migrations.AddField(
            model_name='paslauga',
            name='suma',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Suma'),
        ),
        migrations.AlterField(
            model_name='automobilis',
            name='automobilio_modelis_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.automobilio_modelis', verbose_name='Automobilis'),
        ),
    ]
