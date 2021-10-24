# THIS PYTHON FILE IS CREATED BY ME - SHIVAYA
# IN VIEWS PYTHON IT WILL CONTAIN ALL THE FUNCTIONS TO BE EXECUTED WHEN THE SPECIFIED END POINTS OF OUR URL
# MEETS, AND IT DECIDES WHICH THING IS TO BE VIEWED TO USER
# WHENEVER WE NEED TO RETURN TEMPLATE WE NEED TO USE THE RENDER FUNCTION ALWAYS REMEMBER
# THE DESIGN OF FRONTEND OF ANY WEBSITE IS DONE WITH THE HELP OF HTML TEMPLATES
from django.http import HttpResponse
from django.shortcuts import render # render function is used for the rendering of the templates
def index(request):
    
    return render(request,"index.html") # render function of django.shortcuts is used to render any type of template
def analyze(request):
    djtext=request.GET.get('text','default') # taking the data of the text area
    removepunc=request.GET.get('removepunc','off') # checking weather on or of
    capitalizeall=request.GET.get('capall','off') # checking weather on or of
    extraspaceremover=request.GET.get('extraspaceremover','off') # checking weather on or of
    newlineremover=request.GET.get('newlineremover','off') # checking weather on or of
    charcounter=request.GET.get('charcounter','off') # checking weather on or of
    spacecounter=request.GET.get('spacecounter','off') # checking weather on or of
    punc='''!()-[]{};:"'\,<>./?@#$%^&*_~'''
     # empty string
    if removepunc=="on": # IF USER HAVE CHECKED THE CHECK BUTTON
        analyzed=""
        for char in djtext:
            if char not in punc: # if the character is not puncuation
                analyzed=analyzed+char # text after removal of punctuation
        if capitalizeall=="on":
            org=""
            for char in analyzed:
                org=org+char.upper()
            remove_punc_dict={"status":"TEXT AFTER REMOVING PUNCTUATIONS AND CAPITALIZING IS BELOW :","original":org}
            return render(request,"removepunctuation.html",remove_punc_dict)
        

        else:    
            remove_punc_dict={"status":"TEXT AFTER REMOVING PUNCTUATIONS IS BELOW :","original":analyzed}
            return render(request,"removepunctuation.html",remove_punc_dict)
    elif capitalizeall=="on": # if client wants to capitalize it's text from website
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        remove_punc_dict={"status":"TEXT AFTER CAPETALIZING IS BELOW :","original":analyzed}
        return render(request,"removepunctuation.html",remove_punc_dict)
    elif extraspaceremover=="on": # if client wants to remove the extra space from the text line in website
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and  djtext[index+1]==" "): # if there is an extra space
                analyzed=analyzed+char
        remove_punc_dict={"status":"TEXT AFTER REMOVING EXTRA SPACES IS BELOW :","original":analyzed}
        return render(request,"removepunctuation.html",remove_punc_dict)
    elif newlineremover=="on": # client wants to remove the newline characters from it's text
        analyzed=""
        for char in djtext:
            if char != '\n':
                analyzed=analyzed+char
        remove_punc_dict={"status":"TEXT AFTER REMOVING THE NEW LINE IS BELOW :","original":analyzed}
        return render(request,"removepunctuation.html",remove_punc_dict)        
    elif charcounter=="on":
        count=0
        for char in djtext:
            if char!=" ": # if the character is not equal to the space
                count+=1
        remove_punc_dict={"status":"NO OF CHARACTERS IN THE TEXT IS GIVEN BELOW :","original":count}
        return render(request,"removepunctuation.html",remove_punc_dict)    
    elif spacecounter=="on":
        count=0
        for char in djtext:
            if char==" ":
                count+=1
        remove_punc_dict={"status":"NO. OF SPACES IN THE TEXT IS GIVEN BELOW :","original":count}
        return render(request,"removepunctuation.html",remove_punc_dict)   

    else: # if user have not checked the check button
        return HttpResponse("AN ERROR OCCURAD ON THIS PAGE")
def about(request):
    my_info={"my_name":"Shivaya","my_class":"BCA"}
    return render(request,"about.html",my_info)

            