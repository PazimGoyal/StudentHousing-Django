from django.core.mail import send_mail as mail
def send_mail(name,descript,phone,email,lister_email,url):
    description = """This mail is regarding your ad. on studentHousing.com 
view your ad. here :""" + "http://pazimgoyal.pythonanywhere.com/" + url + """   

""" + "Requested by:- " + name+ "\n" + phone + "\n"+descript + """
You can reply to user using website chatting service or directly reply at """ + email + """   
Thankyou for using StudentHousing.com"""
    send = mail('no-reply - student housing your ad. ', description, email, [lister_email, ])
    return send
