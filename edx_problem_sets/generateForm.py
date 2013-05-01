def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """
    new_story = story
    story_list = new_story.split(' ')
    count = 0
    
    for i in story_list:
        if i in listOfAdjs:
            story_list[count] = '[ADJ]'
            count += 1
        elif i in listOfNouns:
            story_list[count] = '[NOUN]'
            count += 1
        elif i in listOfVerbs:
            story_list[count] = '[VERB]'
            count += 1
        else:
            count += 1
    
    long = len(story_list)
    count = 0
    newest_story = ''
    
    for i in story_list:
        if count < (long-1):
            newest_story += (str(i) + ' ')
            count += 1
        else:
            newest_story += str(i)
    return newest_story

def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    string_of_words = madLibsForm
    list_of_words = string_of_words.split(' ')
    list_of_madLibstemplates = []
    
    for i in list_of_words:
        if i == '[ADJ]' or i == '[VERB]' or i == '[NOUN]':
            list_of_madLibstemplates.append(str(i))
    return list_of_madLibstemplates

def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    word = userWord
    
    if madTemplate == '[ADJ]':
        return word in listOf Adjs
    elif madTemplate == '[NOUNS]'
        return word in listOfNound
    elif madTemplate == '[VERB]'
        return word in listOfVerbs
