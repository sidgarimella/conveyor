## Conveyor

A set of tools that allow Jupyter notebook cell outputs to be computed and used in other notebooks and scripts. 

#### Use Cases

 - Split ordered steps across multiple notebooks, picking up the most recent state information with each new notebook
 - Prototype and organize workflows entirely in Jupyter notebooks without having to manage script exports
 - Improve performance by reducing overheads from notebook servers and unused code cells

#### Requirements

Conveyor currently only supports Jupyter notebooks written in Python. It is important to ensure that you have the version of Python (and any dependencies) used in your notebooks also installed locally, or on the machine using this library.

#### Examples

For quick and simple access to global variables in a prior notebook:

```python
conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb", import_globals=True)

# all notebook globals pushed to conveyor.globals with import_globals flag
from conveyor.globals import x, y, z

print(y)
```

Conveyor can also provide you with any information available to you in a prior Jupyter workspace. 

```python
results = conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb")

# To get a specific cell's source code
code = results[1]['code']

# To get a specific cell result
fourth_code_cell_result = results[3]['result']
any_code_cell_result = results[<any_code_cell_idx>]['result']

# To get variables available in notebook
x = results[-1]['state']['x']
any_variable = results[-1]['state'][<variable_name>]
```

There are options for running notebooks that can be used to optimize notebook execution, or stitch notebooks together in *pipelines*.

```python
from conveyor.multinb import Pipeline
...
data_processing = Pipeline()
data_processing.add_notebook(filename="conveyor/examples/load_data.ipynb", carry_vars=['df'])
data_processing.add_notebook(filename="conveyor/examples/process_data.ipynb", 
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

This package will be made available on pypi.

#### Documentation



