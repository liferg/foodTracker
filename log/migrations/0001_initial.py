# Generated by Django 3.0.8 on 2022-01-12 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=120)),
                ('brand', models.CharField(max_length=120)),
                ('servingSize', models.IntegerField()),
                ('servingSizeUnit', models.CharField(max_length=120)),
                ('calories', models.IntegerField()),
                ('gramsProtein', models.IntegerField()),
                ('gramsCarb', models.IntegerField()),
                ('gramsFat', models.IntegerField()),
                ('gramsFiber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SingleDayFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('breakfast', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='breakfastFoods', to='log.Food')),
                ('dinner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='dinnerFoods', to='log.Food')),
                ('lunch', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lunchFoods', to='log.Food')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=120)),
                ('lastName', models.CharField(max_length=120)),
                ('userName', models.CharField(max_length=120)),
                ('foodDiary', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='log.SingleDayFood')),
            ],
        ),
    ]