# Generated by Django 4.1.4 on 2023-04-17 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0010_alter_cartitem_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='Condition',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='on_deleted',
            new_name='is_admin',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='modify_at',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='package',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='rank',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitem', to='user_panel.cart'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
