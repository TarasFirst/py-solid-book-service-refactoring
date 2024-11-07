from app.views import display_obj, print_obj
from app.serializers import choose_type_serializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    results = []

    command_functions = {
        "display": lambda method_type: display_obj(
            obj_to_display=book,
            display_type=method_type,
            content_attr="content"
        ),
        "print": lambda method_type: print_obj(
            obj_to_print=book,
            print_type=method_type,
            content_attr="content",
            title_attr="title"
        ),
        "serialize": lambda method_type: choose_type_serializer(
            book,
            method_type
        )
    }

    for cmd, method_type in commands:
        if cmd in command_functions:
            results.append(command_functions[cmd](method_type))

    return "\n".join(filter(None, results))


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("serialize", "json"), ("display", "reverse")]))
