import nltk
from nltk.parse import FeatureChartParser
from nltk.parse import EarleyChartParser
from nltk.grammar import FeatureGrammar
from numpy import empty

import hcmut.iaslab.nlp.app.utility as utility

def parse(grammar,sentences,parser,output_file,trace=1):
    with open(output_file,'w') as f:
        for sent in sentences:
            tokens = nltk.word_tokenize(sent) 
            cp = parser(grammar, trace =trace)
            try: 
                chart = cp.chart_parse(tokens)
                trees = list(chart.parses(grammar.start()))
            
                if not trees:
                    f.write('()\n')
                else:
                    for tree in trees:
                        f.write(' '.join(str(tree).split()) + '\n')
            except ValueError:
                f.write('()\n') # if tokens not in grammar then output ()

