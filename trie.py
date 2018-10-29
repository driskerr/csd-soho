class TrieNode:
  def __init__(self, value=None):
    self.children = []
    self.value = value
    
  def __repr__(self):
    return "Node: {}".format(self.value)
  

class Trie:
  def __init__(self):
    self.root = TrieNode()
    
  def add_child(self, child_node):
    self.children.append(child_node)
    
  def insert(self, word):
    current_node = self.root
    for letter in word:
      Letter_Node = TrieNode(letter)
      comparable_Letter = Letter_Node.value
      comparable_children = [node.value for node in current_node.children]
      if comparable_Letter not in comparable_children:
        current_node.children.append(Letter_Node)
        comparable_children = [node.value for node in current_node.children]
      else:
        pass
      current_node = current_node.children[comparable_children.index(comparable_Letter)]
 
  def search(self, search_term):
    searched_node = self.root
    options = ['']
    for letter in search_term:
      search_children = [node.value for node in searched_node.children]
      if letter in search_children:
        options[0] += letter
        searched_node = searched_node.children[search_children.index(letter)]
      else:
        options = []
        return options
    current_node = searched_node
    num_branches = len(current_node.children)
    options = options * num_branches
    for i in range(num_branches):
      branch_node = current_node.children[i]
      num_more_branches = len(branch_node.children)
      while branch_node:
        options[i] += branch_node.value
        if branch_node.children != []:
          branch_node = branch_node.children[0]
        else:
          branch_node = None
    return options

      
      
  
#TESTING
"""
categories = Trie()
categories.insert('french')
categories.insert('chinese')
categories.insert('filipino')
categories.insert('japanese')

#print(categories.search('fi'))
#print(categories.search('c'))
print(categories.search('f'))
print(categories.search('p'))
#print(categories.search('fo'))
print(categories.search('j'))
"""
