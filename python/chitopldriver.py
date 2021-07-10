
import sys

# sys.path.append('c:\\python\\')
import chitteroplbasic as chitter


theGame = chitter.ChitterOPLGraph('conv01');

theGame.load_twine_file('chitteropl04.html')

# conv.print_tables()
# conv.save_json("chitteropl04.json")


theGame.reset()

while True:#set to True to play
     
    #process game requests
    theGame.turn()

    #display gamestate
    print(theGame.current_message())
    
    #process player input
    user_input = input()
    theGame.process_input(user_input)

    
    
    
    
    
    
    
    
    
    
    