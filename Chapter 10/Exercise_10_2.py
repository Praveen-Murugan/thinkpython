"""
Use capitalize_all to write a function named capitalize_nested that takes
a nested list of strings and returns a new nested list with all strings capitalized

"""


def capitalize_nested(t):
    if isinstance(t, list):
        return [capitalize_nested(s) for s in t]
    else:
        return t.capitalize()

print(capitalize_nested(['this', 'that', ['other','what'],['string','nested']]))
