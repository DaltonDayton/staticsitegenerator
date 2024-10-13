from src.htmlnode import HTMLNode


class LeafNode(HTMLNode):
    tag: str | None
    value: str | None
    props: dict[str, str] | None

    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.tag is None:
            return f"{self.value}"
        props = self.props_to_html()
        return f"<{self.tag}{' ' + props if props else ''}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"Tag: {self.tag}, Value: {self.value}, Props: {self.props}"
