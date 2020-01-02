from packaging import version

from .code_cell import Cell
from .cell_conductor import *

import os
import sys
import nbformat

SUPPORTED_LANGUAGES = [
    "python"
]

PYTHON_MIN_REQ = "2.7"
KNOWN_NBFORMAT = 4


class Notebook:
    def __init__(self, filename):
        self.__filename = filename
        self.__fp = self.__validate(filename)
        self.__NotebookNode = self.__nbconvert(self.__fp)

        self.cells = list()
        self.state = {}

        self.__extract_source()

    def __validate(self, filename):
        if not os.path.isfile(filename):
            print(
                "File " +
                str(filename) +
                " does not exist or could not be found in the working directory.")
            return False

        try:
            f = open(filename)
            return f
        except IOError:
            print(
                "File " +
                str(filename) +
                " could not be opened for processing.")
            return False

    def __nbconvert(self, fp):
        res = nbformat.read(fp, KNOWN_NBFORMAT)

        if res['metadata']['kernelspec']['language'] not in SUPPORTED_LANGUAGES:
            print("Language not supported.")
            return False

        # TODO: Ensure local packages of different version aren't being used to run notebook code
        # User needs same version of python
        if version.parse(res['metadata']['language_info']
                         ['version']) < version.parse(PYTHON_MIN_REQ):
            print(
                "Conveyor currently only supports Python " +
                PYTHON_MIN_REQ +
                " and above.")
            return False

        return res

    def __extract_source(self):
        if not self.__NotebookNode:
            print("No notebook to extract. See nbconvert details.")
            return False

        code_cell_idx = 0
        all_cells = self.__NotebookNode['cells']

        for cell in all_cells:
            if cell['cell_type'] == 'code':
                self.cells.append(
                    Cell(
                        code_cell_idx,
                        cell['source']))
                code_cell_idx += 1

    # TODO: See how this handles compile/runtime errors

    def run(self, select_cells=None, until_variable=None):
        """
        Executes notebook code cells.

        :param select_cells: (optional) List of indices in order of select code cells to run.
                             By default, all code cells will be run in order.
        :param until_variable: Name of variable to halt execution once acquired.
                               If variable does not exist, will run all cells.

        :return: A list of dictionaries containing cell index's, state information, and outputs.
        """

        custom_aggregate = list()

        if until_variable:
            cell_idx = 0
            while until_variable not in self.state and cell_idx < len(
                    self.cells):
                cell_output = run_cell(self, cell_idx)
                custom_aggregate.append(cell_output)
                cell_idx += 1
            return custom_aggregate

        elif select_cells:
            for cell_idx in select_cells:
                cell_output = run_cell(self, cell_idx)
                custom_aggregate.append(cell_output)
            return custom_aggregate

        return run_all(self)
