# Generated by Django 2.1.2 on 2018-10-22 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20181004_0109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campania',
            options={'verbose_name': 'Campaña', 'verbose_name_plural': 'Campañas'},
        ),
        migrations.AlterModelOptions(
            name='campania_insumo',
            options={'verbose_name': 'Campaña insumo', 'verbose_name_plural': 'Campañas de insumos'},
        ),
        migrations.AlterModelOptions(
            name='insumo',
            options={'verbose_name': 'Insumo', 'verbose_name_plural': 'Insumos'},
        ),
        migrations.AlterModelOptions(
            name='login',
            options={'verbose_name': 'Login', 'verbose_name_plural': 'Login'},
        ),
        migrations.AlterModelOptions(
            name='mascota',
            options={'verbose_name': 'Mascota', 'verbose_name_plural': 'Mascotas'},
        ),
        migrations.AlterModelOptions(
            name='origen_mascota',
            options={'verbose_name': 'Origen mascota', 'verbose_name_plural': 'Origen de mascotas'},
        ),
        migrations.AlterModelOptions(
            name='raza',
            options={'verbose_name': 'Raza', 'verbose_name_plural': 'Razas'},
        ),
        migrations.AlterModelOptions(
            name='refugio',
            options={'verbose_name': 'Refugio', 'verbose_name_plural': 'Refugios'},
        ),
        migrations.AlterModelOptions(
            name='tipo_campania',
            options={'verbose_name': 'Tipo campaña', 'verbose_name_plural': 'Tipos de campaña'},
        ),
        migrations.AlterModelOptions(
            name='tipo_insumo',
            options={'verbose_name': 'Tipo Insumo', 'verbose_name_plural': 'Tipos de Insumo'},
        ),
        migrations.AlterModelOptions(
            name='tipo_usuario',
            options={'verbose_name_plural': 'Tipos de Usuario'},
        ),
        migrations.AlterModelOptions(
            name='tipo_vivienda',
            options={'verbose_name_plural': 'Tipos de Vivienda'},
        ),
        migrations.AlterModelOptions(
            name='transferencia',
            options={'verbose_name': 'Transferencia', 'verbose_name_plural': 'Transferencias'},
        ),
        migrations.AlterModelOptions(
            name='visita_adopcion',
            options={'verbose_name': 'Visita adopcion', 'verbose_name_plural': 'Visitas de adopcion'},
        ),
        migrations.AlterModelOptions(
            name='visita_medica',
            options={'verbose_name': 'Visita Medica', 'verbose_name_plural': 'Visitas Medicas'},
        ),
    ]
