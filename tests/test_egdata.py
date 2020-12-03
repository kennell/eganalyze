from unittest import TestCase
from tests.utils import load_test_data
from eganalyze.lib import EgData


class TestEgData(TestCase):

    def setUp(self):
        self.df = load_test_data('portfolio')
        self.data = EgData(self.df)

    def test_normalize_columns(self):
        self.assertListEqual(
            self.data.df.columns.to_list(),
            ['project_name', 'status', 'country', 'date_funded', 'next_payment_date', 'next_payment_amount',
             'maturity_date', 'repaid_date', 'interest_rate', 'ltv', 'initial_loan_period', 'loan_period_left', 'bonus',
             'actual_return', 'outstanding_principal', 'initial_principal', 'revenue_earned', 'bonus_earned',
             'principal_repaid', 'penalties_received', 'days_late', 'id', 'url', 'outstanding_principal_percentage',
             'outstanding_interest_rate_weighted', 'outstanding_ltv_weighted']
        )
