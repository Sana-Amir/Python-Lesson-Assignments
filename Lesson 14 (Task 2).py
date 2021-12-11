def stop_words(words):
    def inner(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            for word in words:
                result = result.replace(word, "*")

            return result
        return wrapper
    return inner


@stop_words(["SFI", "Python"])
def create_slogan(name):
    return f"{name} is studying SFI and Python!"


print(create_slogan("Anna"))