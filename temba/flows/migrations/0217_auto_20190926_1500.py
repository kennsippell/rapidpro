# Generated by Django 2.2.4 on 2019-09-26 15:00

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import temba.utils.models


class Migration(migrations.Migration):

    dependencies = [("flows", "0216_auto_20190917_2113")]

    operations = [
        migrations.AlterField(
            model_name="flowcategorycount", name="category_name", field=models.CharField(max_length=128)
        ),
        migrations.AlterField(
            model_name="flowcategorycount",
            name="flow",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="category_counts", to="flows.Flow"
            ),
        ),
        migrations.AlterField(
            model_name="flowcategorycount", name="result_key", field=models.CharField(max_length=128)
        ),
        migrations.AlterField(
            model_name="flowcategorycount", name="result_name", field=models.CharField(max_length=128)
        ),
        migrations.AlterField(
            model_name="flowlabel",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="flow_labels", to="orgs.Org"
            ),
        ),
        migrations.AlterField(
            model_name="flowlabel",
            name="uuid",
            field=models.CharField(
                db_index=True, default=temba.utils.models.generate_uuid, max_length=36, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="flownodecount",
            name="flow",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="node_counts", to="flows.Flow"
            ),
        ),
        migrations.AlterField(
            model_name="flowpathcount",
            name="flow",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="path_counts", to="flows.Flow"
            ),
        ),
        migrations.AlterField(model_name="flowpathcount", name="from_uuid", field=models.UUIDField()),
        migrations.AlterField(model_name="flowpathcount", name="period", field=models.DateTimeField()),
        migrations.AlterField(model_name="flowpathcount", name="to_uuid", field=models.UUIDField()),
        migrations.AlterField(model_name="flowpathrecentrun", name="from_step_uuid", field=models.UUIDField()),
        migrations.AlterField(model_name="flowpathrecentrun", name="from_uuid", field=models.UUIDField()),
        migrations.AlterField(model_name="flowpathrecentrun", name="to_step_uuid", field=models.UUIDField()),
        migrations.AlterField(model_name="flowpathrecentrun", name="to_uuid", field=models.UUIDField()),
        migrations.AlterField(
            model_name="flowpathrecentrun",
            name="visited_on",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="flowruncount",
            name="flow",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="exit_counts", to="flows.Flow"
            ),
        ),
        migrations.AlterField(
            model_name="flowsession",
            name="contact",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="sessions", to="contacts.Contact"
            ),
        ),
    ]
