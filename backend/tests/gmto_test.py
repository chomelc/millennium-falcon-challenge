import pytest
import unittest
import os

from ..functions.gmto_functions import compute_odds, get_odds


class TestComputeOdds(unittest.TestCase):
    def test_first_sample(self):
        empire = f"{os.environ.get('MFC_PATH')}/sample-data/empire1.json"
        mf = f"{os.environ.get('MFC_PATH')}/backend/millennium-falcon.json"
        assert get_odds(compute_odds(empire, mf)) == 0

    def test_second_sample(self):
        empire = f"{os.environ.get('MFC_PATH')}/sample-data/empire2.json"
        mf = f"{os.environ.get('MFC_PATH')}/backend/millennium-falcon.json"
        assert get_odds(compute_odds(empire, mf)) == 81

    def test_third_sample(self):
        empire = f"{os.environ.get('MFC_PATH')}/sample-data/empire3.json"
        mf = f"{os.environ.get('MFC_PATH')}/backend/millennium-falcon.json"
        assert get_odds(compute_odds(empire, mf)) == 90

    def test_fourth_sample(self):
        empire = f"{os.environ.get('MFC_PATH')}/sample-data/empire4.json"
        mf = f"{os.environ.get('MFC_PATH')}/backend/millennium-falcon.json"
        assert get_odds(compute_odds(empire, mf)) == 100
