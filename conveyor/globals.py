def push_globals(aggregate_output, result_type):
    final_state_globals = aggregate_output[-1]['state']
    globals().clear()
    for var in final_state_globals:
        # ignore conveyor output of result_type
        if not isinstance(final_state_globals[var], result_type):
            globals()[var] = final_state_globals[var]
            