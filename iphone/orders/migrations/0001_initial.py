# Generated by Django 3.2.5 on 2022-05-20 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iphone_types', models.CharField(choices=[('IPhone SE (1ST GENERATION)', 'iphone se (1st generation)'), ('IPhone 6', 'iphone 6'), ('IPhone 6 PLUS', 'iphone 6 plus'), ('IPhone 6s', 'iphone 6s'), ('IPhone 7', 'iphone 7'), ('IPhone 7 PLUS', 'iphone 7 plus'), ('IPhone 8', 'iphone 8'), ('IPhone 8 PLUS', 'iphone 8 plus'), ('IPhone X', 'iphone x'), ('IPhone XR', 'iphone Xr'), ('IPhone XS MAX', 'iphone Xs Max'), ('IPhone XS', 'iphone Xs'), ('IPhone SE (2ND GENERATION)', 'iphone se (2nd generation'), ('IPhone 11', 'iphone 11'), ('IPhone 11 PRO MAX', 'iphone 11 Pro Max'), ('IPhone 11 PRO', 'iphone 11 Pro'), ('IPhone 12', 'iphone 12'), ('IPhone 12 MINI', 'iphone 12 mini'), ('IPhone 12 PRO', 'iphone 12 Pro'), ('IPhone SE (3RD GENERATION)', 'iphone se(3rd generation)'), ('IPhone 13 MINI', 'iphone 13 mini'), ('IPhone 13', 'iphone 13'), ('IPhone 13 PRO MAX', 'iphone 13 Pro Max'), ('IPhone 13 PRO', 'iphone 13 Pro')], default='IPhone SE (1ST GENERATION)', max_length=40)),
                ('order_status', models.CharField(choices=[('PENDING', 'pending'), ('IN_TRANSIT', 'inTransit'), ('DELIVERED', 'delivered')], default='PENDING', max_length=40)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]