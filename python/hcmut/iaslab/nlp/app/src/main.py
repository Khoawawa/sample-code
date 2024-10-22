import generate
import grammar_rule
import parse
import utils
import nltk
from nltk.parse import EarleyChartParser

nltk.download()

grammar_file = utils.get_path('output/grammar.txt')
output_file = utils.get_path('output/samples.txt')
#1.1 WRITE GRAMMAR TO GRAMMAR TXT
grammar_rule.print_rules()
#load grammar to nltk.CFG
# grammar = utils.load_grammar(grammar_file)
# #1.2 GENERATE 10,000 SENTENCES
# generate.generate_cfg(grammar,output_file)
# #1.3 PARSING FROM INPUT
# #get input to list 
# input_file = utils.get_path('input/sentences.txt')
# #OPTIONAL to generate random sentences for sentences.txt
# # generate.generate_random(grammar,input_file,n=30)

# sentences = utils.read_sentences_to_list(input_file)
# #parse list of sentence
# parse.parse(grammar,sentences,EarleyChartParser)

