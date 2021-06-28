import unittest
from models import OrganisationUnit
from main import calculate_memebership_fee, find_config


class CalculateMembershipFee(unittest.TestCase):


    # Setup required data before testing
    def setUp(self):
            client_config = (False, 0)

            divisions = [
            ("division_a", {"config": (False, 0)}),
            ("division_b", {"config": (True, 35000)})
            ]

            areas = [
            ("area_a", {"par": 0, "config": (True, 45000)}),
            ("area_b", {"par": 0, "config": (False, 0)}),
            ("area_c", {"par": 1, "config": (True, 45000)}),
            ("area_d", {"par": 1, "config": (False, 0)})
            ]

            branches = [
            ("branch_a", {"par": 0, "config": None }),
            ("branch_b", {"par": 0, "config": (False, 0)}),
            ("branch_c", {"par": 0, "config": (False, 0)}),
            ("branch_d", {"par": 0, "config": None }),
            ("branch_e", {"par": 1, "config": (False, 0)}),
            ("branch_f", {"par": 1, "config": (False, 0)}),
            ("branch_g", {"par": 1, "config": (False, 0)}),
            ("branch_h", {"par": 1, "config": (False, 0)}),
            ("branch_i", {"par": 2, "config": (False, 0)}),
            ("branch_j", {"par": 2, "config": (False, 0)}),
            ("branch_k", {"par": 2, "config": (True, 25000)}),
            ("branch_l", {"par": 2, "config": (False, 0)}),
            ("branch_m", {"par": 3, "config": None }),
            ("branch_n", {"par": 3, "config": (False, 0)}),
            ("branch_o", {"par": 3, "config": (False, 0)}),
            ("branch_p", {"par": 3, "config": (False, 0)})
            ]

            
            # Create list to store each level objects
            division_objs = []
            area_objs = []
            branch_objs = []

            # Create entire organisation structure
            client_obj = OrganisationUnit("client", client_config)

            for division in divisions:
                division_objs.append(OrganisationUnit(division[0], division[1]["config"], client_obj))

            for area in areas:
                area_objs.append(OrganisationUnit(area[0], area[1]["config"], division_objs[area[1]["par"]]))

            for branch in branches:
                branch_objs.append(OrganisationUnit(branch[0], branch[1]["config"], area_objs[branch[1]["par"]]))

            self.client_obj = client_obj
            self.division_objs = division_objs
            self.area_objs = area_objs
            self.branch_objs = branch_objs

    def test_rent_amount_less_than_threshold(self):
        rent_amount = 2400
        rent_period = "week"
        Organisation_unit = self.area_objs[0]

        with self.assertRaises(ValueError):
            calculate_memebership_fee(rent_amount, rent_period, Organisation_unit)

    def test_rent_amount_greater_than_threshold(self):
        rent_amount = 210000
        rent_period = "week"
        Organisation_unit = self.area_objs[0]
        with self.assertRaises(ValueError):
            calculate_memebership_fee(rent_amount, rent_period, Organisation_unit)

    def test_find_config_with_no_config(self):
        self.assertEqual((True, 45000), find_config(self.branch_objs[3]))

    def test_find_config_with_config(self):
        self.assertEqual((False, 0), find_config(self.area_objs[3]))

    def test_calculate_memebership_fee_below_minimum(self):
        rent_amount = 12000
        rent_period = "month"
        Organisation_unit = self.branch_objs[5]

        self.assertEqual(144, calculate_memebership_fee(rent_amount, rent_period, Organisation_unit))

    def test_calculate_memebership_fee_above_minimum(self):
        rent_amount = 60000
        rent_period = "month"
        Organisation_unit = self.branch_objs[5]

        self.assertEqual(180, calculate_memebership_fee(rent_amount, rent_period, Organisation_unit))


if __name__ == "__main__":
    unittest.main()