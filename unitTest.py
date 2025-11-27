# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import unittest
from unittest.mock import Mock, MagicMock, patch
from mainCode import *
import pytest
import os

# ---------------------------------------------------------------------
# Class of unit tests
# ---------------------------------------------------------------------
class my_unit_tests(unittest.TestCase):

    # ---------------------------------------------------------------------
    # File handling unit tests
    # ---------------------------------------------------------------------

    # Tests if the csv file has been saved
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile('historicalData.csv'))

    # ---------------------------------------------------------------------
    # TESTING: read_nordic_data()
    # ---------------------------------------------------------------------

    # Tests if the df file has the Daily Price colum made
    def test_df_headings(self):
        if 'Daily Price Change' in df:
            result = True
        self.assertEqual(result, True)

    # ---------------------------------------------------------------------
    # TESTING: plot_graph()
    # ---------------------------------------------------------------------

    # Test the sort has been triggered
    def test_np_sort(self):
        sorted_sample, nlogn = plot_graph(daily_change_array)
        assert np.all(np.diff(sorted_sample) >= 0)



    # Test that nlogn has been calculated correctly
    def test_nlogn_correct(self):
        n_values = np.array([10, 20, 30]) # Checking with known vals
        expected_result = np.array([
        10 * np.log(10),
        20 * np.log(20),
        30 * np.log(30)
    ])
        actual_result = compute_nlogn(n_values)
        assert np.allclose(expected_result, actual_result)


    # run the tests
if __name__ == "__main__":
    unittest.main()


# y = 4.07x -0.67