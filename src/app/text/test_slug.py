from app.text.slug import slugify


def test_slugify() -> None:
    assert slugify("Hello, World!") == "hello-world"
    assert slugify("  --Multiple   spaces--  ") == "multiple-spaces"
    assert slugify("!!!") == ""
