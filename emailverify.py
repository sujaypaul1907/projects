#Email Verifier

email = input("Enter your email ID: ")
p, q, r = 0, 0, 0

if len(email) >= 6: #g@g.com or g@g.in -- minimum 6 characters
    if email[0].isalpha():  #g@g.in -- starts with alphabet
        if ("@" in email) and (email.count("@")==1): #g@g.in -- only one @ in email id
            if (email[-4]==".") ^ (email[-3]=="."): #g@g.com or g@g.in -- '.' is at 4th or 3rd position from end
                for i in email: 
                    if i.isspace():
                        p = 1          
                    elif i.isalpha():
                        if i == i.upper():
                            q = 1
                    elif i == i.isdigit():
                        continue
                    elif i == "_" or i == "@" or i == ".":
                        continue
                    else:
                        r = 1
                if p == 1 or q == 1 or r == 1:
                    print("Error 05: Your email ID has spaces or upper cases")
                else:
                    print("You entered correct email ID")
            else:
                print("Error 04: Your email extension has multiple '.' or no '.'")
        else:
            print("Error 03: Your email ID has no @ ormultiple @")
    else:
        print("Error 02: Your email ID does not start with an alphabet")
else:
    print("Error 01: Your email ID does not have sufficient characters")