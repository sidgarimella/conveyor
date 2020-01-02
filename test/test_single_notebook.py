import unittest
import warnings

import conveyor

class TestSingleNotebookRun(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=ResourceWarning)

    def test_results_exist(self):
        results = conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb")
        assert results is not None

    def test_getvar(self):
        results = conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb")
        assert results.getvar('y') == 20

    def test_objects_exist(self):
        results = conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb")
        fig = results[5]['state']['fig']
        assert fig is not None

    def test_functions_export(self):
        results = conveyor.run_notebook("conveyor/examples/Sample Calculations II.ipynb")
        assert results[-1]['state']['sum_three'](2, 3, 4) == 9