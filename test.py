import conveyor

import pprint
import matplotlib.pyplot as plt

results = conveyor.run_notebook("conveyor/examples/Sample Calculations I.ipynb")

# Object test
#fig = results[5]['state']['fig']
#plt.show()

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(results[7])

# Function test
# print(results[-1]['state']['sum_three'](2, 3, 4))