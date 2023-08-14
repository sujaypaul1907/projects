#Firstly - pip install pywhatkit
'''
Method 01:
import pywhatkit as pyw

pyw.image_to_ascii_art('C:/Python3/Python_Code/Images/goku.jpg', 'ascii.txt')

#image_to_ascii_art('<image located with extension>','ascii file name with txt extension')

'''
#Method 02:

from ascii_magic import AsciiArt, from_image

output = AsciiArt.from_image('C:/Python3/Python_Code/Images/goku.jpg')

output.to_terminal()

#output.to_html_file('ascii_art.html', columns=500, width_ratio = 2)

