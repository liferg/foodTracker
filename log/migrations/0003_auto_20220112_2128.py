# Generated by Django 3.0.8 on 2022-01-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_remove_food_gramsfiber'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='gramsFiber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='brand',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='gramsCarb',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='gramsFat',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='gramsProtein',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='servingSize',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='servingSizeUnit',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
