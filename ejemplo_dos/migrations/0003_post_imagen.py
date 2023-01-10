
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo_dos', '0002_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null='True', upload_to='posteos'),
            preserve_default='True',
        ),
    ]