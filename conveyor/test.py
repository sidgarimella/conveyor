from notebook import Notebook

nb = Notebook("examples/Sample Calculations I.ipynb")

for ccell in nb.CodeCells:
    print(ccell)