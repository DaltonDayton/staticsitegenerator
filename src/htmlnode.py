class HTMLNode:
    tag: str | None
    value: str | None
    children: list["HTMLNode"] | None
    props: dict[str, str] | None

    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        if not isinstance(tag, str) and tag is not None:
            raise TypeError("Tag must be a string or None")
        if not isinstance(value, str) and value is not None:
            raise TypeError("Value must be a string or None")
        if not isinstance(children, list) and children is not None:
            raise TypeError("Children must be a list or None")
        if not isinstance(props, dict) and props is not None:
            raise TypeError("Props must be a dictionary or None")

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        html = ""
        for prop in self.props:
            html = f'{html}{prop}="{self.props[prop]}" '
        return html.rstrip(" ")

    def __repr__(self) -> str:
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"
