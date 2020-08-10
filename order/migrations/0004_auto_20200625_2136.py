# Generated by Django 3.0.7 on 2020-06-25 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200625_2106'),
        ('order', '0003_auto_20200625_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_info', to='user.UserInfo'),
        ),
    ]
