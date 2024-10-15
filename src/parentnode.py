from src.htmlnode import HTMLNode


class ParentNode(HTMLNode):
    tag: str | None
    children: list["HTMLNode"] | None
    props: dict[str, str] | None

    def __init__(
        self,
        tag: str | None,
        children: list["HTMLNode"] | None,
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        childstr = ""
        for child in self.children:
            childstr += child.to_html()
        props = self.props_to_html()
        return f"<{self.tag}{' ' + props if props else ''}>{childstr}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
