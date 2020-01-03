Running a notebook
==================

There's only one function used to run individual notebooks, but there are several options you can use to control a notebook's execution.


.. function:: run_notebook(filename, start_cell_idx=None, select_cells=None, until_variable=None, from_state=None, import_globals=False)

   Executes code cells of a Jupyter notebook.

   :param filename: Name or path to Jupyter notebook file.
   :param start_cell_idx: (optional) Index of code cell to begin execution at. Useful for intercepting variables in notebooks for pipelines.
   :param select_cells: (optional) List of indices in order of select code cells to run. By default, all code cells will be run in order.
   :param until_variable: (optional) Name of variable to halt execution once acquired. If variable does not exist, will run all cells.
   :param from_state: (optional) Initialized values before code execution. Used in pipelines.
   :param import_globals: (optional) Make globals from notebook available in nbglobals. False by default. 
   :rtype: NbResult object containing a list of cell states and results. For more information, see the section on Output.

There are a couple important caveats when using this that are important to keep in mind:

* **run_notebook** does not evaluate code on a Jupyter server. This means that Conveyor will instead try running the code it finds inside the Jupyter notebook using the version of Python active in your context, making it possible for run_notebook to attempt to execute Python 3.X code with Python 2.X (and vice-versa). Check to make sure you are running the same version of Python as the notebook code. 
* `until_variable` tells Conveyor to stop running the notebook the first time a cell completes with a definition of the specified variable name
