import re

from applications.user.models import User


class Validate:

    
    def __init__(self, dni, email):
        
        self.dni = dni
        self.email = email
    
    def checkDNI(self):

        for u in User.objects.all():

            if u.dni == self.dni:

                return True

            else:

                return False

    def lenghtDNI(self):

        if len(self.dni) is 8:

            return True
        
        else:
            return False
    
    def VerifyEmail(self):

        emailRegularEx = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

        return re.match(emailRegularEx, self.email) is not None

    def CheckEmail(self):

        for e in User.objects.all():

            if e.email == self.email:

                return True
            
            else:

                return False