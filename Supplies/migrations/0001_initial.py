# Generated by Django 3.2 on 2021-04-22 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('verified', models.BooleanField(default=False)),
                ('supply_type', models.CharField(choices=[('PLM', 'Plasma'), ('BLD', 'Blood'), ('OXY', 'OXYGEN'), ('HFD', 'Home Food')], max_length=3)),
                ('supply_desc', models.CharField(max_length=264)),
                ('primary_contact', models.IntegerField()),
                ('secondary_contact', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('supplier_name', models.CharField(max_length=128)),
                ('quantity_remaining', models.CharField(max_length=10)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Common.address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
