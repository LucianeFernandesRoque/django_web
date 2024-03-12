from datetime import date
from model_bakery import baker
from cursos.models import Curso
import pytest
# def test_config():
#     assert 1==1

@pytest.fixture
def curso():
    today = date.today()
    curso = baker.make(
        Curso,
        titulo = 'Java',
        data_do_curso = today,
        carga_horaria = '50'
    )
    return curso, today

@pytest.mark.django_db
def test_str_must_return_string(curso):
    curso, today = curso
    assert str(curso) == f'Java: {today} - 50'