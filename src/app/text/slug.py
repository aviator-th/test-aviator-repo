import re

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Lowercase ``text`` and join its runs of letters and digits with single
    hyphens, e.g. "Hello, World!" -> "hello-world". Empty when nothing is left."""
    return _NON_ALNUM.sub("-", text.lower()).strip("-")
