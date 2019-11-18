chapter_pattern = "CHAPITRE \d ([A-Z /,]*)"
sub_chapter_pattern = r"\n\s*LA GARANTIE(.*?)\n"
article_pattern = r"\n\s*ARTICLE \d(.*?)\n"
sub_article_pattern = r"\n\s*Article \d.\d(.*?)\n"
sub_sub_article_pattern = r"\n\s*\d[.]\d.\ *(.*?)\n"

dict_level_to_pattern = {}

dict_level_to_pattern[1] = {"level_type": "chapter",
                            "pattern": chapter_pattern}
dict_level_to_pattern[2] = {"level_type": "sub-chapter",
                            "pattern": sub_chapter_pattern}
dict_level_to_pattern[3] = {"level_type": "article",
                            "pattern": article_pattern}
dict_level_to_pattern[4] = {"level_type": "sub-article",
                            "pattern": sub_article_pattern}
dict_level_to_pattern[5] = {"level_type": "sub-article",
                            "pattern": sub_sub_article_pattern}
