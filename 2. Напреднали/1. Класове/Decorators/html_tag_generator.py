from functools import wraps


def html_tag_generator(tag, attrs):
    def decorator(function):
        @wraps(function)
        def wrapper(text):
            attr_string = " ".join(f"{k}='{v}'" for k, v in attrs.items())
            text = f"<{tag} {attr_string}>{text}</{tag}>"
            return function(text)
        return wrapper
    return decorator


@html_tag_generator(tag="div", attrs={"class": "container col-s-12", "id": "mydiv"})
def modify_text(text):  # <- `text` has been modified by the decorator!
    print(text)


modify_text("Python")