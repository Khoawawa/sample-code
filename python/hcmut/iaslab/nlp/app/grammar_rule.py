import pandas as pd
import numpy as np
import os
from nltk.grammar import CFG, FeatureGrammar
import hcmut.iaslab.nlp.app.utility as utility

def print_rules(grammar_file,lexicon_file,output_file):
    generate_grammar(grammar_file,output_file)
    generate_grammar(lexicon_file,output_file,append=True)
    
def remove_last_space(s):
    return s[:-1] if s.endswith(' ') else s 
    
def generate_grammar(input_file,output_file, append = False):
    df = pd.read_excel(input_file)
    df.fillna("")
    rule_col = 'Production Rule' if not append else 'Terminal'
    grammar_rules = df.groupby('Non-terminal').agg({
        rule_col: lambda x: ' | '.join(x.astype(str).tolist() if not append else [f"'{item}'" for item in x])
    }).reset_index()
    grammar_rules['is_S'] = grammar_rules['Non-terminal'].str.startswith("S")
    grammar_rules = grammar_rules.sort_values(by='is_S',ascending=False).drop(columns=['is_S'])
    
    grammar_rules = grammar_rules.apply(lambda row: f"{row['Non-terminal']} -> {row[rule_col]}", axis=1).tolist()
    
    # Determine file writing mode
    open_type = 'w' if not append else 'a'
    # os.chdir('/')
    print(os.path.exists("../output"))
    
    # Write the grammar rules to the output file
    with open(output_file, open_type) as f:
        if open_type == 'a':
            f.write("\n")
        f.write("\n".join(grammar_rules))



if __name__ == '__main__':
    print_rules()
    # get_root_directory()