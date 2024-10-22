import os
from nltk.grammar import CFG

def read_sentences_to_list(sen_file):
    with open(sen_file,'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def get_data_path(data_file):
    return "src/hcmut/iaslab/nlp/app/data/" + data_file 

def get_IO(IO_file, type):
    path = "../" + ('input' if type == "i" else 'output') + '/'
    return path + IO_file

def load_grammar(grammar_file):
    with open(grammar_file,'r') as f:
        grammar_str = f.read().strip() 
    grammar = CFG.fromstring(grammar_str)
    return grammar