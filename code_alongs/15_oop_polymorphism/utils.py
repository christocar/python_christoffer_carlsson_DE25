from numbers import Number

def validate_number(value):
    if not isinstance(value, Number):
        raise TypeError(f"Value must be a number, not {type(value)}")