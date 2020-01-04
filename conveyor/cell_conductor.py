from io import StringIO

import sys
import copy


def run_all(nb, state=None):
    aggregate = list()
    for cell_idx in range(len(nb.cells)):
        if state:
            execute_cell_sequential_state(nb, cell_idx, state)
        else:
            execute_cell_sequential(nb, cell_idx)

        cell = nb.cells[cell_idx]
        aggregate.append({
            "cell_idx": cell_idx,
            "code": cell.source,
            "state": dict(cell.state),
            "stdout": cell.output["stdout"],
            "result": cell.output["result"]
        })
    return aggregate


def run_cell(nb, idx):
    execute_cell_idx(nb, idx)
    cell = nb.cells[idx]
    return {
        "cell_idx": idx,
        "code": cell.source,
        "state": dict(cell.state),
        "stdout": cell.output["stdout"],
        "result": cell.output["result"]
    }


def execute_cell_sequential_state(nb, idx, state):
    prior_state = None
    if idx == 0:
        prior_state = state
    else:
        prior_state = nb.cells[idx - 1].state

    safe_exec(nb, idx, prior_state)
    nb.state = nb.cells[idx].state


def execute_cell_sequential(nb, idx):
    prior_state = None
    if idx == 0:
        # empty on rerun. should memory remain from consecutive runs?
        prior_state = {}
    else:
        prior_state = nb.cells[idx - 1].state

    safe_exec(nb, idx, prior_state)

    # nb.state should always track the most recent state
    # helpful if user wants to run non-adjacent cells or make future runs
    nb.state = nb.cells[idx].state


def execute_cell_idx(nb, idx):
    prior_state = nb.state
    safe_exec(nb, idx, prior_state)
    nb.state = nb.cells[idx].state

    return idx


def safe_exec(nb, idx, prior_state):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()

    # TODO: preprocess source code to deal with !/% os/kernel commands
    exec(nb.cells[idx].source, prior_state, prior_state)
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
