Outputs
==============

Running notebooks and pipelines in Conveyor produce Result objects, which are simple wrappers on lists. The result object structures vary slightly between `run_notebook` output and `pipeline.run` output.

Simple Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To get a variable value available the last executed notebook cell, use:


.. code-block:: python

   results = conveyor.run_notebook("<notebook_name.ipynb>")
   results.getvar('<variable_name>')

where `<variable_name>` is replaced by the variable name you are trying to extract from the notebook.


Alternatively, you can use:


.. code-block:: python

   results = conveyor.run_notebook("<notebook_name.ipynb>")
   results[-1]['state']['<variable_name>']

which effectively does the same thing as the method from the first example. 

You may want to use this approach if you are trying to obtain a variable's value before the execution of a certain code cell. To do so, simply replace the "-1" index with the code cell index you are trying to intercept the variable at. 

The above also works to get functions from the notebook, although this has not been tested extensively.

Parsing Notebook `NbResult` Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each code cell's information is represented as a dictionary in the list, and the list will contain the cell info in the order of cells executed.

As such, an NbResult object may look like the following:


.. code-block:: python
    
   [
        {
            'cell_idx': 0,
            'code': 'x=10\\nx',
            'state': {
                'x': 10
            },
            'stdout': '',
            'result': 10
        },
        {
            'cell_idx': 1,
            'code': 'y=20',
            'state': {
                'x': 10,
                'y': 20
            },
            'stdout': '',
            'result': None
        },
        ...
   ]

Variables, functions, objects, and logs from any point in the notebook are accessible through entries in this list.

Parsing Pipeline `PlResult` Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each step's information is represented as a dictionary in the list, and the list will contain the pipeline step's info in the order of steps executed.

A PlResult object may look like:


.. code-block:: python

    [
        {
            'step_idx': 0,
            'step_type': 'notebook',
            'file': 'ExampleNotebookI.ipynb',
            'result': {
                'df': <Some Data>
            }
        },
        {
            'step_idx': 1,
            'step_type': 'transform',
            'file': None,
            'result': {
                'df_processed': <Processed Data>
            }
        }
    ]

Any variable names that should be made available in any given step's result must be specified by a list passed to the `carry_vars` parameter of that step. This informs the pipeline what variables to carry over to the next step. This is described further in the `multinb` documentation.