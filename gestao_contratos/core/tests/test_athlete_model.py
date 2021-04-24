from django.test import TestCase

from gestao_contratos.core.models import Athlete


class AthleteModelTest(TestCase):
    def setUp(self) -> None:
        self.athlete = Athlete.objects.create(name='José da Silva', email='jose@silva.com', cpf='359687038-06',
                                              rg='48360457-4')
        self.athlete.save()

    def test_str_rpr(self):
        self.assertEqual('José da Silva', str(self.athlete))
