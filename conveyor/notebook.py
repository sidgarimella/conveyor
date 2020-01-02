from packaging import version

import code_cell
import cell_conductor

import os
import sys
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

        self.CodeCells = list()
        self.__extract_source()


    def __validate(self, filename):
        if not os.path.isfile(filename):
            print("File " + str(filename) + " does not exist or could not be found in the working directory.")
            return False

        try:
            f = open(filename)
            return f
        except IOError:
            print("File " + str(filename) + " could not be opened for processing.")
            return False


    def __nbconvert(self, fp):
        res = nbformat.read(fp, KNOWN_NBFORMAT)

        if res['metadata']['kernelspec']['language'] not in SUPPORTED_LANGUAGES:
            print("Language not supported.")
            return False

        if version.parse(res['metadata']['language_info']['version']) < version.parse(PYTHON_MIN_REQ):
            print("Conveyor currently only supports Python " + PYTHON_MIN_REQ + " and above.")
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
                self.CodeCells.append(code_cell.CodeCell(code_cell_idx, cell['source']))
                code_cell_idx += 1

    def run(self):
        cell_conductor.start(self.CodeCells)


