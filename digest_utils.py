import ast


def strpdict(string: str) -> dict:
    """Parses a dictionary from string

    Args:
        string (str): _description_

    Returns:
        dict: _description_
    """
    try:
        return ast.literal_eval(string)
    except Exception as e:
        # No need for proper logging
        print(e)
        return None
