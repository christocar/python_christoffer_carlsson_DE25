from numbers import Number

def validate_positive_number(value) -> None:
    if not isinstance(value, Number):
        raise TypeError(f"Value must be a number, not a {type(value)}")
    
    if value < 0:
        raise ValueError("Value must be non-negative")