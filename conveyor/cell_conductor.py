from cStringIO import StringIO

import notebook

import sys


def start(nb):
    for cell_idx in range(len(nb.CodeCells)):
        print(nb.CodeCells[cell_idx].source)
        execute_cell_sequential(nb, cell_idx)
        print(nb.CodeCells[cell_idx].output)

    print("Final state:")
    print(nb.state)


def execute_cell_sequential(nb, idx):
    prior_state = None
    if idx == 0:
        # empty on first run, but has memory from prior runs otherwise
        prior_state = nb.state
    else:
        prior_state = nb.CodeCells[idx - 1].state

    safe_exec(nb, idx, prior_state)

    # nb.state should always track the most recent state
    # helpful if user wants to run non-adjacent cells or make future runs
    nb.state = nb.CodeCells[idx].state


def safe_exec(nb, idx, prior_state):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()

    exec(nb.CodeCells[idx].source, globals(), prior_state)
    nb.CodeCells[idx].state = prior_state

    sys.stdout = old_stdout
    cell_stdout = redirected_output.getvalue()

    nb.CodeCells[idx].output['stdout'] = cell_stdout
    nb.CodeCells[idx].output['result'] = None

    if len(nb.CodeCells[idx].source.strip()) == 0:
        return

    # if last line of cell source is a variable, use the variable value as the
    # cell result
    if nb.CodeCells[idx].source.splitlines()[-1] in nb.CodeCells[idx].state:
        nb.CodeCells[idx].output['result'] = nb.CodeCells[idx].state[nb.CodeCells[idx].source.splitlines()[-1]]

    # TODO: if the last line contains a primitive value that is not set to a
    # variable, track as cell result
