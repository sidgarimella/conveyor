import conveyor

import pprint
import matplotlib.pyplot as plt

results = conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb")

#print(results[-1]['state'])

# Verify all
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(results)

# Object test
# fig = results[5]['state']['fig']
# plt.show()

# Function test
# print(results[-1]['state']['sum_three'](2, 3, 4))