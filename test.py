import conveyor

import pprint

# Single notebook 
results = conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb")

# Notebook-in-notebook cross directory test
# results = conveyor.run_notebook("conveyor/examples/Sample Calculations II.ipynb")

# Final state check
#print(results[-1]['state'])

# Verify all
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(results)

# Object test
# fig = results[5]['state']['fig']
# plt.show()

# Function test
# print(results[-1]['state']['sum_three'](2, 3, 4))