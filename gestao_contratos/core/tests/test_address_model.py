from django.test import TestCase

from gestao_contratos.core.models import Address, Athlete


class AddressModel(TestCase):
    def setUp(self) -> None:
        athlete_obj = Athlete.objects.create(name='José da Silva', email='jose@silva.com', cpf='359687038-06',
                                             rg='48360457-4')
        athlete_obj.save()

        self.address = Address.objects.create(country='Brasil', state='SP', city='Mogi das Cruzes',
                                              cep='08775-020', street='estrada cruz do seculo', number='280',
                                              athlete=athlete_obj)

    def test_address_fields(self):
        self.assertTrue(Address.objects.exists())

    def test_str(self):
        self.assertEqual('08775-020', str(self.address))
