import sys # provides various functions, variables use to manipulate diff parts of python environment

def error_message_detail(error, error_detail:sys):
    file_name = exc_tb.tb_frame.f_code.co_filename
    _,_,exc_tb=error_detail.exc_info() # this gives all info on which file exception error occurs
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message
      
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail) # Whenever we're raising custom exception we're inheriting parent exception

    def __str__(self):
        return self.error_message