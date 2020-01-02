from cStringIO import StringIO

import notebook

import sys


def run_all(nb):
    for cell_idx in range(len(nb.cells)):
        execute_cell_sequential(nb, cell_idx)
        print(nb.cells[cell_idx])


def execute_cell_sequential(nb, idx):
    prior_state = None
    if idx == 0:
        # empty on first run, but has memory from prior runs otherwise
        prior_state = nb.state
    else:
        prior_state = nb.cells[idx - 1].state

    safe_exec(nb, idx, prior_state)

    # nb.state should always track the most recent state
    # helpful if user wants to run non-adjacent cells or make future runs
    nb.state = nb.cells[idx].state

# TODO: execute_cell method for running particular cells

def safe_exec(nb, idx, prior_state):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()

    # TODO: preprocess source code to deal with !/% os/kernel commands
    exec(nb.cells[idx].source, globals(), prior_state)
    nb.cells[idx].state = prior_state

    sys.stdout = old_stdout
    cell_stdout = redirected_output.getvalue()

    nb.cells[idx].output['stdout'] = cell_stdout
    nb.cells[idx].output['result'] = None

    if len(nb.cells[idx].source.strip()) == 0:
        return

    # if last line of cell source is a variable, use the variable value as the
    # cell result
    if nb.cells[idx].source.splitlines()[-1] in nb.cells[idx].state:
        nb.cells[idx].output['result'] = nb.cells[idx].state[nb.cells[idx].source.splitlines()[-1]]

    # TODO: if the last line contains a primitive value that is not set to a
    # variable, track as cell result
