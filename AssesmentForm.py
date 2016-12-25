

class AssesmentForm(object):
    """
    
    """
    
    def __init__(self):
        pass
    
    def load_from_google(self):
        pass
    
    def add_multiple_choice(self):
        pass
    
    def add_free_response(self):
        pass

    def edit_multiple_choice(self):
        pass

    def edit_free_response(self):
        pass
    
    def make_pdf(self):
        pass
    
    def get_questions(self):
        pass
        
        
class multiple_choice_question(object):
    """
    Class for building and representing multiple choice questions
    """
    
    def __init__(self):
        pass
    
    def add_choice(self,text,correct=False):
        pass
    
    def get_choices(self):
        pass
    
    def edit_choice(self,choice_id,text=None,correct=None):
        pass
    
    def make_image(self):
        pass



class free_response_question(object):
    """
    Class for building and representing free response questions
    """
    
    def __init__(self):
        pass
    
    def add_prompt(self,text,image=None):
        pass
        
    def edit_prompt(self,text,image=None):
        pass

    def make_image(self):
        pass






class AssesmentResult(object):
    """
    
    """
    
    def __init__(self):
        pass
    
    def load_from_excel(self,path):
        pass
    
    def load_from_google(self,path):
        pass
    
    def get_mc_matrix(self):
        pass
    
    
    def get_questions(self):
        pass
    
    
    
    
    
    
    
        