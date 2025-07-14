def html_tag(tag_name):
    def decorator_func(func):
        def wrapper():
            return f"<{tag_name}>{func()}</{tag_name}>"
        return wrapper
    return decorator_func

a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'hello, world!'

print(hello())
