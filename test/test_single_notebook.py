from func_timeout import FunctionTimedOut

import unittest
import sys
import errno

import conveyor

class TestSingleNotebookRun(unittest.TestCase):
    def setUp(self):
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")

    def test_file_exists(self):
        self.assertRaises(FileNotFoundError, conveyor.run_notebook, 
            "conveyor/examples/Sample Calculus IV.ipynb")

    def test_results_exist(self):
        results = conveyor.run_notebook("conveyor/examples/tests/Sample Calculations I.ipynb")
        assert (results is not None) or (results is not False)

    def test_getvar(self):
        results = conveyor.run_notebook("conveyor/examples/tests/Sample Calculations I.ipynb")
        assert results.getvar('y') == 20

    def test_objects_exist(self):
        results = conveyor.run_notebook("conveyor/examples/tests/Sample Calculations I.ipynb")
        fig = results[5]['state']['fig']
        assert fig is not None

    def test_nested_crossdirectory(self):
        results = conveyor.run_notebook("conveyor/examples/tests/Sample Calculations II.ipynb")
        assert (results is not None) or (results is not False)

    def test_functions_export(self):
        results = conveyor.run_notebook("conveyor/examples/tests/Sample Calculations II.ipynb")
        assert results[-1]['state']['sum_three'](2, 3, 4) == 9
    """
    def test_notebook_timeout(self):
        self.assertRaises(FunctionTimedOut, conveyor.run_notebook, 
            "conveyor/examples/tests/Big Timeout.ipynb", timeout=2)
    """
    