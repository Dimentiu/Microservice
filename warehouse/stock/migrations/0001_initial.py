from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('country', models.CharField(max_length=500)),
            ],
            options={
                'unique_together': {('name', 'surname')},
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=200, verbose_name='Publisher')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('date_of_order', models.DateTimeField(auto_now_add=True)),

                ('status', models.CharField(choices=[('Packed', 'Packed'), ('Delivering', 'Delivering'), ('In_progress', 'In_progress'), ('Received', 'Received')], default='In_progress', max_length=30, verbose_name='Status')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.publisher')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.book')),
            ],
        ),
    ]
