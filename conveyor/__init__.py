from func_timeout import func_timeout, FunctionTimedOut

from .notebook import Notebook 
from .nbglobals import *

import os


def run_notebook(filename, start_cell_idx=None, select_cells=None, until_variable=None, from_state=None, import_globals=False, timeout=None):
    """
    Executes notebook code cells from notebook working directory.

    :param start_cell_idx: (optional) Index of code cell to begin execution at.
                           Useful for intercepting variables in notebooks for pipelines.
    :param select_cells: (optional) List of indices in order of select code cells to run. 
                         By default, all code cells will be run in order.
    :param until_variable: (optional) Name of variable to halt execution once acquired. 
                           If variable does not exist, will run all cells.
    :param from_state: (optional) Initialized values before code execution. Used in pipelines.
    :param import_globals: (optional) Set globals from notebook to globals in current workspace.
                           False by default. 
    :param timeout: (optional) Set timeout for notebook execution. If time limit exceeded, results
                    will not be available

    :return: A list of dictionaries containing cell index's, state information, and outputs. 
    """
    nb = Notebook(filename)
    current_wd = os.getcwd()

    os.chdir(os.path.dirname(os.path.abspath(filename)))
    res = None
    if timeout:
        try:
            res = func_timeout(timeout, nb.run, args=(
                        start_cell_idx, 
                        select_cells, 
                        until_variable, 
                        from_state, 
                        import_globals
                    ))
        except FunctionTimedOut:
            raise
    else:
        res = nb.run(start_cell_idx=start_cell_idx, select_cells=select_cells, until_variable=until_variable, 
            from_state=from_state, import_globals=import_globals)
    os.chdir(current_wd)
    return res