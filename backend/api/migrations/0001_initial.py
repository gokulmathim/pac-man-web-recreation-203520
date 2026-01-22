from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HighScore",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("player_name", models.CharField(max_length=64)),
                ("score", models.IntegerField()),
                ("level", models.IntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["-score", "created_at"],
            },
        ),
    ]
