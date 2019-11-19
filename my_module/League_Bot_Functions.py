
import string, webbrowser

"""A collection of function for doing my project. Changed few parts from the functions 
   I made for chatbot assignment to use for my project. Created many functions to be used
   for League bot but was not able to differentiate more functions in main chat bot function
   due to using various flags for specific cases. Using class attributes could've make it easier
   Only referenced A3 assignments and searched webbrowser documentation for idea of opening the link
"""

#These are variables I used to save all the league information 
artillery = {'Jayce':'Top and Mid', "Vel'Koz":'Support', 'Xerath':'Mid', 'Ziggs':'Mid'}
assassin = {'Akali':'Top and Mid','Kassadin':'Mid','Katarina':'Mid',"Kha'Zix":'Jungle','Fizz':'Mid','Evelynn':'Jungle','Ekko':'Mid','Shaco':'Jungle','Pyke':'Mid and Support','Noctunre':'Jungle','Talon':'Mid','Zed':'Mid'}
battlemage = {'Malzahar':'Mid','Karthus':'Mid','Cassiopeia':'Mid','Aurelion Sol':'Mid','Anivia':'Mid','Rumble':'Top','Ryze':'Mid','Swain':'Top','Taliyah':'Jungle','Viktor':'Top and Mid','Vladimir':'Mid'}
burst = {'Lux':'Mid and Support','Lissandra':'Mid','LeBlanc':'Mid','Brand':'Mid and Support','Ahri':'Mid','Annie':'Mid','Orianna':'Mid','Veigar':'Mid and Support','Twisted Fate':'Mid','Syndra':'Mid','Zoe':'Mid'}
catcher = {'Ivern':'Jungle','Bard':'Support','Blitzcrank':'Support','Rakan':'Support','Neeko':'Mid and support','Morgana':'Support','Thresh':'Support','Zyra':'Support'}
diver = {'Kled':'Top','Lee Sin':'Jungle','Jarvan IV':'Jungle','Irelia':'Top and Mid','Hecarim':'Jungle','Camille':'Top and Jungle','Elise':'Jungle','Diana':'Mid','Skarner':'Jungle','Renekton':'Top','Rengar':'Top and Jungle',"Rek'Sai":'Jungle','Olaf':'Jungle','Pantheon':'Top','Wukong':'Top and Jungle','Warwick':'Jungle','Vi':'Jungle','Xin Zhao':'Jungle'}
enchanter = {'Lulu':'Support','Janna':'Support','Karma':'Support','Soraka':'Support','Sona':'Support','Nami':'Support','Taric':'Support'}
juggernaut = {'Illaoi':'Top','Aatrox':'Top and Mid','Dr.Mundo':'Top','Darius':'Top','Garen':'Top','Shyvana':'Jungle','Nasus':'Top','Modrekaiser':'Top','Udyr':'Jungle','Urgot':'Top','Trundle':'Jungle','Volibear':'Top and Jungle','Yorick':'Top'}
marksman = {'Lucian':'ADC','Kindred':'Jungle',"Kog'Maw":'ADC',"Kai'Sa":'ADC','Jinx':'ADC','Jhin':'ADC','Kalista':'ADC','Caitlyn':'ADC','Ashe':'ADC','Draven':'ADC','Corki':'Mid and ADC','Ezreal':'ADC','Sivir':'ADC','Miss Fortune':'ADC','Vayne':'ADC','Varus':'ADC','Twitch':'ADC','Tristana':'ADC','Xayah':'ADC'}
skirmisher = {'Master Yi':'Jungle','Kayn':'Jungle','Jax':'Top and Jungle','Fiora':'Top','Riven':'Top','Tryndamere':'Top','Yasuo':'Top and Mid'}
specialist = {'Kennen':'Top','Kayle':'Top','Graves':'Jungle','Heimerdinger':'Top and Support','Azir':'Mid',"Cho'Gath":'Top','Fiddlesticks':'Support','Gangplank':'Top','Gnar':'Top','Singed':'Top','Nidalee':'Jungle','Quinn':'Top','Teemo':'Top','Zilean':'Support'}
vanguard = {'Malphite':'Top and Support','Leona':'Support','Alistar':'Support','Amumu':'Jungle','Gragas':'Jungle','Sion':'Top','Rammus':'Jungle','Sejuani':'Jungle','Nautilus':'Support','Ornn':'Top','Zac':'Jungle'}
warden = {'Braum':'Support','Galio':'Mid','Shen':'Top and Support','Nunu':'Jungle','Poppy':'Top','Tahm Kench':'Support'}
   
#From the A3. ChatBot 
def string_concatenator ( string1, string2, separator):
    """Adds strings together with separator between them
    Parameters
    ----------
    string1: string
        The front string to add 
    string2: string
        The following string to add
    separator: string 
        The string that goes between two strings
    Returns
    -------
    output: string
        Added string of two strings 
    """
    output = string1+separator+string2
    return output

def prepare_text(input_string):
    """Helper method to make the input lower case and split multiple strings
    Got rid of remove_punctuation from org because some inputs need to contain '
    Parameters
    ----------
    input_string: string
        A string that user input 
    Returns
    -------
    out_list: list
        List representation of input after modifying
    """
    out_list = []
    temp_string = ''
    temp_string = input_string.lower()
    out_list = temp_string.split()
    return out_list

def list_to_string (input_list, separator):
    """Helper method to change the list to string with separator between them
    Parameters
    ----------
    input_list: list
        list that contains user input
    separator: string
        A string that goes between each string 
    Returns
    -------
    output: string
        String representation of the list with separator 
    """
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
    return output

def end_chat (input_list):
    """Ends the chat if the input matches 'quit' or 'exit'
    Parameters
    ----------
    input_list: list
        the list that contains user input
    Returns
    -------
        boolean
    Whether the input was quit or exit or none 
    """
    for item in input_list:
        if item.lower() == 'quit' or item.lower() == 'exit':
            return True
        else: 
            return False
        
def is_in_list(list_one, list_two):
    """ Check if any element of list_one is in list_two.
    Parameters
    ----------
    list_one: list 
        List to check if its inside the two
    list_two: list
        List to see if one belongs inside 
        
    Returns
    -------
            boolean
        Boolean whether list_one exists or not 
    """
    for element in list_one:
        if element in list_two:
            return True
    return False

#Functions I developed to create League Bot functions
def start():
    """ Used to Print Starting message for league bot"""
    print("Welcome to Summoner's Rift")
    print("What do you want to know? Choose between Role, Classes, or Characters")
    print("You may type 'link' to open the browser with list of characters")
    
def is_List(input_list):
    """ Checks if the input was 'list'
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = ''
    check = list_to_string(input_list,' ')
    if check.lower() == 'list':
            return True
    return False

def is_Role_Kind (input_list):
    """ Checks if the input was a kind of role
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input belongs in one of the roles or not 
    """
    dicts = {}
    dicts = dict_of_dict()
    check = ''
    check = list_to_string(input_list,' ')
    
    #Loop through the dictionary of dictionary to find the value of inner dictionary 
    for ea in dicts.keys():
        for a in dicts[ea]:
            if check.lower() == dicts[ea].get(a).lower():
                return True
    return False 

def is_Role (input_list):
    """ Checks if the input was 'role'
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = ''
    check = list_to_string(input_list,' ')
    if check.lower() == 'role':
        return True
    return False
   
def is_More(input_list):
    """ Checks if the input was 'more'
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = ''
    check = list_to_string(input_list,' ')
    if check.lower() == 'yes':
        return True
    return False

def is_Link(input_list):
    """ Checks if the input was 'link'
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = ''
    check = list_to_string(input_list,' ')
    if check.lower() == 'link':
        return True
    return False

def is_No_More(input_list):
    """ Checks if the input was 'no'
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = ''
    check = list_to_string(input_list,' ')
    if check.lower() == 'no':
        return True
    return False

def is_Classes (input_list):
    """ Checks if the input was 'classes'
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = ''
    check = list_to_string(input_list,' ')
    if check.lower() == 'classes':
        return True
    return False

def is_Classes_Kind (input_list):
    """ Checks if the input was one of the classes 
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is one of the classes or not
    """
    dicts = {}
    dicts = dict_of_dict()
    check = ''
    check = list_to_string(input_list,' ')
    #Checks the key of outer dictionary and return True if it matches input
    for ea in dicts.keys():
        if ea.lower() == check.lower():
            return True
    return False
            
def is_Characters (input_list):
    """ Checks if the input was 'characters'
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = ''
    check = list_to_string(input_list,' ')
    if check.lower() == 'characters':
        return True
    return False

def is_Back (input_list):
    """ Checks if the input was 'back'
    Parameters
    ----------
    input_list: list 
        List that contains user input
        
    Returns
    -------
            boolean
        Boolean whether input is as expected or not.
    """
    check = ''
    check = list_to_string(input_list,' ')
    if check.lower() == 'back':
        return True
    return False 

def dict_of_dict():
    """Creates a dictionary of all classes dictionary
    Returns
    -------
    list_Dict: dictionary 
        dictionary that contains a dictionary of all classes dictionary 
    """
    list_Dict = {}
    list_Dict.update({'artillery':artillery})
    list_Dict.update({'assassin':assassin})
    list_Dict.update({'battlemage':battlemage})
    list_Dict.update({'burst':burst})
    list_Dict.update({'catcher':catcher})
    list_Dict.update({'diver':diver})
    list_Dict.update({'enchanter':enchanter})
    list_Dict.update({'juggernaut':juggernaut})
    list_Dict.update({'marksman':marksman})
    list_Dict.update({'skirmisher':skirmisher})
    list_Dict.update({'specialist':specialist})
    list_Dict.update({'vanguard':vanguard})
    list_Dict.update({'warden':warden})
    return list_Dict

def kind_of_classes():
    """Creates a string with all kinds of classes
    Returns
    -------
    classes: string 
        String of all classes 
    """
    diction = dict_of_dict()
    classes = ''
    #Access the name of Classes to return 
    for ea in diction.keys():
        classes = classes + ea +", "
    classes = classes[:-2]
    return classes 

def key_of_dicts():
    """Creates a list with all the champion names
    Returns
    -------
    champions: list
        list with names of all champions 
    """
    champions = []
    diction = dict_of_dict()
    #Loop through the dictionary of dictionary to find the key of inner dictionary 
    for ea in diction.keys():
        for a in diction[ea]:
            champions.append(a)
    return champions 

def get_role(key):
    """Gets the role of specific character
    Parameters
    ----------
    key: list
        list that contains input
    Returns
    -------
    diction[ea].get(a): string
        String that contains role information of character
    """
    diction = dict_of_dict()
    check = ''
    check = list_to_string(key,'')
    #Loop through the dictionary of dictionary to find the key of inner dictionary 
    for ea in diction.keys():
        for a in diction[ea]:
            if a.lower() == check.lower():
                return diction[ea].get(a)
            
def get_classes(key):
    """Gets the class of specific character
    Parameters
    ----------
    key: list
        list that contains input
    Returns
    -------
    ea: string
        String that contains class information of character
    """
    diction = dict_of_dict()
    check = ''
    check = list_to_string(key,'')
    #Loop through the dictionary of dictionary to find the key
    for ea in diction.keys():
        for a in diction[ea]:
            #If key matches the input, return the key of outer dictionary 
            if a.lower() == check.lower():
                return ea
            
def get_characters_role(role):
    """Gets characters that has certain role
    Parameters
    ----------
    key: list
        list that contains input
    Returns
    -------
    characters: string
        String that contains characters name with certain role 
    """
    diction = {}
    diction = dict_of_dict()
    check = ''
    check = list_to_string(role,' ')
    characters=''
    #Used string because there can be multiple characters with same role. 
    for ea in diction:
        for a in diction[ea]:
            #Checks the inner dictionary's value to see if the role matches input 
                if diction[ea].get(a).lower() == check.lower():
                    characters = characters + a + ', '
                    
    #Used to get rid of comma at the end
    characters = characters[:-2]
    return characters

def get_characters_classes(classes):
    """Gets characters that has certain class
    Parameters
    ----------
    key: list
        list that contains input
    Returns
    -------
    characters: string
        String that contains characters name with certain class 
    """
    diction = {}
    diction = dict_of_dict()
    check = ''
    check = list_to_string(classes,'')
    characters=''
    #Used string because there can be multiple characters with same class
    for ea in diction:
        for a in diction[ea]:
            #Checks outer dictionary's key and add the inner dictionary's key if classes match 
            if ea.lower()== check.lower():
                characters = characters + a + ', '
                
    #Removes comma at the end 
    characters = characters[:-2]
    return characters

def activate_chatBot():
    """Main function to run League bot. Due to using flags without making a class, 
    was not able to make more functions that could contain information inside
    all the loops"""
    
    ##Used these to set up the League Bot
    dics=[]
    dics = key_of_dicts()
    dics_Str = list_to_string(dics,' ')
    dics = prepare_text(dics_Str)
    start()
    next_msg='Do you want different information? Type Yes or No'
    
    ##These are all list of flags I used to control the options of League Bot. 
    ##Would've been easier with class variables but wanted to try without using class.
    chat = True
    
    #Theses three are main flags to check whether certain function of the program is supposed to run 
    count = 0
    prompt = False
    flag = 0
    role2 = False
    classes2 = False 
    characters2 = False 
    
    while chat:

        # Get a message from the user
        msg = input('')
        out_msg = None
        msg = prepare_text(msg)
        
        # Check if the input is a 'role'
        role = is_Role(msg)
        # Check if the input is a 'classes'
        classes = is_Classes(msg)
        
        # Check if the input is a 'more'
        more = is_More(msg)
        
        # Check if the input is a 'list'
        menu = is_List(msg)
        
        # Check if the input is a 'back'
        back =is_Back(msg)
        
        # Check if the input is a 'characters'
        character = is_Characters(msg)
        
        # Check if the input is one of the roles
        character_role = is_Role_Kind(msg)
        
        # Check if the input is one of the classes 
        character_class = is_Classes_Kind(msg)
        
        # Check if the input is a 'no'
        nomore = is_No_More(msg)
        
        # Check if the input is a 'link'
        link = is_Link(msg)
        # Prepare the input message
        
        # Check for an end msg 
        
        ##Ends the bot if the user types exit or quit
        if end_chat(msg):
            out_msg = 'See you next time!'
            chat = False
            prompt = False
        ##Opens browser with the list of characters if user types link 
        ##Found the way to implement this by searching on google 'hyperlink string in python'
        ##Used documentation website to learn how to use the open function 
        elif link:
            webbrowser.open('https://na.leagueoflegends.com/en/game-info/champions/')
            prompt = True
            out_msg = 'Refer for future reference!'
            count=1
            flag =1
        
        ##Only runs this elif loop when the input is one of the charcter and after the question. 
        elif  is_in_list(msg,dics) and count is 1:
            
            ##Response with specific role that the character belongs to 
            if role2 is True:
                out_msg = 'The role of '+list_to_string(msg,' ')+' is/are '+ get_role(msg)
                prompt = True 
                role2 = False 
                flag = 1
            
            ##Response with specific class that the character belongs to 
            elif classes2 is True:
                out_msg = 'The class of '+list_to_string(msg,' ')+' is/are '+ get_classes(msg)
                prompt = True 
                classes2 = False 
                flag = 1
        
        ##Shows the list of classes for users so user can know what classes there are. 
        elif menu is True and count is 1:
            out_msg = 'These are the List of Classes: '+kind_of_classes()+". Type 'back' to go back"
            prompt = False
            flag = 0
            
        ##Gives response with the list of characters that belong to the specific role 
        elif character_role is True and count is 1:
            out_msg = 'The characters with '+list_to_string(msg,' ')+' is/are '+get_characters_role(msg)
            prompt = True 
            flag = 1 
            
        ##Gives response with the list of characters that belong to the specific class 
        elif character_class is True and count is 1: 
            out_msg = 'The characters with '+list_to_string(msg,' ')+' is/are '+get_characters_classes(msg)
            prompt = True
            flag = 1
        
        ##Asks user to type the role they want to find characters of. Shows example of input
        elif role is True and count is 0 and characters2 is True:
            out_msg = "Type the role. Type in order from Top to Bottom. There's Top, Jungle, Mid, ADC, and Support EX) Top and Jungle  Jungle and Mid"
            characters2 = False
            prompt = False
            count = 1 
            flag = 0
            
        ##Asks user to type the class they want to find characters of. Back command also pops this question
        elif classes is True and count is 0 and characters2 is True or back is True:
            out_msg = 'Type the class or specific character. If you want to see the list of classes, type list'
            characters2 = False
            back = False 
            prompt = False
            count = 1
            flag = 0
        
        ##Asks which character's role info user wants to know 
        elif role is True and count is 0:
            out_msg = "Which Character's role information are you looking for?"
            role2 = True 
            count = 1
            prompt = False
            flag = 0 
            
        ##Asks which character's class info user wants to know
        elif classes is True and count is 0:
            out_msg = "Which class information are you looking for? Type 'list' if you want to see the list of classes."
            classes2 = True
            count = 1 
            prompt = False
            flag = 0
            
        ##Asks how user wants to find the list of characters 
        elif character is True and count is 0:
            out_msg = "How do you want to find characters? Role or Classes?"
            characters2 = True 
            prompt = False
            flag = 0
            
        ##Prints error statement if input does not match any of the cases so far 
        else:
            out_msg = 'Wrong Input or the feature will be updated in the future' 
            
        ##If user wants more information, ask what kind of information they want 
        if more is True and count is 1 and flag is 1:
                out_msg = 'What do you want to know more? Role or Classes or Characters?' 
                prompt = False
                count = 0
                flag = 0
                
        ##Ends bot if user doesn't want more information         
        elif nomore is True and count is 1 and flag is 1:
            out_msg = 'Fine. Good bye.'
            chat = False 
            prompt = False 
            
        ##Prints the response to user     
        print(out_msg)
        
        ##Only asks if user wants more information if the bot completes answering 
        if prompt is True:
            print(next_msg)