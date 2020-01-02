## Conveyor

A set of tools that allow Jupyter notebook cell outputs to be computed and used in other notebooks and scripts. 

#### Use Cases

 - Split ordered steps across multiple notebooks, picking up the most recent state information with each new notebook
 - Prototype and organize workflows entirely in Jupyter notebooks without having to manage script exports
 - Improve performance by reducing overheads from notebook servers and unused code cells

#### Requirements

Conveyor currently only supports Jupyter notebooks written in Python. It is important to ensure that you have the version of Python (and any dependencies) used in your notebooks also installed locally, or on the machine using this library.

#### Example

```python
import conveyor
...
results = conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb")

# To get variables available at the end of a notebook
x = results[-1]['state']['x']
any_variable = results[-1]['state'][<variable_name>]

# To get a specific cell output
fourth_code_cell_result = results[3]['result']
any_code_cell_result = results[<any_code_cell_idx>]['result']
```

#### Installation

This package will be made available on pypi.

#### Documentation



