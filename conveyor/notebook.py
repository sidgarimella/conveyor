from packaging import version

from .code_cell import Cell
from .nbresult import NbResult
from .nbglobals import push_globals
from .cell_conductor import *

import os
import sys
import errno
import warnings

import nbformat

SUPPORTED_LANGUAGES = [
    "python"
]

PYTHON_MIN_REQ = "3.5"
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
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(
                    errno.ENOENT), filename)

        try:
            f = open(filename)
            return f
        except IOError:
            print(
                "File " +
                str(filename) +
                " could not be opened for processing.")
            raise

    def __nbconvert(self, fp):
        res = nbformat.read(fp, KNOWN_NBFORMAT)

        # TODO: Raise exceptions
        if res['metadata']['kernelspec']['language'] not in SUPPORTED_LANGUAGES:
            raise ImportError(
                "Languages other than Python are not currently supported.")

        # TODO: Ensure local packages of different version aren't being used to run notebook code
        # User needs same version of python
        if version.parse(res['metadata']['language_info']
                         ['version']) < version.parse(PYTHON_MIN_REQ):
            raise ImportError("Conveyor currently only supports Python " +
                              PYTHON_MIN_REQ +
                              " and above.")

        if int(res['metadata']['language_info']
               ['version'][0]) != sys.version_info[0]:
            warnings.warn("You are trying to run code that is written in Python " +
                          str(res['metadata']['language_info']['version'][0]) +
                          " in Python " + str(sys.version_info[0]) + ". Errors may occur.")

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

    def run(
            self,
            start_cell_idx=None,
            select_cells=None,
            until_variable=None,
            from_state=None,
            import_globals=False):
        """
        Executes notebook code cells.

        :param start_cell_idx: (optional) Index of code cell to begin execution at.
                               Useful for intercepting variables in notebooks for pipelines.
        :param select_cells: (optional) List of indices in order of select code cells to run.
                             By default, all code cells will be run in order.
        :param until_variable: (optional) Name of variable to halt execution once acquired.
                               If variable does not exist, will run all cells.
        :param from_state: (optional) Initialized values before code execution. Used in pipelines.
        :param import_globals: (optional) Set globals from notebook to globals in current workspace.
                           False by default.

        :return: A list of dictionaries containing cell index's, state information, and outputs.
        """

        custom_aggregate = NbResult()
        if from_state:
            self.state = from_state

        if until_variable:
            cell_idx = 0
            if start_cell_idx:
                cell_idx = start_cell_idx

            while until_variable not in self.state and cell_idx < len(
                    self.cells):
                cell_output = run_cell(self, cell_idx)
                custom_aggregate.append(cell_output)
                cell_idx += 1

            if import_globals:
                push_globals(custom_aggregate, result_type=NbResult)

            return custom_aggregate

        elif start_cell_idx:
            cell_idx = start_cell_idx
            while cell_idx < len(self.cells):
                cell_output = run_cell(self, cell_idx)
                custom_aggregate.append(cell_output)
                cell_idx += 1

            if import_globals:
                push_globals(custom_aggregate, result_type=NbResult)

            return custom_aggregate

        elif select_cells:
            for cell_idx in select_cells:
                cell_output = run_cell(self, cell_idx)
                custom_aggregate.append(cell_output)

            if import_globals:
                push_globals(custom_aggregate, result_type=NbResult)

            return custom_aggregate

        aggregate = NbResult(run_all(self, state=from_state))

        if import_globals:
            push_globals(aggregate, result_type=NbResult)

        return aggregate
