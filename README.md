[!logo](images/parser.png)

### PDF Parser
**Purpose**: Extract a structured content of a file

Note: Entity = Chapter, article, sub-chapter...

## Entity class
* level (int): in the content structure (highest level: 0)
* number (int)
* title (string)
* content (string)
* sub-entities (Entity)
* parent-entity (Entity)
* source (string): path from top to the entity

## Architecture
* Extraction folder
* Inputs folder
    * contract.pdf: source file
    * contract_spec.py: file structure specification
* Outputs folder
    * content.txt: text content extracted
    * content.pkl: structured content extraction
    * table.txt: table of content extracted
