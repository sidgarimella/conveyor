from .pipeline_objects import *
from .plresult import *


class Pipeline:
    def __init__(self):
        self.steps = list()
        self._state = {}

    def add_notebook(
            self,
            filename,
            carry_vars,
            select_cells=None,
            start_cell_idx=None,
            until_variable=None):
        self.steps.append(
            NotebookStep(
                filename,
                carry_vars=carry_vars,
                start_cell_idx=start_cell_idx,
                select_cells=select_cells,
                until_variable=until_variable))

    def add_transform(self, l_function):
        self.steps.append(
            TransformStep(l=l_function)
        )

    def run(self):
        pl_aggregate = PlResult()

        step_idx = 0
        for step in self.steps:
            self._state = step.apply(self._state)
            step_type = "notebook"
            if isinstance(step, TransformStep):
                step_type = "transform"
            pl_aggregate.append({
                "step_idx": step_idx,
                "step_type": step_type,
                "file": None if isinstance(step, TransformStep) else step.filename,
                "result": dict(self._state)
            })
            step_idx += 1

        return pl_aggregate
