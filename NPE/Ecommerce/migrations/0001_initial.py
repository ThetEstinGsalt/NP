# Generated by Django 4.2.4 on 2023-08-31 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Image', models.ImageField(upload_to='images/')),
                ('Image2', models.ImageField(upload_to='images/')),
                ('Image3', models.ImageField(upload_to='images/')),
                ('Usage', models.CharField(default='Utilitarian and decorative purposes', max_length=200)),
                ('Description', models.TextField(max_length=10000)),
                ('InStock', models.BooleanField(default=True)),
                ('Sizes', models.CharField(max_length=1000)),
                ('SubCategory', models.ManyToManyField(to='Ecommerce.productsubcategory')),
                ('category', models.ManyToManyField(to='Ecommerce.productcategory')),
            ],
        ),
    ]
