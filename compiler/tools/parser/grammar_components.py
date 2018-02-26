from compiler.tools import constants

terminals = [
    constants.T_A_ID,
    constants.T_A_INTEGER,
    constants.T_A_FLOAT,
    constants.T_R_EQUALS,
    constants.T_R_IS_EQUALS,
    constants.T_R_LESS_THAN,
    constants.T_R_LESS_THAN_OR_GREATER_THAN,
    constants.T_R_LESS_THAN_OR_EQUAL,
    constants.T_R_GREATER_THAN,
    constants.T_R_GREATER_THAN_OR_EQUAL,
    constants.T_R_SEMI_COLON,
    constants.T_R_COMMA,
    constants.T_R_DOT,
    constants.T_R_COLON,
    constants.T_R_DOUBLE_COLON,
    constants.T_R_PLUS,
    constants.T_R_MINUS,
    constants.T_R_MULTIPLY,
    constants.T_R_LINE_COMMENT,
    constants.T_R_BLOCK_COMMENT,
    constants.T_R_DIVIDE,
    constants.T_R_OPEN_PARENTHESIS,
    constants.T_R_CLOSE_PARENTHESIS,
    constants.T_R_OPEN_BRACE,
    constants.T_R_CLOSE_BRACE,
    constants.T_R_OPEN_BRACKET,
    constants.T_R_CLOSE_BRACKET,
    constants.T_R_AND,
    constants.T_R_NOT,
    constants.T_R_OR,
    constants.T_R_IF,
    constants.T_R_THEN,
    constants.T_R_ELSE,
    constants.T_R_FOR,
    constants.T_R_CLASS,
    constants.T_R_INT,
    constants.T_R_FLOAT,
    constants.T_R_GET,
    constants.T_R_PUT,
    constants.T_R_RETURN,
    constants.T_R_PROGRAM,
    constants.T_R_EOF,
    constants.T_E_LEADING_ZERO,
    constants.T_E_TRAILING_ZERO,
    constants.T_E_FLOAT_FORMAT,
    constants.T_E_BLOCK_COMMENT_FORMAT,
    constants.T_E_UNEXPECTED_CHAR
]

rules = {
    "1": "prog → A B T_R_PROGRAM funcBody T_R_SEMI_COLON",
    "2": "A → classDecl A",
    "3": "A → EPSILON",
    "4": "B → funcDef B",
    "5": "B → EPSILON",
    "6": "classDecl → T_R_CLASS T_A_ID C T_R_OPEN_BRACE varOrFuncDeclHead T_R_CLOSE_BRACE T_R_SEMI_COLON",
    "7": "varOrFuncDeclHead → type T_A_ID varOrFuncDeclTail",
    "8": "varOrFuncDeclHead → EPSILON",
    "9": "varOrFuncDeclTail → T_R_OPEN_PARENTHESIS funcDeclTail funcDeclOnly",
    "10": "varOrFuncDeclTail → I varDeclTail varOrFuncDeclHead",
    "11": "funcDeclOnly → type T_A_ID T_R_OPEN_PARENTHESIS funcDeclTail funcDeclOnly",
    "12": "funcDeclOnly → EPSILON",
    "13": "varDeclOnlyHead → type T_A_ID I varDeclTail varDeclOnlyHead",
    "14": "varDeclOnlyHead → EPSILON",
    "15": "C → T_R_COLON T_A_ID D",
    "16": "C → EPSILON",
    "17": "D → T_R_COMMA T_A_ID D",
    "18": "D → EPSILON",
    "19": "F → funcDecl F",
    "20": "F → EPSILON",
    "21": "funcDecl → type T_A_ID T_R_OPEN_PARENTHESIS fParams T_R_CLOSE_PARENTHESIS T_R_SEMI_COLON",
    "22": "funcDeclTail → fParams T_R_CLOSE_PARENTHESIS T_R_SEMI_COLON",
    "23": "funcHead → type G T_R_OPEN_PARENTHESIS fParams T_R_CLOSE_PARENTHESIS",
    "24": "G → T_A_ID G`",
    "25": "G` → T_R_DOUBLE_COLON T_A_ID",
    "26": "G` → EPSILON",
    "27": "funcDef → funcHead funcBody T_R_SEMI_COLON",
    "28": "funcBody → T_R_OPEN_BRACE varDeclOnlyHead H T_R_CLOSE_BRACE",
    "29": "H → statement H",
    "30": "H → EPSILON",
    "31": "varDeclTail → T_R_SEMI_COLON",
    "32": "I → arraySize I",
    "33": "I → EPSILON",
    "34": "statement → T_R_FOR T_R_OPEN_PARENTHESIS type T_A_ID assignOp expr T_R_SEMI_COLON arithExpr relExpr T_R_SEMI_COLON assignStat T_R_CLOSE_PARENTHESIS statBlock T_R_SEMI_COLON",
    "35": "statement → T_R_IF T_R_OPEN_PARENTHESIS expr T_R_CLOSE_PARENTHESIS T_R_THEN statBlock T_R_ELSE statBlock T_R_SEMI_COLON",
    "36": "statement → T_R_GET T_R_OPEN_PARENTHESIS varFuncCallHeader T_R_CLOSE_PARENTHESIS T_R_SEMI_COLON",
    "37": "statement → T_R_PUT T_R_OPEN_PARENTHESIS expr T_R_CLOSE_PARENTHESIS T_R_SEMI_COLON",
    "38": "statement → T_R_RETURN T_R_OPEN_PARENTHESIS expr T_R_CLOSE_PARENTHESIS T_R_SEMI_COLON",
    "39": "statement → assignStat T_R_SEMI_COLON",
    "40": "assignStat → varFuncCallHeader assignOp expr",
    "41": "statBlock → T_R_OPEN_BRACE H T_R_CLOSE_BRACE",
    "42": "statBlock → statement",
    "43": "statBlock → EPSILON",
    "44": "expr → arithExpr isRelExpr",
    "45": "isRelExpr → relExpr",
    "46": "isRelExpr → EPSILON",
    "47": "relExpr → relOp arithExpr",
    "48": "arithExpr → term arithExpr`",
    "49": "arithExpr` → addOp term arithExpr`",
    "50": "arithExpr` → EPSILON",
    "51": "sign → T_R_MINUS",
    "52": "sign → T_R_PLUS",
    "53": "term → factor term`",
    "54": "term` → multOp factor term`",
    "55": "term` → EPSILON",
    "56": "factor → T_R_OPEN_PARENTHESIS arithExpr T_R_CLOSE_PARENTHESIS",
    "57": "factor → T_A_FLOAT",
    "58": "factor → T_A_INTEGER",
    "59": "factor → T_R_NOT factor",
    "60": "factor → varFuncCallHeader",
    "61": "factor → sign factor",
    "62": "varFuncCallHeader → T_A_ID J T_A_ID varFuncCallTail",
    "63": "varFuncCallTail → variableTail",
    "64": "varFuncCallTail → functionCallTail",
    "65": "variableTail → K",
    "66": "functionCallTail → T_R_OPEN_PARENTHESIS aParams T_R_CLOSE_PARENTHESIS",
    "67": "J → T_R_OPEN_PARENTHESIS aParams T_R_CLOSE_PARENTHESIS T_R_DOT T_A_ID J",
    "68": "J → K T_R_DOT T_A_ID J",
    "69": "J → EPSILON",
    "70": "K → indice K",
    "71": "K → EPSILON",
    "72": "idnestP → T_R_OPEN_PARENTHESIS aParams T_R_CLOSE_PARENTHESIS T_R_DOT T_A_ID",
    "73": "idnestP → K T_R_DOT T_A_ID",
    "74": "idnestP → EPSILON",
    "75": "indice → T_R_OPEN_BRACKET arithExpr T_R_CLOSE_BRACKET",
    "76": "arraySize → T_R_OPEN_BRACKET T_A_INTEGER T_R_CLOSE_BRACKET",
    "77": "type → T_R_FLOAT",
    "78": "type → T_R_INT",
    "79": "fParams → type T_A_ID I L",
    "80": "fParams → EPSILON",
    "81": "L → fParamsTail L",
    "82": "L → EPSILON",
    "83": "aParams → expr M",
    "84": "aParams → EPSILON",
    "85": "M → aParamsTail M",
    "86": "M → EPSILON",
    "87": "fParamsTail → T_R_COMMA type T_A_ID I",
    "88": "aParamsTail → T_R_COMMA expr",
    "89": "assignOp → T_R_EQUALS",
    "90": "relOp → T_R_GREATER_THAN",
    "91": "relOp → T_R_GREATER_THAN_OR_EQUAL",
    "92": "relOp → T_R_IS_EQUALS",
    "93": "relOp → T_R_LESS_THAN",
    "94": "relOp → T_R_LESS_THAN_OR_EQUAL",
    "95": "relOp → T_R_LESS_THAN_OR_GREATER_THAN",
    "96": "addOp → T_R_MINUS",
    "97": "addOp → T_R_OR",
    "98": "addOp → T_R_PLUS",
    "99": "multOp → T_R_AND",
    "100": "multOp → T_R_DIVIDE",
    "101": "multOp → T_R_MULTIPLY",
    "102": "POP",
    "103": "SCAN"
}

predict_set = {
    "1": {
        "LHS": "prog",
        "RHS": ["A", "B", "T_R_PROGRAM", "funcBody", "T_R_SEMI_COLON"]},
    "2": {
        "LHS": "A",
        "RHS": ["classDecl", "A"]},
    "3": {
        "LHS": "A",
        "RHS": ["EPSILON"]},
    "4": {
        "LHS": "B",
        "RHS": ["funcDef", "B"]},
    "5": {
        "LHS": "B",
        "RHS": ["EPSILON"]},
    "6": {
        "LHS": "classDecl",
        "RHS": ["T_R_CLASS", "T_A_ID", "C", "T_R_OPEN_BRACE", "varOrFuncDeclHead", "T_R_CLOSE_BRACE",
                "T_R_SEMI_COLON"]},
    "7": {
        "LHS": "varOrFuncDeclHead",
        "RHS": ["type", "T_A_ID", "varOrFuncDeclTail"]},
    "8": {
        "LHS": "varOrFuncDeclHead",
        "RHS": ["EPSILON"]},
    "9": {
        "LHS": "varOrFuncDeclTail",
        "RHS": ["T_R_OPEN_PARENTHESIS", "funcDeclTail", "funcDeclOnly"]},
    "10": {
        "LHS": "varOrFuncDeclTail",
        "RHS": ["I", "varDeclTail", "varOrFuncDeclHead"]},
    "11": {
        "LHS": "funcDeclOnly",
        "RHS": ["type", "T_A_ID", "T_R_OPEN_PARENTHESIS", "funcDeclTail", "funcDeclOnly"]},
    "12": {
        "LHS": "funcDeclOnly",
        "RHS": ["EPSILON"]},
    "13": {
        "LHS": "varDeclOnlyHead",
        "RHS": ["type", "T_A_ID", "I", "varDeclTail", "varDeclOnlyHead"]},
    "14": {
        "LHS": "varDeclOnlyHead",
        "RHS": ["EPSILON"]},
    "15": {
        "LHS": "C",
        "RHS": ["T_R_COLON", "T_A_ID", "D"]},
    "16": {
        "LHS": "C",
        "RHS": ["EPSILON"]},
    "17": {
        "LHS": "D",
        "RHS": ["T_R_COMMA", "T_A_ID", "D"]},
    "18": {
        "LHS": "D",
        "RHS": ["EPSILON"]},
    "19": {
        "LHS": "F",
        "RHS": ["funcDecl", "F"]},
    "20": {
        "LHS": "F",
        "RHS": ["EPSILON"]},
    "21": {
        "LHS": "funcDecl",
        "RHS": ["type", "T_A_ID", "T_R_OPEN_PARENTHESIS", "fParams", "T_R_CLOSE_PARENTHESIS", "T_R_SEMI_COLON"]},
    "22": {
        "LHS": "funcDeclTail",
        "RHS": ["fParams", "T_R_CLOSE_PARENTHESIS", "T_R_SEMI_COLON"]},
    "23": {
        "LHS": "funcHead",
        "RHS": ["type", "G", "T_R_OPEN_PARENTHESIS", "fParams", "T_R_CLOSE_PARENTHESIS"]},
    "24": {
        "LHS": "G",
        "RHS": ["T_A_ID", "G`"]},
    "25": {
        "LHS": "G`",
        "RHS": ["T_R_DOUBLE_COLON", "T_A_ID"]},
    "26": {
        "LHS": "G`",
        "RHS": ["EPSILON"]},
    "27": {
        "LHS": "funcDef",
        "RHS": ["funcHead", "funcBody", "T_R_SEMI_COLON"]},
    "28": {
        "LHS": "funcBody",
        "RHS": ["T_R_OPEN_BRACE", "varDeclOnlyHead", "H", "T_R_CLOSE_BRACE"]},
    "29": {
        "LHS": "H",
        "RHS": ["statement", "H"]},
    "30": {
        "LHS": "H",
        "RHS": ["EPSILON"]},
    "31": {
        "LHS": "varDeclTail",
        "RHS": ["T_R_SEMI_COLON"]},
    "32": {
        "LHS": "I",
        "RHS": ["arraySize", "I"]},
    "33": {
        "LHS": "I",
        "RHS": ["EPSILON"]},
    "34": {
        "LHS": "statement",
        "RHS": ["T_R_FOR", "T_R_OPEN_PARENTHESIS", "type", "T_A_ID", "assignOp", "expr", "T_R_SEMI_COLON", "arithExpr",
                "relExpr", "T_R_SEMI_COLON", "assignStat", "T_R_CLOSE_PARENTHESIS", "statBlock", "T_R_SEMI_COLON"]},
    "35": {
        "LHS": "statement",
        "RHS": ["T_R_IF", "T_R_OPEN_PARENTHESIS", "expr", "T_R_CLOSE_PARENTHESIS", "T_R_THEN", "statBlock", "T_R_ELSE",
                "statBlock", "T_R_SEMI_COLON"]},
    "36": {
        "LHS": "statement",
        "RHS": ["T_R_GET", "T_R_OPEN_PARENTHESIS", "varFuncCallHeader", "T_R_CLOSE_PARENTHESIS", "T_R_SEMI_COLON"]},
    "37": {
        "LHS": "statement",
        "RHS": ["T_R_PUT", "T_R_OPEN_PARENTHESIS", "expr", "T_R_CLOSE_PARENTHESIS", "T_R_SEMI_COLON"]},
    "38": {
        "LHS": "statement",
        "RHS": ["T_R_RETURN", "T_R_OPEN_PARENTHESIS", "expr", "T_R_CLOSE_PARENTHESIS", "T_R_SEMI_COLON"]},
    "39": {
        "LHS": "statement",
        "RHS": ["assignStat", "T_R_SEMI_COLON"]},
    "40": {
        "LHS": "assignStat",
        "RHS": ["varFuncCallHeader", "assignOp", "expr"]},
    "41": {
        "LHS": "statBlock",
        "RHS": ["T_R_OPEN_BRACE", "H", "T_R_CLOSE_BRACE"]},
    "42": {
        "LHS": "statBlock",
        "RHS": ["statement"]},
    "43": {
        "LHS": "statBlock",
        "RHS": ["EPSILON"]},
    "44": {
        "LHS": "expr",
        "RHS": ["arithExpr", "isRelExpr"]},
    "45": {
        "LHS": "isRelExpr",
        "RHS": ["relExpr"]},
    "46": {
        "LHS": "isRelExpr",
        "RHS": ["EPSILON"]},
    "47": {
        "LHS": "relExpr",
        "RHS": ["relOp", "arithExpr"]},
    "48": {
        "LHS": "arithExpr",
        "RHS": ["term", "arithExpr`"]},
    "49": {
        "LHS": "arithExpr`",
        "RHS": ["addOp", "term", "arithExpr`"]},
    "50": {
        "LHS": "arithExpr`",
        "RHS": ["EPSILON"]},
    "51": {
        "LHS": "sign",
        "RHS": ["T_R_MINUS"]},
    "52": {
        "LHS": "sign",
        "RHS": ["T_R_PLUS"]},
    "53": {
        "LHS": "term",
        "RHS": ["factor", "term`"]},
    "54": {
        "LHS": "term`",
        "RHS": ["multOp", "factor", "term`"]},
    "55": {
        "LHS": "term`",
        "RHS": ["EPSILON"]},
    "56": {
        "LHS": "factor",
        "RHS": ["T_R_OPEN_PARENTHESIS", "arithExpr", "T_R_CLOSE_PARENTHESIS"]},
    "57": {
        "LHS": "factor",
        "RHS": ["T_A_FLOAT"]},
    "58": {
        "LHS": "factor",
        "RHS": ["T_A_INTEGER"]},
    "59": {
        "LHS": "factor",
        "RHS": ["T_R_NOT", "factor"]},
    "60": {
        "LHS": "factor",
        "RHS": ["varFuncCallHeader"]},
    "61": {
        "LHS": "factor",
        "RHS": ["sign", "factor"]},
    "62": {
        "LHS": "varFuncCallHeader",
        "RHS": ["T_A_ID", "J", "T_A_ID", "varFuncCallTail"]},
    "63": {
        "LHS": "varFuncCallTail",
        "RHS": ["variableTail"]},
    "64": {
        "LHS": "varFuncCallTail",
        "RHS": ["functionCallTail"]},
    "65": {
        "LHS": "variableTail",
        "RHS": ["K"]},
    "66": {
        "LHS": "functionCallTail",
        "RHS": ["T_R_OPEN_PARENTHESIS", "aParams", "T_R_CLOSE_PARENTHESIS"]},
    "67": {
        "LHS": "J",
        "RHS": ["T_R_OPEN_PARENTHESIS", "aParams", "T_R_CLOSE_PARENTHESIS", "T_R_DOT", "T_A_ID", "J"]},
    "68": {
        "LHS": "J",
        "RHS": ["K", "T_R_DOT", "T_A_ID", "J"]},
    "69": {
        "LHS": "J",
        "RHS": ["EPSILON"]},
    "70": {
        "LHS": "K",
        "RHS": ["indice", "K"]},
    "71": {
        "LHS": "K",
        "RHS": ["EPSILON"]},
    "72": {
        "LHS": "idnestP",
        "RHS": ["T_R_OPEN_PARENTHESIS", "aParams", "T_R_CLOSE_PARENTHESIS", "T_R_DOT", "T_A_ID"]},
    "73": {
        "LHS": "idnestP",
        "RHS": ["K", "T_R_DOT", "T_A_ID"]},
    "74": {
        "LHS": "idnestP",
        "RHS": ["EPSILON"]},
    "75": {
        "LHS": "indice",
        "RHS": ["T_R_OPEN_BRACKET", "arithExpr", "T_R_CLOSE_BRACKET"]},
    "76": {
        "LHS": "arraySize",
        "RHS": ["T_R_OPEN_BRACKET", "T_A_INTEGER", "T_R_CLOSE_BRACKET"]},
    "77": {
        "LHS": "type",
        "RHS": ["T_R_FLOAT"]},
    "78": {
        "LHS": "type",
        "RHS": ["T_R_INT"]},
    "79": {
        "LHS": "fParams",
        "RHS": ["type", "T_A_ID", "I", "L"]},
    "80": {
        "LHS": "fParams",
        "RHS": ["EPSILON"]},
    "81": {
        "LHS": "L",
        "RHS": ["fParamsTail", "L"]},
    "82": {
        "LHS": "L",
        "RHS": ["EPSILON"]},
    "83": {
        "LHS": "aParams",
        "RHS": ["expr", "M"]},
    "84": {
        "LHS": "aParams",
        "RHS": ["EPSILON"]},
    "85": {
        "LHS": "M",
        "RHS": ["aParamsTail", "M"]},
    "86": {
        "LHS": "M",
        "RHS": ["EPSILON"]},
    "87": {
        "LHS": "fParamsTail",
        "RHS": ["T_R_COMMA", "type", "T_A_ID", "I"]},
    "88": {
        "LHS": "aParamsTail",
        "RHS": ["T_R_COMMA", "expr"]},
    "89": {
        "LHS": "assignOp",
        "RHS": ["T_R_EQUALS"]},
    "90": {
        "LHS": "relOp",
        "RHS": ["T_R_GREATER_THAN"]},
    "91": {
        "LHS": "relOp",
        "RHS": ["T_R_GREATER_THAN_OR_EQUAL"]},
    "92": {
        "LHS": "relOp",
        "RHS": ["T_R_IS_EQUALS"]},
    "93": {
        "LHS": "relOp",
        "RHS": ["T_R_LESS_THAN"]},
    "94": {
        "LHS": "relOp",
        "RHS": ["T_R_LESS_THAN_OR_EQUAL"]},
    "95": {
        "LHS": "relOp",
        "RHS": ["T_R_LESS_THAN_OR_GREATER_THAN"]},
    "96": {
        "LHS": "addOp",
        "RHS": ["T_R_MINUS"]},
    "97": {
        "LHS": "addOp",
        "RHS": ["T_R_OR"]},
    "98": {
        "LHS": "addOp",
        "RHS": ["T_R_PLUS"]},
    "99": {
        "LHS": "multOp",
        "RHS": ["T_R_AND"]},
    "100": {
        "LHS": "multOp",
        "RHS": ["T_R_DIVIDE"]},
    "101": {
        "LHS": "multOp",
        "RHS": ["T_R_MULTIPLY"]
    }
}
