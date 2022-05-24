import spacy  # version 3.0.6'
# initialize language model
nlp = spacy.load("en_core_web_md")

import spacy_entity_linker

import os

print("xXXXA:"+spacy_entity_linker.DatabaseConnection.DB_DEFAULT_PATH)
#sqlite3.connect(spacy_entity_linker.DatabaseConnection.DB_DEFAULT_PATH)

# add pipeline (declared through entry_points in setup.py)
nlp.add_pipe("entityLinker", last=True)

doc = nlp("""The following events happend in Colombia on Monday:

Carlos attacked Uribe.

Uribe attacked Marcel.

Marcel attacked Alvaro Uribe.

Alvaro Uribe attacked Erik.

Erik attached Julia.

Julia attacked Juan Manuel Santos.

Juan Manuel attacked Carlos.""")

# returns all entities in the whole document
all_linked_entities = doc._.linkedEntities
# iterates over sentences and prints linked entities

for sent in doc.sents:
    for e in sent._.linkedEntities.entities:
      print(e.__dict__)