from django.test import TestCase

from gestao_contratos.core.forms import AthleteForm
from gestao_contratos.core.models import Address, Athlete


class AthleteFormTest(TestCase):
    def setUp(self) -> None:
        athlete = Athlete.objects.create(name='José da Silva', email='jose@silva.com', cpf='359687038-06',
                                         rg='48360457-4')
        athlete.save()
        self.address_valid = Address.objects.create(country='Brasil', state='SP', city='Mogi das Cruzes',
                                                    cep='08775-020', street='estrada cruz do seculo',
                                                    number='280', athlete=athlete)

    def make_form_to_validate(self, **kwargs):
        """
        Aux method to make a form AthleteForm to be validated
        :param kwargs:
        :return: instance of AthleteForm
        """
        valid = dict(name='José da Silva', email='jose@silva.com', cpf='021.212.440-42',
                     rg='12345678-9', address=self.address_valid.pk)

        # on function call, if any aditional data is passed the actual valid is updated
        data = dict(valid, **kwargs)

        form = AthleteForm(data)
        return form

    def test_fields(self):
        """
        AthleteForm must have 5 fields: name, email, cpf, rg, address
        :return: None
        """
        form = AthleteForm()
        expected = ['name', 'email', 'cpf', 'rg']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_athlete_form_valid(self):
        """
        Test AthleteForm has valid data
        :return:
        """
        form = self.make_form_to_validate()
        self.assertTrue(form.is_valid())

    def test_athele_form_name_invalid(self):
        """ Name field must have more then 3 charaters """
        form = self.make_form_to_validate(name='Aa')
        self.assertFalse(form.is_valid())
