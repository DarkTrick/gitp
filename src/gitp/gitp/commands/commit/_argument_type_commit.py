
def argument_type_commit(value):
    """
    Describes the type for specifying a commit

        1) "last"
        2) a number
        3) a commit id
    """
    if value == "last":
        return "HEAD~1"
    try:
        number = int(value)
        if number > 0:
            return "HEAD~" + str(number)
    except ValueError:
        pass

    # If the input does not match above, consider it
    # an arbitrary string ( = commit ID)
    return value