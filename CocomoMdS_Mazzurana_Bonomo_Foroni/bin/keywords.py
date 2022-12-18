import re

LANGS = ["python", "c", "c++", "c#", "java", "javascript", "php", "assembly", "batch", "bash", "powershell"]

KEYWORDS = {
    "python": ["def", "if", "for", "in", "and", "not", "or", "print", "class", "try", "except", "import", "from", "as",
               "lambda"],
    "c": ["int", "char", "float", "if", "else", "for", "while", "return", "struct", "union", "typedef", "const",
          "static", "enum", "void"],
    "c++": ["int", "char", "float", "double", "if", "else", "for", "while", "return", "struct", "class", "private",
            "public", "protected", "friend", "virtual", "inline", "const", "static", "template", "namespace", "using",
            "new", "delete"],
    "c#": ["abstract", "as", "base", "bool", "break", "byte", "case", "catch", "char", "checked", "class", "const",
           "continue", "decimal", "default", "delegate", "do", "double", "else", "enum", "event", "explicit", "extern",
           "false", "finally", "fixed", "float", "for", "foreach", "goto", "if", "implicit", "in", "int", "interface",
           "internal", "is", "lock", "long", "namespace", "new", "null", "object", "operator", "out", "override", "params",
           "private", "protected", "public", "readonly", "ref", "return", "sbyte"],
    "java": ["public", "private", "protected", "class", "interface", "extends", "implements", "if", "else", "for",
             "while", "do", "try", "catch", "finally", "return", "void", "null", "this", "super", "new", "import",
             "package"],
    "javascript": ["function", "if", "else", "for", "while", "do", "try", "catch", "finally", "return", "var", "let",
                   "const", "this", "new", "delete", "typeof", "instanceof", "null", "undefined", "NaN", "Infinity"],
    "php": ["function", "if", "else", "for", "while", "echo", "isset", "$_GET", "$_POST", "$_SESSION", "$_COOKIE", "do",
            "default", "declare", "array", "empty", "endforeach", "endfor", "endif", "final", "extends", "goto"],
    "assembly": ["ds", "les", "lfs", "lgs", "lss", "pop", "push", "in	ins	out", "outs", "lahf", "sahf", "popf",
                 "pushf", "cmc", "clc", "stc", "cli", "sti", "cld", "std", "add", "adc", "sub", "sbb", "cmp", "inc",
                 "dec", "test", "sal", "shl", "sar", "shr", "shld", "shrd", "not", "neg", "bound", "and", "or", "xor"],
    "batch": ["echo", "pause", "dir", "cd", "mkdir", "rm", "copy", "if", "else", "for", "while", "call", "goto", "date", "del",
              "color", "exit", "erase", "md", "ftype", "mklink", "path", "prompt", "rename", "time", "set", "start"],
    "bash": ["case", "coproc", "do", "done", "elif", "else", "esac", "fi", "for", "function", "if", "in", "select",
             "then", "until", "while", "{", "}", "time", "[[", "]]"],
    "powershell": ["begin", "break", "catch", "class", "continue", "data", "define", "do", "dynamicparam", "else",
                   "elseif", "end", "enum", "exit", "filter", "finally", "for", "foreach", "from", "function", "hidden",
                   "if", "in", "param", "process", "return", "static", "switch", "throw", "trap", "try", "until", "using",
                   "var ", "while"]
}

def keywordsCount(text):
    """
    Calculates the percentages of the languages based on how many times some keyword of each language are in the text.

        Parameters:
            text (str): text which keywords are extracted from

        Returns:
            percentage (dict): python dictionary with the calculated percentages of each language
    """

    splitted = re.split("\n| |[(]|[{]|=|[+]|-|[*]|/|;", text)
    counters = dict.fromkeys(LANGS, 0)
    percentage = dict.fromkeys(LANGS, 0)
    sum = 0

    for lang in LANGS:
        for keyword in KEYWORDS[lang]:
            counters[lang] += splitted.count(keyword)
            sum += splitted.count(keyword)
    
    for lang in LANGS:
        percentage[lang] = round(((counters[lang] * 100) / sum), 2)

    return percentage
