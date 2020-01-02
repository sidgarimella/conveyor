from .notebook import Notebook 

import os


def run_notebook(filename, select_cells=None, until_variable=None):
    """
    Executes notebook code cells.

    :param select_cells: (optional) List of indices in order of select code cells to run. 
                         By default, all code cells will be run in order.
    :param until_variable: Name of variable to halt execution once acquired. 
                           If variable does not exist, will run all cells.

    :return: A list of dictionaries containing cell index's, state information, and outputs. 
    """
    nb = Notebook(filename)
    current_wd = os.getcwd()
    
    os.chdir(os.path.dirname(os.path.abspath(filename)))
    res = nb.run(select_cells=select_cells, until_variable=until_variable)
    os.chdir(current_wd)
    return res