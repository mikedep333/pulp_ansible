# Generated by Django 2.2.4 on 2019-08-19 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0009_collectionimport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ansibledistribution',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterModelOptions(
            name='ansibleremote',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterModelOptions(
            name='collectionremote',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterModelOptions(
            name='collectionversion',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'default_related_name': '%(app_label)s_%(model_name)s'},
        ),
        migrations.AlterField(
            model_name='ansibledistribution',
            name='basedistribution_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ansible_ansibledistribution', serialize=False, to='core.BaseDistribution'),
        ),
        migrations.AlterField(
            model_name='ansibledistribution',
            name='repository',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ansible_ansibledistribution', to='core.Repository'),
        ),
        migrations.AlterField(
            model_name='ansibledistribution',
            name='repository_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ansible_ansibledistribution', to='core.RepositoryVersion'),
        ),
        migrations.AlterField(
            model_name='ansibleremote',
            name='remote_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ansible_ansibleremote', serialize=False, to='core.Remote'),
        ),
        migrations.AlterField(
            model_name='collectionremote',
            name='remote_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ansible_collectionremote', serialize=False, to='core.Remote'),
        ),
        migrations.AlterField(
            model_name='collectionversion',
            name='content_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ansible_collectionversion', serialize=False, to='core.Content'),
        ),
        migrations.AlterField(
            model_name='collectionversion',
            name='tags',
            field=models.ManyToManyField(editable=False, related_name='ansible_collectionversion', to='ansible.Tag'),
        ),
        migrations.AlterField(
            model_name='role',
            name='content_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ansible_role', serialize=False, to='core.Content'),
        ),
    ]
