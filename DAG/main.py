class DAG:
  def __init__(self):
    self.graph = {}
    self.nodes = []

  def is_node(self, node):
    return node in self.nodes

  def add_node(self, node):
    print(node)
    if not self.is_node(node):
      self.graph[node] = [[], []]
      self.nodes.append(node[0])

  def add_right_edge(self, from_node, to_node):
    print(from_node)
    print(self.graph)
    if self.is_node(from_node) and self.is_node(to_node):
      self.graph[from_node][1].append(to_node)
    else:
      raise ValueError("One or more nodes not found in the graph.")

  def add_left_edge(self, from_node, to_node):
    print(from_node in self.nodes)
    print(self.graph)
    if self.is_node(from_node) and self.is_node(to_node):
      self.graph[from_node][0].append(to_node)
    else:
      raise ValueError("One or more nodes not found in the graph.")

  def display(self):
    print(self.graph)
    for node in self.graph:
      print(''.join(self.graph[node][0]), '<-', node, "->", ", ".join(self.graph[node][1]))

dag = DAG()

lines = [input("Line "+str(i)+": ") for i in range(int(input("Enter the number of lines: ")))]
for i in lines:
  root = [i.split("=")[0]]
  node = i.split('=')[1]
  root.append(node[1])
  dag.add_node(str(root))
  print(root)
  dag.add_left_edge(root, node[0])
  dag.add_right_edge(root, node[2])

dag.display()
