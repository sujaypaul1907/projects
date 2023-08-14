#Text to handwriting maker

import pywhatkit


txt = "This free online tool converts your PNG images to JPEG format, applying proper compression methods. Unlike other services, this tool does not ask for your email address, offers mass conversion and allows files up to 50 MB"

pywhatkit.text_to_handwriting(txt, save_to="sample1.png")

print("Handwritten notes generated succesfully")



