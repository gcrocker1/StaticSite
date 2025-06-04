class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
       self.tag = tag
       self.value = value
       self.children = children
       self.props = props

    def to_html(self):  # Child classes will override this
        raise NotImplementedError
    
    def props_to_html(self):
        ret_str = ""
        if self.props is None:
            raise Exception("this node has no props")
        for key, value in self.props.items():
            ret_str += f" {key}={value}"
        return ret_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"