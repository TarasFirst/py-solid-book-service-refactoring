def get_type_action(type_action: str, obj_attr: str) -> None:
    if type_action == "console":
        print(obj_attr)
    elif type_action == "reverse":
        print(obj_attr[::-1])
    else:
        raise ValueError(f"Unknown type action: {type_action}")


def get_attr(obj: object) -> dict:
    return obj.__dict__.items()


def display_obj(
        obj_to_display: object,
        display_type: str,
        content_attr: str
) -> None:
    content = getattr(obj_to_display, content_attr)
    try:
        get_type_action(type_action=display_type, obj_attr=content)
    except ValueError as e:
        raise e


def print_obj(
        obj_to_print: object,
        print_type: str,
        title_attr: str,
        content_attr: str
) -> None:
    title = getattr(obj_to_print, title_attr)
    content = getattr(obj_to_print, content_attr)
    name_obj = obj_to_print.__class__.__name__.lower()
    if print_type == "console":
        print(f"Printing the {name_obj}: {title}...")
        get_type_action(type_action=print_type, obj_attr=content)
    elif print_type == "reverse":
        print(f"Printing the {name_obj} in reverse: {title}...")
        get_type_action(type_action=print_type, obj_attr=content)
    else:
        raise ValueError(f"Unknown print type: {print_type}")
