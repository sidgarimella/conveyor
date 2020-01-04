from func_timeout import FunctionTimedOut

import unittest
import sys
import errno

import conveyor

class TestTimeoutRun(unittest.TestCase):
    def setUp(self):
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")

    """ Causes issues with file handling in other tests. Passes independently, but omit for now.
    def test_notebook_timeout(self):
        self.assertRaises(FunctionTimedOut, conveyor.run_notebook, 
            "conveyor/examples/tests/Big Timeout.ipynb", timeout=2)
    """
