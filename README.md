<<<<<<< HEAD
# CKY ParserThis project realizes two functions:1、Convert any Context-Free Grammar into a Chomsky Normal Form grammar.2、Parse a sentence with Cocke-Kasami-Younger algorithm.------## UsageThe project contains *CKY.py*, *CNF.py*, *grammar.txt* and *str.txt*.*CNF.py* can convert any CFG into a CNF grammar.*CKY.py* can parse a sentence based on CNF grammar.*grammar.txt* contains the generic CFG.*str.txt* contains the sentence to be parsedWe put these four files in the same directory, and then run the command:
```python CKY.py grammar.txt str.txt```
we will get the result.See the **Example** below, you will know how to use it.------## ExampleFor example, if we want to parse the sentence "Book the flight through Houston", we can write the sentence in the *str1.txt* file:
```Book the flight through Houston```
Then we build a context-free grammar which contains the input sentence and write it in the *grammar.txt* file:
```S -> NP VPS -> Aux NP VPS -> VPNP -> PronounNP -> Proper-NounNP -> Det NominalNominal -> NounNominal -> Nominal NounNominal -> Nominal PPVP -> Verb NPVP -> Verb NP PPVP -> VerbVP -> Verb PPVP -> VP PPPP -> Preposition NPVerb -> 'Book'Det -> 'the'Noun -> 'flight'Preposition -> 'through'Proper-Noun -> 'Houston'```
After constructing the two files above, we can run the command:
```python CKY.py grammar.txt str1.txt```
Then we can get the new grammar in CNF which is in *new_grammar.txt* file, possible parses and visualization of the parse tree:```The given sentence is contained in the language produced by the given grammarPossible parse(s):[S [Verb 'Book'] [NP [Det 'the'] [Nominal [Nominal 'flight'] [PP [Preposition 'through'] [NP 'Houston']]]]][S [VP1 [Verb 'Book'] [NP [Det 'the'] [Nominal 'flight']]] [PP [Preposition 'through'] [NP 'Houston']]][S [VP [Verb 'Book'] [NP [Det 'the'] [Nominal 'flight']]] [PP [Preposition 'through'] [NP 'Houston']]]```<center>![](https://github.com/Huntersxsx/CKY-Parser/img/tree1.png)

![](https://github.com/Huntersxsx/CKY-Parser/img/tree2.png)

![](https://github.com/Huntersxsx/CKY-Parser/img/tree3.png)

</center>
------## Probabilistic CKY Parsing of PCFGsProbabilistic Context-Free Grammar is the simplest augmentation of the context-free grammar, and the algorithms for computing the most likely parse are simple extensions of the standard algorithms for parsing. Most modern probabilistic parsers are based on the probabilistic CKY.In this project, I also realize the Probabilistic CKY and put it in the P-CKY directory. Compared with CKY, the Probabilistic CKY has only made some simple modifications. The usage is similar, we can run the program by:
```python P_CKY.py p_grammar.txt str1.txt```
and then we will get the possibility of each parse and the visualization of the most-likely parse.For example, we can get the result:
```The given sentence is contained in the language produced by the given grammarPossible parse(s):[S [Verb 'Book'] [NP [Det 'the'] [Nominal [Nominal 'flight'] [PP [Preposition 'through'] [NP 'Houston']]]]]the possibility of this parse is  0.002[S [VP1 [Verb 'Book'] [NP [Det 'the'] [Nominal 'flight']]] [PP [Preposition 'through'] [NP 'Houston']]]the possibility of this parse is  0.02[S [VP [Verb 'Book'] [NP [Det 'the'] [Nominal 'flight']]] [PP [Preposition 'through'] [NP 'Houston']]]the possibility of this parse is  0.006The most-likely parse is: [S [VP1 [Verb 'Book'] [NP [Det 'the'] [Nominal 'flight']]] [PP [Preposition 'through'] [NP 'Houston']]] its possibility is: 0.02```
Considering that we cannot get the actual probability of each grammar rule, I assign every rule a possibilty and write the grammar in CNF, see it in the *p_grammar.txt*.

<center>![](https://github.com/Huntersxsx/CKY-Parser/img/tree1.png)
</center>

=======
# CKY-Parser
CKY algorithm and Probabilistic CKY algorithm
>>>>>>> a61a64b1c4d829ac6eea95c4e874dab21a1f11c2
