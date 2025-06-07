

class HTMLNode():
	def __init__(self, tag = None, value = None, children = None, props = None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		if self.props == None:
			return ""
		else:
			html = ' '.join(f'{key}="{value}"' for key, value in self.props.items())
			return f" {html}"

	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
	def __init__(self, tag = None, value = None, props = {}):
		super().__init__(tag = tag, value = value, children = None, props = props)

	def to_html(self):
		if not self.value:
			raise ValueError
		elif not self.tag:
			return self.value
		else:
			joined_attributes = ' '.join(f'{key}="{value}"' for key, value in self.props.items())
			return f"<{self.tag}{joined_attributes}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
	def __init__(self, tag, children, value = None, props = {}):
		super().__init__(tag = tag, value = None, children = children, props = props)

	def to_html(self):
		if not self.tag:
			raise ValueError
		elif not self.children:
			raise ValueError("missing 'children'")
		else:
			children_string = ""
			for c in self.children:
				children_string = f"{children_string}{c.to_html()}"
			return f"<{self.tag}>{children_string}</{self.tag}>"
