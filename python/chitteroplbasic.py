import json
# import sys


# opl interpreter
import oplbasic as opl

# html parsing stuff
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup



import twinepassage



class ChitterOPLNode:
 def __init__(self, na, ph):
  self.name = na
  self.phrase = ph
  self.edge_0 = "noedge" # working to remove
  self.edge_1 = "noedge" # working to remove
  self.edge_2 = "noedge" # working to remove
  self.edge_3 = "noedge" # working to remove
  self.edge_4 = "noedge" # working to remove
  self.connects = {'a':'noedge','b':'noedge','c':'noedge','d':'noedge','e':'noedge'}  # this is to replace the .edit_# nomenclature
  
 def print_me(self):
  print(self.name)
  print(self.phrase)
  print(self.edge_0) # working to remove
  print(self.edge_1) # working to remove
  print(self.edge_2) # working to remove
  #print(self.edge_3) # working to remove
  #print(self.edge_4) # working to remove
  print(self.connects['a'])
  print(self.connects['b'])
  print(self.connects['c'])
  print(self.connects['d'])
  print(self.connects['e'])
  
 #utility for writing to json
 def make_dictionary(self):
  ret = {}
  ret['name'] = self.name
  ret['phrase'] = self.phrase
  ret['edge_0'] = self.edge_0 # working to remove
  ret['edge_1'] = self.edge_1 # working to remove
  ret['edge_2'] = self.edge_2 # working to remove
  ret['connects_a'] = self.connects['a']
  ret['connects_b'] = self.connects['b']
  ret['connects_c'] = self.connects['c']
  ret['connects_d'] = self.connects['d']
  ret['connects_e'] = self.connects['e']
  
  return ret
  
  
  
class ChitterOPLEdge:
 def __init__(self, na, ph):
  self.name = na
  self.phrase = ph
  self.next_node = "nonode"
    
 def print_me(self):
  print(self.name)
  print(self.phrase)
  print(self.next_node)

 #utility for writing to json
 def make_dictionary(self):
  ret = {}
  ret['name'] = self.name
  ret['phrase'] = self.phrase
  ret['next_node'] = self.next_node
  
  return ret
  
  
  
  #node table, and edge table
class ChitterOPLGraph:
 def __init__(self, na):
  self.name = na
  self.nodes = {}
  self.edges = {}
  self.first_node_name = "Prelude001" # This is rule
  self.current_node = ""
  self.character_lines = "" # character is internal character to this graph
  self.character_mood = "" # mood hinting to send to the presentation layers / character engines
  self.player_options = ""
  self.player_lines = "" 
  self.player_input = "" # player is external character to this graph
  self.is_chat_over = True
  self.is_waiting = False
  self.oplInt = {}
  # self.luaVM = LuaRuntime(unpack_returned_tuples=True)
  # utility function in OPL
  self.jsonPassageFunction = 'FUN jsonPassage(l,e,o) -> "{\'lines\': \'" + l + "\', \'emote\':\'" + e + "\', \'options\':\'" + o + "\'}"'
  self.jsonEdgeFunction = 'FUN jsonEdge(l,e) -> "{\'lines\': \'" + l + "\', \'emote\':\'" + e + "\'}"'
  result, error = opl.run('<stdin>', self.jsonPassageFunction)
  result, error = opl.run('<stdin>', self.jsonEdgeFunction)
  
  
 def turn(self):
  
  if( not( self.is_chat_over ) ):
  
   if( not( self.is_waiting) ):
        self.visit_current_node()
    
 def process_input(self,i):
  if( i == 'reset' ):
   self.reset()
  else: 
   self.player_input = i
   self.process_edges()
  
 def reset(self):
  self.current_node = self.first_node_name
  self.is_chat_over = False
  self.is_waiting = False
  
  self.character_lines = ""
  self.character_mood = ""
  self.player_lines = ""
  self.player_options = ""

    #this creates a ";" delimited string to send across the network to a client playing the game
 def current_message(self):
    message = self.character_lines + ";" + self.character_mood + ";" + self.player_options + ";" + self.player_lines
    return message
    
 def visit_current_node(self):
  self.visit_node(self.current_node)
  
 def visit_node(self,n):
  
  if( not(n == "nonode") ):
   # result, error = opl.run('<stdin>','jsonPassage("This is flippin cool.","happy", "a,b,c,#")') # self.luaVM.execute(self.nodes[n].phrase)
   result, error = opl.run('<stdin>',self.nodes[n].phrase) # self.luaVM.execute(self.nodes[n].phrase)
   sQuotes = str(repr(result.elements[-1]))
   sQuotes = sQuotes[1:-1] # remove outside quotes
   dQuotes= sQuotes.replace("\'","\"")
   vm_return = {}
   vm_return = json.loads(dQuotes)
 
   
   self.character_lines = vm_return['lines'] # for now, the player prompt will be part of the character lines. Seems to make the most sense.
   self.character_mood = vm_return['emote']
   self.player_options = vm_return['options']
      
   self.is_waiting = True
   if(self.nodes[n].edge_0 == 'noedge' and self.nodes[n].edge_1 == 'noedge' and self.nodes[n].edge_2 == 'noedge'):
    self.is_chat_over = True
 
 
 def process_edges(self):
  # working to remove .edge nomenclature
  # temp_edge_0 = self.nodes[self.current_node].edge_0 # working to remove
  # temp_edge_1 = self.nodes[self.current_node].edge_1 # working to remove
  # temp_edge_2 = self.nodes[self.current_node].edge_2 # working to remove
  
  temp_edge_0 = self.nodes[self.current_node].connects['a']
  temp_edge_1 = self.nodes[self.current_node].connects['b']
  temp_edge_2 = self.nodes[self.current_node].connects['c']
  
  
  
  if(not self.is_chat_over):
   if( self.player_input.isdigit() and not(temp_edge_0 == 'noedge') and self.num_option()):
    result, error = sQuotes = opl.run('<stdin>','VAR playerInput = ' + self.player_input) # vm_return = self.luaVM.execute('playerInput = ' + self.player_input)#set user input in the vm
    result, error = sQuotes = opl.run('<stdin>',self.edges[temp_edge_0].phrase) # self.luaVM.execute(self.edges[temp_edge_0].phrase)
    sQuotes = str(repr(result.elements[-1]))
    sQuotes = sQuotes[1:-1] # remove outside quotes
    dQuotes= sQuotes.replace("\'","\"")
    vm_return = {}
    vm_return = json.loads(dQuotes)
    self.player_lines = vm_return['lines']
    self.current_node = self.edges[temp_edge_0].next_node
    self.is_waiting = False
    self.player_input = '' #consume so I only process once
    
   if( self.player_input == 'a' and not(temp_edge_0 == 'noedge') and self.a_option() ):
    #vm_return = self.luaVM.execute('playerInput = "a"')#set user input in the vm
    result, error = opl.run('<stdin>',self.edges[temp_edge_0].phrase) # self.luaVM.execute(self.edges[temp_edge_0].phrase)
    sQuotes = str(repr(result.elements[-1]))
    sQuotes = sQuotes[1:-1] # remove outside quotes
    dQuotes= sQuotes.replace("\'","\"")
    vm_return = {}
    vm_return = json.loads(dQuotes)
    self.player_lines = vm_return['lines']
    self.current_node = self.edges[temp_edge_0].next_node
    self.is_waiting = False
    self.player_input = '' #consume so I only process once
    
   if( self.player_input == 'b' and not(temp_edge_1 == 'noedge')  and self.b_option()):
    #vm_return = self.luaVM.execute('playerInput = "b"')#set user input in the vm
    result, error = opl.run('<stdin>',self.edges[temp_edge_1].phrase) # self.luaVM.execute(self.edges[temp_edge_1].phrase)
    sQuotes = str(repr(result.elements[-1]))
    sQuotes = sQuotes[1:-1] # remove outside quotes
    dQuotes= sQuotes.replace("\'","\"")
    vm_return = {}
    vm_return = json.loads(dQuotes)
    self.player_lines = vm_return['lines']
    self.current_node = self.edges[temp_edge_1].next_node
    self.is_waiting = False
    self.player_input = '' #consume so I only process once
    
   if( self.player_input == 'c' and not(temp_edge_2 == 'noedge') and self.c_option() ):
    #vm_return = self.luaVM.execute('playerInput = "c"')#set user input in the vm
    result, error = opl.run('<stdin>',self.edges[temp_edge_2].phrase) # self.luaVM.execute(self.edges[temp_edge_2].phrase)
    sQuotes = str(repr(result.elements[-1]))
    sQuotes = sQuotes[1:-1] # remove outside quotes
    dQuotes= sQuotes.replace("\'","\"")
    vm_return = {}
    vm_return = json.loads(dQuotes)
    self.player_lines = vm_return['lines']
    self.current_node = self.edges[temp_edge_2].next_node
    self.is_waiting = False
    self.player_input = '' #consume so I only process once
  

 def num_option(self):
  return (self.player_options.find('#') > -1)
  
 def a_option(self):
  return (self.player_options.find('a') > -1)
  
 def b_option(self):
  return (self.player_options.find('b') > -1)
  
 def c_option(self):
  return (self.player_options.find('c') > -1)
  
 def d_option(self):
  return (self.player_options.find('d') > -1)
  
 def e_option(self):
  return (self.player_options.find('e') > -1)
 
  
 def save_json(self,file_name):
    file_dict = {}
 
    node_list = []
    edge_list = []
    
   
    for n,m in self.nodes.items():
        node_list.append(self.nodes[n].make_dictionary())
   
    for n,m in self.edges.items():
        edge_list.append(self.edges[n].make_dictionary())
    
    
    file_dict['nodes'] = node_list
    file_dict['edges'] = edge_list
    
    file_handle = open(file_name,'w') 
    file_text = json.dumps(file_dict,indent=2)
    file_handle.write(file_text)
    file_handle.close()
    file_dict.clear()
 

#this one doesn't work with Unity 
 def save_json_0(self, file_name):
  file_dict = {}
  
  #temporary un-classed dictionaries
  node_dict = {}
  edge_dict = {}
  
  for n,m in self.nodes.items():
   node_dict[n] = self.nodes[n].make_dictionary()
   
  for n,m in self.edges.items():
   edge_dict[n] = self.edges[n].make_dictionary()
    
  file_dict['nodes'] = node_dict
  file_dict['edges'] = edge_dict

  file_handle = open(file_name,'w') 
  file_text = json.dumps(file_dict,indent=2)
  file_handle.write(file_text)
  file_handle.close()
  file_dict.clear()
   
 def load_twine_file(self,file_name):
  file = open(file_name,"r")
  file_text = file.read()
  page_content = BeautifulSoup(file_text, "html.parser")
  paragraphs = page_content.find_all("tw-passagedata")
  vm = twinepassage.TwinePassageScanner()
  #loop thru paragraphs and grab all from html file
  for pg in range(0,len(paragraphs)): 
   vm.scan_passage(paragraphs[pg]['name'],paragraphs[pg].text)
   self.nodes[vm.node_name] = ChitterOPLNode(vm.node_name,vm.node_phrase)
   #iterate thru vm edges and populate self.edges and edge keys in current node
   #stopping at 3 for now, I might redu this to make it a list
   if(len(vm.edge_phrases) >= 1):
    self.nodes[vm.node_name].edge_0 = vm.node_name + '_0' # working to remove
    self.nodes[vm.node_name].connects['a'] = vm.node_name + '_0'
    self.edges[vm.node_name + '_0'] = ChitterOPLEdge(vm.node_name + '_0',vm.edge_phrases[vm.node_name + '_0'])
    self.edges[vm.node_name + '_0'].next_node = vm.edge_next_nodes[vm.node_name + '_0']
   if(len(vm.edge_phrases) >= 2):
    self.nodes[vm.node_name].edge_1 = vm.node_name + '_1' # working to remove
    self.nodes[vm.node_name].connects['b'] = vm.node_name + '_1'
    self.edges[vm.node_name + '_1'] = ChitterOPLEdge(vm.node_name + '_1',vm.edge_phrases[vm.node_name + '_1'])
    self.edges[vm.node_name + '_1'].next_node = vm.edge_next_nodes[vm.node_name + '_1']
   if(len(vm.edge_phrases) >= 3):
    self.nodes[vm.node_name].edge_2 = vm.node_name + '_2' # working to remove
    self.nodes[vm.node_name].connects['c'] = vm.node_name + '_2'
    self.edges[vm.node_name + '_2'] = ChitterOPLEdge(vm.node_name + '_2',vm.edge_phrases[vm.node_name + '_2'])
    self.edges[vm.node_name + '_2'].next_node = vm.edge_next_nodes[vm.node_name + '_2']
  
   
 def print_tables(self):
  print('\nnodes\n')
  for x,y in self.nodes.items():
   self.nodes[x].print_me()
  print('\nedges\n')
  for x,y in self.edges.items():
   self.edges[x].print_me()
   
  
#this allows for non text game navigation between NPCs
#game environment will have named NPCs, you pass the name to NPCChitterLuaGraph.
#NPCChitteraOPLGraph looks up the NPC name and sets the current_node to the first node for that NPC  
class NPCChitterOPLGraph(ChitterOPLGraph):

    def __init__(self, na):
        ChitterOPLGraph.__init__(self, na)
        self.npc_table = {} #npc_name,first_node(of_npc)
        self.is_chitting = True
    def leave(self):
        self.reset()    #placing reset here, makes it so you have to leave in order get the turn based thing working right
        self.is_chitting = False
    def talk_to(self,npc):
        if(npc in self.npc_table):
            if(not self.is_chitting):
                self.current_node = self.npc_table[npc]
                self.is_chitting = True
    
    #use this to process game messages(reset), then user_input(leave,talk_to,a,b,c,d,e,#)
    def process_input(self,i):
        if( i == 'reset' ):
            self.reset()
        elif(i in self.npc_table):
            self.talk_to(i)
        elif(i == "leave"):
            print("leaving")
            self.leave()
        
        if(self.is_chitting):
            self.player_input = i
            self.process_edges()
    
    def turn(self):
        if(self.is_chitting):
            ChitterOPLGraph.turn(self)
            
    def convert_npc_table(self):
        ret_set = []
        for k,s in self.npc_table.items():
            ret_set.append({"npc_name":k,"npc_first_node":s})
        return ret_set
        
    def save_json(self,file_name):
        file_dict = {}
     
        node_list = []
        edge_list = []
        npc_list = []
        
        
       
        for n,m in self.nodes.items():
            node_list.append(self.nodes[n].make_dictionary())
       
        for n,m in self.edges.items():
            edge_list.append(self.edges[n].make_dictionary())
        
        npc_list = self.convert_npc_table()
        
        
        file_dict['nodes'] = node_list
        file_dict['edges'] = edge_list
        file_dict['npcs'] = npc_list
        
        file_handle = open(file_name,'w') 
        file_text = json.dumps(file_dict,indent=2)
        file_handle.write(file_text)
        file_handle.close()
        file_dict.clear()
        
        

  
  
  