from django.db import migrations, models
import datetime

def migrate_time_to_duration(apps, schema_editor):
    Privilege = apps.get_model('privilegy', 'Privilege')
    for privilege in Privilege.objects.all():
        privilege.time_duration = datetime.timedelta(days=privilege.time)  # Преобразование дней в интервал времени
        privilege.save()

class Migration(migrations.Migration):

    dependencies = [
        ('privilegy', '0001_initial'),  # Укажите правильное имя последней миграции
    ]

    operations = [
        # Добавление нового поля с типом interval
        migrations.AddField(
            model_name='privilege',
            name='time_duration',
            field=models.DurationField(null=True),
        ),
        # Перенос данных из старого поля в новое
        migrations.RunPython(migrate_time_to_duration),
        # Удаление старого поля
        migrations.RemoveField(
            model_name='privilege',
            name='time',
        ),
        # Переименование нового поля
        migrations.RenameField(
            model_name='privilege',
            old_name='time_duration',
            new_name='time',
        ),
    ]
