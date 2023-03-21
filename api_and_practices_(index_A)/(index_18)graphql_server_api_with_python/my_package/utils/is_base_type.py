def is_base_type(obj):
    """
    Returns True if obj is a basic data type, otherwise False.
    """
    return type(obj) in [int, str, bool, float, list, tuple, dict, set]
