import unittest
import sys

from conveyor.multinb import Pipeline

class TestPipelineRun(unittest.TestCase):
    def setUp(self):
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")

    def test_pipeline_additions(self):
        data_processing1 = Pipeline()
        data_processing1.add_notebook(filename="conveyor/examples/load_data.ipynb", carry_vars=['df'])
        data_processing1.add_notebook(filename="conveyor/examples/process_data.ipynb",
            carry_vars=['magic_number'],start_cell_idx=3)

        def transform_magic(from_state):
            to_state = dict()
            to_state['transformed_magic_number'] = -1 * from_state['magic_number']
            return to_state

        data_processing1.add_transform(transform_magic)
        assert len(data_processing1.steps) == 3

    def test_pipeline_output_exists(self):
        data_processing2 = Pipeline()
        data_processing2.add_notebook(filename="conveyor/examples/load_data.ipynb", carry_vars=['df'])
        data_processing2.add_notebook(filename="conveyor/examples/process_data.ipynb",
            carry_vars=['magic_number'],start_cell_idx=3)

        def transform_magic(from_state):
            to_state = dict()
            to_state['transformed_magic_number'] = -1 * from_state['magic_number']
            return to_state

        data_processing2.add_transform(transform_magic)
        output1 = data_processing2.run()
        assert output1 is not None

    def test_pipeline_output_accurate(self):
        data_processing3 = Pipeline()
        data_processing3.add_notebook(filename="conveyor/examples/load_data.ipynb", carry_vars=['df'])
        data_processing3.add_notebook(filename="conveyor/examples/process_data.ipynb",
            carry_vars=['magic_number'],start_cell_idx=3)

        def transform_magic(from_state):
            to_state = dict()
            to_state['transformed_magic_number'] = -1 * from_state['magic_number']
            return to_state

        data_processing3.add_transform(transform_magic)
        output2 = data_processing3.run()
        assert output2[-1]['result']['transformed_magic_number'] == -30

    def test_pipeline_output_stages(self):
        data_processing4 = Pipeline()
        data_processing4.add_notebook(filename="conveyor/examples/load_data.ipynb", carry_vars=['df'])
        data_processing4.add_notebook(filename="conveyor/examples/process_data.ipynb",
            carry_vars=['magic_number'],start_cell_idx=3)

        def transform_magic(from_state):
            to_state = dict()
            to_state['transformed_magic_number'] = -1 * from_state['magic_number']
            return to_state

        data_processing4.add_transform(transform_magic)
        output3 = data_processing4.run()
        assert len(output3) == 3
