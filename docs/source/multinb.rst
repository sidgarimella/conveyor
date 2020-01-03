The `multinb` module
====================

Operations involving multiple notebooks in sequences can use pipelines to further organize execution.

There are two types of steps provided by `multinb` that are sufficient to connect and process notebooks in a great deal of ways. 

Notebook steps
""""""""""""""

Notebook steps abstract notebook files down to inputs, outputs, and the cells that should be run in between. Each notebook step requires a filename and `carry_vars` to be defined.

.. function:: add_notebook(self, filename, carry_vars, start_cell_idx=None, select_cells=None, until_variable=None)

   Contains any necessary information for running a notebook in a pipeline.

   :param filename: Name or path to Jupyter notebook file.
   :param carry_vars: Variables to save from execution for the next step.
   :param start_cell_idx: (optional) Index of code cell to begin execution at. Necessary for intercepting variables in notebooks to use the output from a prior step*
   :param select_cells: (optional) List of code cell indices to run. If not defined, will run all cells.
   :param until_variable: (optional) Name of variable to halt execution once acquired. If variable does not exist, will run all cells.

Transform steps
"""""""""""""""

Transform steps accept a dictionary containing the `carry_vars` and their computed values from the last NotebookStep (or the state from the last TransformStep) and output a dictionary containing a new state. They are useful for inserting custom functions between notebooks to rename certain variables, modify values, or dynamically remove variables from the state.

.. function:: add_transform(self, l_function)

   Contains functional information to directly modify the state in a pipeline.

   :param l_function: .. function:: l(from_state)

                         Contains logic to process from_state dictionary of variables.

                         :rtype: Dictionary of format `{ '<variable_name>' : value, ... }`

Building a pipeline
"""""""""""""""""""

By adding steps and intercepting variables using `start_cell_idx`, pipelines can help pull work between complex notebooks in one place. 


.. code-block:: python

   from conveyor.multinb import Pipeline

   data_processing = Pipeline()
   data_processing.add_notebook(filename="conveyor/examples/load_data.ipynb", carry_vars=['df'])
   data_processing.add_notebook(filename="conveyor/examples/process_data.ipynb",
       carry_vars=['magic_number'],start_cell_idx=3)

   def transform_magic(from_state):
       to_state = dict()
       to_state['transformed_magic_number'] = -1 * from_state['magic_number']
       return to_state

   data_processing.add_transform(transform_magic)
   results = data_processing.run()

For information on how to process `results` see the section on output.
