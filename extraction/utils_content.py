#the imports
import re
import unicodedata
import PyPDF2
import textract
from .utils_dump_load import dump_to_txt


#PDF content extraction function
def extract_content(filepath):
    content = ""
    file = open(filepath, "rb")
    pdfReader = PyPDF2.PdfFileReader(file)
    for numpage in range(pdfReader.numPages):
        page_content = pdfReader.getPage(numpage).extractText()
        page_text = page_content
        content += page_text
    return content


def textract_content(filepath):
    bytes_string = textract.process(filepath, method='tesseract', encoding='utf-8', language='fra')
    str_extraction  = str(bytes_string, 'utf-8', 'ignore')
    str_extraction = str_extraction.replace("\'", "’").replace("\x0c", " ")
    return re.sub('[Ÿ_!°@#$]', '', str_extraction)


#Table of extracted content
def table_of_content(entity, txt_file, level=0):
    sub_entities = entity.sub_entities
    for sub_entity_key in sub_entities.keys():
        sub_entity = sub_entities[sub_entity_key]
        line = "\t"*level + str(sub_entity.number) + " " + sub_entity.title + "\n"
        if txt_file == None:
            print(line)
        else:
            print(line)
            dump_to_txt(line, txt_file, "a")
        if sub_entity.sub_entities != {}:
            table_of_content(sub_entity, txt_file, (level+1))



#Cleaning functions
def clean_title(title_res, sub_pattern, start, end):
    i, j = 0, -1
    title = str(title_res)
    while title[i] == "\n":
        i += 1
    while title[j] == "\n":
        j += -1
    #return title.rstrip().lstrip(), (start+i), (end+j)
    c_title = re.findall(sub_pattern, title)[0].replace(":", "").replace("-", "").rstrip().lstrip()
    return c_title, (start+i), (end+j+1)


def clean_content(content):
    page_pattern = r"Page \d*/\d*"
    new_content = re.sub(page_pattern, "", content)
    new_content = re.sub("\s*\n+", "\n", new_content)
    return new_content.rstrip().lstrip()


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
