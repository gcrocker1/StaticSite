from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
       super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Node must have tag!")
        if self.children is None:
            raise ValueError("Node must have children!")
        ret_str = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            ret_str += child.to_html()
        ret_str += f"</{self.tag}>"
        return ret_str
    