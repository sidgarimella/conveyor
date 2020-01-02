import pprint

import conveyor

conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb", import_globals=True)
from conveyor.globals import x, y, z

print(x)


""" Pipeline test

from conveyor.multinb import Pipeline


data_processing = Pipeline()
data_processing.add_notebook(filename="conveyor/examples/load_data.ipynb", carry_vars=['df'])
data_processing.add_notebook(filename="conveyor/examples/process_data.ipynb", 
    carry_vars=['magic_number'],start_cell_idx=3)

def transform_magic(from_state):
    to_state = dict()
    to_state['transformed_magic_number'] = -1 * from_state['magic_number']
    return to_state

data_processing.add_transform(transform_magic)
results = data_processing.run()

print(results)
"""

# Single notebook 
# results = conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb")

# Notebook-in-notebook cross directory test
# results = conveyor.run_notebook("conveyor/examples/Sample Calculations II.ipynb")

# Final state check
#print(results[-1]['state'])

# Verify all
#pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(results)

# Object test
# fig = results[5]['state']['fig']
# plt.show()

# Function test
# print(results[-1]['state']['sum_three'](2, 3, 4))