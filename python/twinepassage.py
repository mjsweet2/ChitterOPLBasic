import time


class TwinePassageScanner:
 def __init__(self):
  self.passage = ""
  self.node_name = ""
  self.node_phrase = ""
  self.edge_names = {}
  self.edge_phrases = {}
  self.edge_next_nodes = {}
  
 def scan_passage(self,n,p):
  self.passage = ''#don't use this for now, I might remove it
  self.node_name = n
  self.edge_names.clear()#don't use this for now, I might remove it
  self.edge_phrases.clear()
  self.edge_next_nodes.clear()
  
  pass1 = p.split('[[')
  self.node_phrase = pass1[0]

  edge_index = 0
  for i in range(1,len(pass1)):
   seperated = pass1[i].split('|')
   self.edge_phrases[self.node_name + '_' + str(edge_index)] = seperated[0]
   self.edge_next_nodes[self.node_name + '_' + str(edge_index)] = seperated[1][:seperated[1].find(']')]
   edge_index+=1
   
   
 def print_me(self):
  print("node_name: " + self.node_name + "\n")
  print("node_phrase: " + self.node_phrase + "\n")
  for x,y in self.edge_phrases.items():
   print("edge_phrase: " + x + " :: " + self.edge_phrases[x] + "\n")
  for x,y in self.edge_next_nodes.items():
   print("edge_next_node: " + x + " :: " + self.edge_next_nodes[x] + "\n")
   

  
  
  
  
  
  
  
  
  