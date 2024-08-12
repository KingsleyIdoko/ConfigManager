# Generated by Django 4.2.14 on 2024-08-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ip_address', models.GenericIPAddressField()),
                ('vendor_type', models.CharField(choices=[('IOS', 'Cisco'), ('EOS', 'Arista'), ('JUNOS', 'Juniper'), ('ACOS', 'A10')], default='IOS', max_length=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
