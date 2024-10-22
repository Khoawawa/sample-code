import copy
import random
import itertools
import sys
from nltk.grammar import Nonterminal, FeatureGrammar, FeatStructNonterminal, FeatureValueType
from nltk.featstruct import unify
import nltk.parse.generate

# from nltk.parse.generate import generate 
def generate(grammar:FeatureGrammar, start = None, depth = None, n= None):
    if not start:
        start = grammar.start()
        
    if depth is None:
        depth = (sys.getrecursionlimit() // 3) - 3
    
    iter = generate_all(grammar,[start],depth,bindings = {})
    
    if n:
        iter = itertools.islice(iter,n)
    return iter

def generate_all(grammar:FeatureGrammar,items:list, depth,bindings=None):
    
    if items:
        try:
            # print(f"{items} --> {bindings}")
            # print(items[0])
            #what i want: bindings persist through the sentence but not between sentences for example S[agr=?a] = NP[agr?a] VP[agr?a], bindings should only persist for those
            for frag1 in generate_one(grammar,items[0], depth,bindings):   
                for frag2 in generate_all(grammar,items[1:],depth,bindings):
                    yield frag1 + frag2
        except RecursionError as err:
            raise RuntimeError(
                "The grammar has rule(s) that yield infinite recursion!\n\
                    Eventually use a lower 'depth', or a higher 'sys.setrecursionlimit()'."
            ) from err
    else:
        yield []

def generate_one(grammar:FeatureGrammar,item,depth,bindings=None):
    if bindings is None:
        bindings = {}
        
    if depth > 0:
        if isinstance(item, Nonterminal):
            gram_prods = grammar.productions(lhs=item)
            for prod in gram_prods:
                lhs = prod.lhs()
                type = grammar._get_type_if_possible(lhs)._value
                # bindings = head_governor(type,bindings)
                # if lhs.type == head_governor(lhs):
                #     binding = {}
                # if type == 'NP':
                #     print(bindings[Variable('?a2')])
                #     # bindings.pop(Variable('?a'),None)
                # else:
                #     bindings = bindings
                    
                unified_lhs = unify(prod.lhs(),item,bindings)
                
                if unified_lhs is not None:
                    
                    yield from generate_all(grammar,prod.rhs(),depth-1,bindings)
        else:
            yield [item]

def generate_cfg(grammar,output_file):    
    with open(output_file,'w') as f:
        sentences = []
        for sent in nltk.parse.generate.generate(grammar,n=10000):
            sentences.append(' '.join(sent))
        f.write('\n'.join(sentences))
        
def generate_random_sentence(grammar,symbol,is_fcfg):
    if not isinstance(symbol,Nonterminal):
        return symbol
    
    prods = grammar.productions(lhs=symbol)
    # print(f'{symbol} -> {prods}')
    prod = random.choice(prods)
    sentence = []
    for symbol in prod.rhs():
        frag = generate_random_sentence(grammar,symbol)
        sentence.append(frag)
    return ' '.join(sentence)

def generate_random(grammar,output_file,n=1):
    with open(output_file,'a') as f:
        sentences = [generate_random_sentence(grammar,grammar.start()) for _ in range(n)]    
        f.write('\n'.join(sentences))
        f.write('\n')
            
demo_grammar = """
    S[AGR=?a] -> NP[AGR=?a] VP[AGR=?a]
    NP[AGR=?a] -> N[AGR=?a]
    N[AGR=[NUM=pl, PER=3]] -> 'dogs'
    N[AGR=[NUM=sg, PER=3]] -> 'dog'
    VP[AGR=?a] -> V[AGR=?a]
    V[AGR=[NUM=sg, PER=3]] -> 'runs'
    V[AGR=[NUM=pl, PER=3]] -> 'run'
"""
def demo(N=23):
    # print(demo_grammar)
    grammar = FeatureGrammar.fromstring(demo_grammar)
    for n, sent in enumerate(generate(grammar,n=N),1):
        print("%3d. %s" % (n, " ".join(sent)))
if __name__ == "__main__":
    demo()