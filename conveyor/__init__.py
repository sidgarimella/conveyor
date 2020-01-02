from notebook import Notebook


def run_notebook(filename):
    nb = Notebook(filename)
    nb.run()
