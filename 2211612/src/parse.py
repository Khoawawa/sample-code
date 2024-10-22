import nltk
from nltk.parse import FeatureChartParser
from nltk.parse import EarleyChartParser
from nltk.grammar import FeatureGrammar
from numpy import empty
from generate import demo_grammar
import utils
def parse(grammar,sentences,parser,trace=1):
    output=utils.get_path('output/parse-results.txt')
    with open(output,'w') as f:
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

def demo():
    parse(FeatureGrammar.fromstring(demo_grammar),['dogs run','dog runs'],FeatureChartParser)

if __name__ == "__main__":
    demo()