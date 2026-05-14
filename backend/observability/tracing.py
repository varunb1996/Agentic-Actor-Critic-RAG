from langsmith import traceable


@traceable

def traced_execution(fn, *args, **kwargs):

    return fn(*args, **kwargs)
