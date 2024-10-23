# NLP GENERATING AND PARSING WITH GRAMMAR RULES
## A Simple Grammar
<!-- Grammar rule -->

```
S -> NP_S_S3 VP_S3 | NP_S VP | WH_S VP
NP_LOC -> DET ADJ N_LOC | DET N_LOC
NP_NS -> DET ADJ N | DET N | N
NP_OBJ -> NP_S3 | NP_NS | PRO_OBJ_S3 | PRO_OBJ
NP_S -> NP_NS | PRO | NP_NS PP
NP_S3 -> N_S3 | DET_S3 ADJ N_S3 | DET_S3 N_S3 | N_S3
NP_S_S3 -> NP_S3 | PRO_S3 | NP_S3 PP
PP -> P NP_LOC
VP -> V_intrans | V | V NP_OBJ | V NP_OBJ | V_intrans PP
VP_S3 -> V_S3_intrans | V_S3 NP_OBJ | V_S3_intrans PP
WH_S -> WH AUX_S3 NP_S3 | WH AUX NP_NS
ADJ -> 'big'
AUX -> 'do'
V_intrans -> 'eat' | 'laugh'
V_S3_intrans -> 'eats' | 'laughs'
V_S3  -> 'writes' | 'eats'
V_S3 -> 'is'
V  -> 'write' | 'eat'
PRO_S3 -> 'he' | 'she' | 'it'
PRO_OBJ_S3 -> 'it'
PRO_OBJ_3 -> 'him' | 'her'
PRO_OBJ -> 'them' | 'me' | 'you' | 'us'
PRO -> 'I' | 'you' | 'they' | 'we'
P -> 'in' | 'at' | 'over' | 'under'
N_S3 -> 'dog' | 'cat'
N_LOC -> 'window'
N -> 'dogs' | 'cats'
DET_S3 -> 'a' | 'the'
DET -> 'the'
AUX_S3 -> 'does'
WH -> 'what' | 'who' | 'why' | 'where' | 'when'
```
## Generation
Use `generate_cfg()` in grammar_rule.py to generate 10000 sentences
### An example
```
the big dog eats over the window
```
## Parsing
Use `parse()` in parse.py to parse sentences
### An example for **the big dog eats over the window** 
```
(S (NP_S_S3 (NP_S3 (DET_S3 the) (ADJ big) (N_S3 dog))) (VP_S3 (V_S3_intrans eats) (PP (P over) (NP_LOC (DET the) (N_LOC window)))))
```