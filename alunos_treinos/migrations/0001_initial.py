# Generated by Django 4.0.5 on 2022-07-03 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alunos', '0001_initial'),
        ('exercicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlunoTreino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alunos.aluno')),
                ('exercicios', models.ManyToManyField(to='exercicios.exercicio')),
            ],
        ),
    ]