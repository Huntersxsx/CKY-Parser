# Global dictionary used for storing the rules.
RULE_DICT = {}


def read_grammar(grammar):
    """
    Load the given grammar and stores it in a List.
    :param grammar: the grammar file.
    """
    with open(grammar) as fr:
        lines = fr.readlines()
    return [x.replace("->", "").split() for x in lines]


def add_rule(rule):
    """
    Adds a rule to the dictionary of lists of rules.
    :param rule: the rule to add to the dict.
    """
    global RULE_DICT

    if rule[0] not in RULE_DICT:
        RULE_DICT[rule[0]] = []
    RULE_DICT[rule[0]].append(rule[1:])


def convert_grammar(grammar):
    """
    Converts a context-free grammar to Chomsky normal form: A -> B C or A -> a
    :param grammar: the CFG.
    :return: grammar converted into CNF.
    """

    # there are three situations we need to address in any generic grammar
    global RULE_DICT
    unit_productions, result = [], []
    res_append = result.append
    index = 0

    for rule in grammar:
        new_rules = []
        if len(rule) == 2 and rule[1][0] != "'":
            # 1、rules that have a single non-terminal on the RHS
            unit_productions.append(rule)
            add_rule(rule)
            continue
        elif len(rule) > 2:
            # 2、rules that mixes terminals with non-terminals on the RHS
            terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if terminals:
                for it in terminals:
                    # Create a new non terminal symbol and replace the terminal symbol with it.
                    # The non terminal symbol derives the replaced terminal symbol.
                    rule[it[1]] = f"{rule[0]}{str(index)}"
                    new_rules += [f"{rule[0]}{str(index)}", it[0]]
                index += 1
            # 3、rules in which the length of the RHS is greater than 2
            while len(rule) > 3:
                new_rules += [f"{rule[0]}{str(index)}", rule[1], rule[2]]
                rule = [rule[0]] + [f"{rule[0]}{str(index)}"] + rule[3:]
                index += 1
        add_rule(rule)
        res_append(rule)
        if new_rules:
            res_append(new_rules)
    # 1、rules that have a single non-terminal on the RHS
    while unit_productions:
        rule = unit_productions.pop()
        if rule[1] in RULE_DICT:
            for item in RULE_DICT[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    if new_rule not in result:
                        res_append(new_rule)
                else:
                    unit_productions.append(new_rule)
                add_rule(new_rule)
    return result
