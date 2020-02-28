## Conveyor
[![Build Status](https://travis-ci.org/sidgarimella/conveyor.svg?branch=master)](https://travis-ci.org/sidgarimella/conveyor)


Compute and use Jupyter notebook cell outputs in other notebooks and scripts with just a couple lines of code.

#### Use Cases

 - Split ordered steps across multiple notebooks, picking up the most recent state information with each new notebook
 - Prototype and organize workflows entirely in Jupyter notebooks without having to manage script exports
 - Improve performance by reducing overheads from notebook servers and unused code cells

#### Requirements

Conveyor currently only supports Jupyter notebooks written in Python. It is important to ensure that you have the version of Python (and any dependencies) used in your notebooks also installed locally, or on the machine using this library.

#### Examples

For quick and simple access to values in a prior notebook:

```python
conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb", import_globals=True)

# all notebook globals pushed to conveyor.nbglobals with import_globals flag
from conveyor.nbglobals import x, y, z, fig

print(y)
```

Conveyor can also provide you with any information available in a prior Jupyter workspace. 

```python
results = conveyor.run_notebook("conveyor/examples/tests/Sample Calculations I.ipynb")

# Cells are zero-indexed, only code cells are counted
code_cell_idx = 1

# Get a cell's source code
code = results[code_cell_idx]['code']

# Get a cell result
cell_result = results[code_cell_idx]['result']

# Get cell stdout
cell_stdout = results[code_cell_idx]['stdout']

# To get any variable available in notebook
x = results.getvar('x')
```

There are options for running notebooks that can be used to optimize notebook execution, or stitch notebooks together in *pipelines*.

```python
from conveyor.multinb import Pipeline
...
data_processing = Pipeline()

# The variable 'df' from load_data.ipynb will replace 'df' in 
# process_data.ipynb, starting from the third code cell.
data_processing.add_notebook(filename="conveyor/examples/tests/load_data.ipynb", carry_vars=['df'])
data_processing.add_notebook(filename="conveyor/examples/tests/process_data.ipynb", 
    carry_vars=['magic_number'], start_cell_idx=3)

# Add custom intermediary steps
def transform_magic(from_state):
    to_state = dict()
    to_state['transformed_magic_number'] = -1 * from_state['magic_number']
    return to_state

data_processing.add_transform(transform_magic)

# Get output of selected variables from each stage
results = data_processing.run()
```

#### Installation

This package is available on pypi. Install it using pip with 

`pip install jupyter-conveyor`

Conveyor is only compatible with Python 3.5 and above.

#### Documentation

See the docs folder, or [read them here](https://conveyor.readthedocs.io/en/latest/).


