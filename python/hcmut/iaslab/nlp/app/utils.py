def test(**kwargs):
    from hcmut.iaslab.nlp.app import generate
    from hcmut.iaslab.nlp.app.grammar_rule import print_rules
    from hcmut.iaslab.nlp.app import parse
    from hcmut.iaslab.nlp.app import utility
    
    import os
    from nltk.parse import EarleyChartParser
    
    os.chdir('/')
    print(os.path.exists('nlp/output'))
    
    grammar_xlsx = utility.get_data_path('grammar_cfg.xlsx')
    lexicon_xlsx = utility.get_data_path('lexicon_cfg.xlsx')
    
    grammar_file = utility.get_IO('grammar.txt','o')
    
    sample_file = utility.get_IO('samples.txt','o')
    
    sentences_file = utility.get_IO('sentences.txt','i')
    
    # #1.1 WRITE GRAMMAR TO GRAMMAR TXT
    print_rules(grammar_xlsx,lexicon_xlsx,grammar_file)
    # #load grammar to nltk.CFG
    # grammar = utility.load_grammar(grammar_file)
    # #1.2 GENERATE 10,000 SENTENCES
    # generate.generate_cfg(grammar,sample_file)
    # #1.3 PARSING FROM INPUT
    # #OPTIONAL to generate random sentences for sentences.txt
    # # generate.generate_random(grammar,input_file,n=30)
    # sentences = utility.read_sentences_to_list(sentences_file)
    # #parse list of sentence
    # parse.parse(grammar,sentences,EarleyChartParser)

