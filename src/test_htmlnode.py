import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
	def test_prop_none(self):
		node = HTMLNode(None, None, None, None)
		self.assertEqual(node.props_to_html(), "")

	def test_prop_single(self):
		node = HTMLNode(None, None, None, {"href": "https://www.google.com"})
		self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

	def test_prop_multiple(self):
		node = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank"})
		self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

	def test_leaf_to_html(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html2(self):
		node = LeafNode(None, "Hi world >:)")
		self.assertEqual(node.to_html(), "Hi world >:)")

	def test_leaf_to_html3(self):
		node = LeafNode("p", None)
		self.assertRaises(ValueError, node.to_html)

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)

if __name__ == "__main__":
	unittest.main()
