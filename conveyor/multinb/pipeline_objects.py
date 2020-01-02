from .. import run_notebook


class NotebookStep:
    def __init__(
            self,
            filename,
            carry_vars,
            start_cell_idx=None,
            select_cells=None,
            until_variable=None):
        self.filename = filename
        self.carry_vars = carry_vars
        self.start_cell_idx = start_cell_idx
        self.select_cells = select_cells
        self.until_variable = until_variable
        self.to_state = None

    def apply(self, from_state):
        results = run_notebook(
            self.filename,
            start_cell_idx=self.start_cell_idx,
            select_cells=self.select_cells,
            until_variable=self.until_variable,
            from_state=from_state)

        next_state = dict()
        for var in self.carry_vars:
            if var in results[-1]['state']:
                next_state[var] = results[-1]['state'][var]
            else:
                print("Carry variables must be present in state.")
                return False

        return next_state


class TransformStep:
    def __init__(self, l=None):
        self._l = l
        self.to_state = None

    def apply(self, from_state):
        return self._l(from_state)
