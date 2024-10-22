import os
from nltk.grammar import CFG

def read_sentences_to_list(sen_file):
    with open(sen_file,'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]
def get_root_directory():
    # os.chdir("/")
    project_directory = os.getcwd()
    return project_directory
def get_path(path):
    return get_root_directory() + "/python/hcmut/iaslab/nlp/app/" + path

def load_grammar(grammar_file = get_path("output/grammar.txt")):
    with open(grammar_file,'r') as f:
        grammar_str = f.read().strip() 
    grammar = CFG.fromstring(grammar_str)
    return grammar