'''
Douglas Huynh

Implementation of ADT: Graph

Nodes (vertices) connected through links (edges).

'''

class Graph:

	def __init__(self):
		self.nodes = dict()
		self.edges = dict()

	class NodeInfo:
		'''Store set of incoming and outgoing edges for each node'''
		def __init__(self):
			self.in_edges = set()
			self.out_edges = set()

	def add_node(self, node):
		if not self.has_node(node):
			self.nodes[node] = Graph.NodeInfo()

	def add_edge(self, edge, value):
		_to, _from = edge[0], edge[1]
		self.add_node(_to)
		self.add_node(_from)

		self.edges[edge] = value
		self.nodes[_to].out_edges.add(edge)
		self.nodes[_from].in_edges.add(edge)

	def remove_node(self, node):
		if not self.has_node(node):
			return

		del_node = self.nodes[node]

		for e in tuple(del_nodes.in_edges):
			self.remove_edge(e)

		for e in tuple(del_nodes.out_edges):
			self.remove_edge(e)

		del self.nodes[node]

	def remove_edge(self, edge):
		_to, _from = edge[0], edge[1]

		if not self.has_edge(edge):
			return

		del self.edges[edge]
		self.nodes[_to].out_edges.remove(e)
		self.nodes[_from].in_edges.remove(e)

	def clear(self):
		self.nodes = dict()
		self.edges = dict()

	def node_count(self):
		return len(self.nodes)

	def edge_count(self):
		return len(self.edges)

	def is_empty(self):
		return self.node_count() == 0

	def has_node(self, n):
		return n in self.nodes

	def has_edge(self, e):
		return e in self.edges

	def edge_value(self, e):
		return self.edges[e]