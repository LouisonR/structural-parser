import re
from .utils_dump_load import load_from_txt
from .utils_content import remove_accents, clean_title, clean_content
from inputs.contract_spec import dict_level_to_pattern

###################################

class Entity():
    def __init__(self, level, number, title, content):
        self.level = level
        self.number = number
        self.title = title
        self.content = content
        self.sub_entities = {}
        self.parent_entity = None
        self.source = ""


    def get_sub_entities_content(self):
        nb_entities = len(dict_level_to_pattern.keys())
        if self.level < nb_entities:
            self.get_entity_content(self.content)
            self.clean_sub_entities()
            for sub_entity_key in self.sub_entities.keys():
                sub_entity = self.sub_entities[sub_entity_key]
                if self.level < nb_entities-1:
                    sub_entity.get_sub_entities_content()
                sub_entity.parent_entity = self


    def get_entity_content(self, content, title_memory=""):
        content_without_accent = remove_accents(content)
        sub_pattern=dict_level_to_pattern[self.level+1]["pattern"]
        res = re.search(sub_pattern, content_without_accent)

        if res == None:
            pass
        else:
            title, start, end = clean_title(res.group(), sub_pattern, res.start(), res.end())
            sub = content[:start]
            content_rest = "\n\n" + content[end:]
            num = len(self.sub_entities.keys())

            self.sub_entities[num] = Entity(
                                            level=self.level+1,
                                            number=num,
                                            title=title_memory,
                                            content=sub
                                            )
            #look for the next one
            next_res = re.search(sub_pattern, content_rest)
            if next_res!= None:
                self.get_entity_content(content_rest, title)
            else:
                num += 1
                self.sub_entities[num] = Entity(
                                                level=self.level+1,
                                                number=num,
                                                title=title,
                                                content=content_rest
                                                )

    def get_and_clean(self):
        self.content = clean_content(self.content)
        self.source += self.title.lower()
        parent = self.parent_entity
        while parent != None:
            self.source = parent.title.lower() + "\\" + self.source
            parent = parent.parent_entity


    def clean_sub_entities(self):
        if 0 in self.sub_entities.keys():
            del self.sub_entities[0]


##########################################

def browse_entity(entity):
    if entity.level == 0:
        entity.get_sub_entities_content()
    entity.get_and_clean()
    for sub_entity_key in entity.sub_entities.keys():
        sub_entity = entity.sub_entities[sub_entity_key]
        browse_entity(sub_entity)
