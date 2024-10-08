# Generated by Django 5.1 on 2024-08-20 09:47

import datetime
import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NIC",
            fields=[
                (
                    "nic_number",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("delivery_date", models.DateField()),
                (
                    "expiration_date",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.expressions.CombinedExpression(
                            models.F("delivery_date"),
                            "+",
                            models.Value(datetime.timedelta(days=1827)),
                        ),
                        output_field=models.DateField(),
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "NIC",
                "db_table_comment": "National Identity Card",
            },
        ),
    ]
