from extraction.class_entity import Entity, browse_entity
from extraction.utils_content import table_of_content, textract_content
from extraction.utils_dump_load import load_from_pickle, dump_to_pickle, load_from_txt, dump_to_txt
import os

#Defining the different paths
dir_path = os.path.dirname(os.path.realpath(__file__))
#   Inputs files
src_filepath = dir_path + "/inputs/contrat.pdf"
#   Outputs files
content_file = dir_path + "/outputs/content.txt"
table_file = dir_path + "/outputs/table.txt"
pickle_file = dir_path + "/outputs/content.pkl"

#Content extraction
if os.path.isfile(content_file) == False:
    print("Process to content extraction")
    content = textract_content(src_filepath)
    dump_to_txt(content, content_file)

#Entity Initialisation
contract = Entity(
                    level=0,
                    title="VISA Premium Contract",
                    number=1,
                    content=load_from_txt(content_file),
                )

#Browse sub entities
browse_entity(contract)

#Dump the table of content of the extracted content
table_of_content(contract, table_file)

#Save the contract extracted content
dump_to_pickle(contract, pickle_file)
