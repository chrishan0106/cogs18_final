"""Test for League_Bot_Functions. Used to test majority of functions in the program
   Created a function that tests all the test code I developed so you don't have to
   call each test functions. 
"""

from my_module.League_Bot_Functions import *

##Used to test some functions 
compare_string = 'hi,Bread'
compare_list = ['hi,','bread']

def test_string_concatenator():
    """Tests string_concatenator function in few cases"""
    assert string_concatenator('hi','Bread',',') == compare_string 
    assert isinstance(string_concatenator('hi','Bread',','),str)
    assert callable(string_concatenator)
    
def test_prepare_text():
    """Tests prepare_text function in few cases"""
    assert ['hi,bread'] == prepare_text(compare_string)  
    assert isinstance(prepare_text(compare_string),list)
    assert callable(prepare_text)
    
def test_list_to_string():
    """Tests list_to_string function in few cases"""
    assert list_to_string(prepare_text(compare_string),'') == compare_string.lower()
    assert isinstance(list_to_string(prepare_text(compare_string),''),str)
    assert callable(list_to_string)
    
def test_end_chat():
    """Tests end_chat function in few cases"""
    assert end_chat(compare_list) == False
    assert isinstance(end_chat(compare_list),bool)
    assert callable(end_chat)
    
def test_is_in_list():
    """Tests is_in_list function in few cases"""
    assert is_in_list([1,2],[1,2,3,4,5]) == True
    assert isinstance(is_in_list([1,2],[1,2,3,4,5]),bool)
    assert callable(is_in_list)
    
def test_is_List():
    """Tests string_concatenator function in few cases"""
    assert is_List(['list']) == True 
    assert isinstance(is_List(['list']),bool)
    assert callable(is_List)
    
def test_is_Role_Kind():
    """Tests is_Role_Kind function in few cases"""
    assert is_Role_Kind(['mid']) == True
    assert is_Role_Kind(['mid and support']) == True 
    assert isinstance(is_Role_Kind(['mid and support']) ,bool)
    assert callable(is_Role_Kind)
    
def test_is_Role():
    """Tests is_Role function in few cases"""
    assert is_Role(['no']) == False
    assert isinstance(is_Role(['no']),bool)
    assert callable(is_Role)
    
def test_is_More():
    """Tests is_More function in few cases"""
    assert is_More(['hoho']) == False 
    assert isinstance(is_More(['hoho']),bool)
    assert callable(is_More)
    
def test_is_No_More():
    """Tests is_No_More function in few cases"""
    assert is_No_More(['no']) == True
    assert isinstance(is_No_More(['no']),bool)
    assert callable(is_No_More)
    
def test_is_Classes():
    """Tests is_Classes function in few cases"""
    assert is_Classes(['classes']) == True
    assert isinstance(is_Classes(['classes']),bool)
    assert callable(is_Classes)
    
def test_is_Classes_Kind():
    """Tests string_concatenator function in few cases"""
    assert is_Classes_Kind(['burst']) == True
    assert isinstance(is_Classes_Kind(['burst']),bool)
    assert callable(is_Classes_Kind)
    
def test_is_Characters():
    """Tests is_Characters function in few cases"""
    assert is_Characters(['nope']) == False 
    assert isinstance(is_Characters(['nope']),bool)
    assert callable(is_Characters)
    
def test_is_Back():
    """Tests is_Back function in few cases"""
    assert is_Back(['Back']) == True
    assert isinstance(is_Back(['Back']),bool)
    assert callable(is_Back)
    
def test_dict_of_dict():
    """Tests dict_of_dict function in few cases"""
    diction ={}
    diction = dict_of_dict()
    assert isinstance(diction,dict)
    assert callable(dict_of_dict)
    
def test_kind_of_classes():
    """Tests kind_of_classes function in few cases"""
    string = ''
    string = kind_of_classes()
    assert isinstance(string,str)
    assert callable(kind_of_classes)
    
def test_key_of_dicts():
    """Tests key_of_dicts function in few cases"""
    keys = []
    keys = key_of_dicts()
    assert isinstance (keys,list)
    assert callable(key_of_dicts)
    
def test_get_role():
    """Tests get_role function in few cases"""
    assert get_role(['ANIVIA']) == 'Mid' 
    assert isinstance(get_role(['ANIVIA']),str)
    assert callable(get_role)
    
def test_get_classes():
    """Tests get_classes function in few cases"""
    assert get_classes(['lux']) == 'burst'
    assert isinstance(get_classes(['lux']),str)
    assert callable(get_classes)
    
def test_get_characters_role():
    """Tests get_characters_role function in few cases"""
    assert get_characters_role(['Top and Mid']) == 'Jayce, Akali, Viktor, Irelia, Aatrox, Yasuo'
    assert isinstance(get_characters_role(['Top and Mid']),str)
    assert callable(get_characters_role)
    
def test_get_characters_classes():
    """Tests get_characters_classes function in few cases"""
    assert get_characters_classes(['Catcher']) == 'Ivern, Bard, Blitzcrank, Rakan, Neeko, Morgana, Thresh, Zyra'
    assert isinstance(get_characters_classes(['Catcher']),str)
    assert callable(get_characters_classes)
    
def test_all():
    """Tests all the testers I created at once."""
    test_string_concatenator()
    test_prepare_text()
    test_list_to_string()
    test_end_chat()
    test_is_in_list()
    test_is_List()
    test_is_Role_Kind()
    test_is_Role()
    test_is_More()
    test_is_No_More()
    test_is_Classes()
    test_is_Classes_Kind()
    test_is_Characters()
    test_is_Back()
    test_dict_of_dict()
    test_kind_of_classes()
    test_key_of_dicts()
    test_get_role()
    test_get_classes()
    test_get_characters_role()
    test_get_characters_classes()