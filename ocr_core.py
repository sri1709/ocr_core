import re
import glob
import sys
try:
    from PIL import Image
    from datetime import datetime
except ImportError:
    import Image
import pytesseract

def ocr_core(path):
    """
    This function will handle the core OCR processing of images.
        """
    text = pytesseract.image_to_string(Image.open(path))
    date_format = re.compile(
 r"""\s*  # optional whitespace
 (?:20)?  # century 
 (\d+)    # Month
 [-/]     # separator
 (\d+)    # Day
 [-/]     # separator
 (?:20)?  # century (optional)
 (\d+)    # years (YY)
 \s*      # optional whitespace""",
            re.VERBOSE)
    #date_format = re.compile( r'[A-Z]{1}[12]\d{1}|[12]\d{1}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])_?|(?:0[1-9]|1[0-2])_[12]\d')
    #date_format = re.compile('\d{2}(?P<sep>[-/])\d{2}(?P=sep)\d{2}')
    #date_format = re.compile(r'(\d\d)/(\d\d)/(\d\d)')
    ans = date_format.search(text)
    i=1
    count=1
    for i in range(3):
	if(ans is None):
	     return None
	else:
	    if(i<=3):
    	       return ans.group(i)
               return  '/'
        i=i+1
    #return text
#image1 = open('image/.jpeg')
#s=(ocr_core(image1))
#print(type(image1
#text_file=(ocr_core('image/certificate.jpg'))
#print len(folders)
#text_file = ocr_core(folders)
#print text_file
#date_format = re.compile(r'(\d\d)/(\d\d)/(\d\d)')
#ans = date_format.search(text_file)
#print(text_file)
#print(ans)
folders = glob.glob("image/*.*")
for file in  folders:
    print file
    text_file=ocr_core(file)
    print text_file
