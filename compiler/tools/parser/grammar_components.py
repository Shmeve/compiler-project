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
    "1": "prog → classDeclList funcDefList T_R_PROGRAM funcBody T_R_SEMI_COLON",
    "2": "classDeclList → classDecl classDeclList",
    "3": "classDeclList → EPSILON",
    "4": "classDecl → T_R_CLASS T_A_ID classInherit T_R_OPEN_BRACE classBody T_R_CLOSE_BRACE T_R_SEMI_COLON",
    "5": "classInherit → T_R_COLON T_A_ID classInheritTail",
    "6": "classInherit → EPSILON",
    "7": "classInheritTail → T_R_COMMA T_A_ID classInheritTail",
    "8": "classInheritTail → EPSILON",
    "9": "classBody → classProp classPropTail",
    "10": "classBody → EPSILON",
    "11": "classProp → type T_A_ID",
    "12": "classPropTail → T_R_OPEN_PARENTHESIS fParams T_R_CLOSE_PARENTHESIS T_R_SEMI_COLON funcDecl",
    "13": "classPropTail → arraySize T_R_SEMI_COLON classBody",
    "14": "funcDecl → funcDeclTail funcDecl",
    "15": "funcDecl → EPSILON",
    "16": "funcDeclTail → type T_A_ID T_R_OPEN_PARENTHESIS fParams T_R_CLOSE_PARENTHESIS T_R_SEMI_COLON",
    "17": "funcDefList → funcDef funcDefList",
    "18": "funcDefList → EPSILON",
    "19": "funcDef → funcHead funcBody T_R_SEMI_COLON",
    "20": "funcHead → type T_A_ID funcScope T_R_OPEN_PARENTHESIS fParams T_R_CLOSE_PARENTHESIS",
    "21": "funcScope → T_R_DOUBLE_COLON T_A_ID",
    "22": "funcScope → EPSILON",
    "23": "funcBody → T_R_OPEN_BRACE funcBodyInner T_R_CLOSE_BRACE",
    "24": "funcBodyInner → T_A_ID funcBodyDecl",
    "25": "funcBodyInner → primitiveType varDeclTail funcBodyInner",
    "26": "funcBodyInner → construct funcBodyStat",
    "27": "funcBodyInner → EPSILON",
    "28": "funcBodyStat → statementList",
    "29": "funcBodyDecl → variableCont assignOp expr T_R_SEMI_COLON funcBodyStat",
    "30": "funcBodyDecl → varDeclTail funcBodyInner",
    "31": "varDeclTail → T_A_ID arraySize T_R_SEMI_COLON",
    "32": "construct → T_R_FOR T_R_OPEN_PARENTHESIS type T_A_ID assignOp expr T_R_SEMI_COLON relExpr T_R_SEMI_COLON assignStat T_R_CLOSE_PARENTHESIS statBlock T_R_SEMI_COLON",
    "33": "construct → T_R_IF T_R_OPEN_PARENTHESIS expr T_R_CLOSE_PARENTHESIS T_R_THEN statBlock T_R_ELSE statBlock T_R_SEMI_COLON",
    "34": "construct → T_R_GET T_R_OPEN_PARENTHESIS variable T_R_CLOSE_PARENTHESIS T_R_SEMI_COLON",
    "35": "construct → T_R_PUT T_R_OPEN_PARENTHESIS expr T_R_CLOSE_PARENTHESIS T_R_SEMI_COLON",
    "36": "construct → T_R_RETURN T_R_OPEN_PARENTHESIS expr T_R_CLOSE_PARENTHESIS T_R_SEMI_COLON",
    "37": "statement → assignStat T_R_SEMI_COLON",
    "38": "statement → construct",
    "39": "statementList → statement statementList",
    "40": "statementList → EPSILON",
    "41": "assignStat → variable assignOp expr",
    "42": "statBlock → T_R_OPEN_BRACE statementList T_R_CLOSE_BRACE",
    "43": "statBlock → statement",
    "44": "statBlock → EPSILON",
    "45": "expr → arithExpr exprTail",
    "46": "exprTail → relOp arithExpr",
    "47": "exprTail → EPSILON",
    "48": "relExpr → arithExpr relOp arithExpr",
    "49": "arithExpr → term arithExprTail",
    "50": "arithExprTail → addOp term arithExprTail",
    "51": "arithExprTail → EPSILON",
    "52": "sign → T_R_MINUS",
    "53": "sign → T_R_PLUS",
    "54": "term → factor termTail",
    "55": "termTail → multOp factor termTail",
    "56": "termTail → EPSILON",
    "57": "factor → T_R_OPEN_PARENTHESIS arithExpr T_R_CLOSE_PARENTHESIS",
    "58": "factor → T_A_FLOAT",
    "59": "factor → T_A_INTEGER",
    "60": "factor → T_R_NOT factor",
    "61": "factor → varOrFunc",
    "62": "factor → sign factor",
    "63": "varOrFunc → T_A_ID varOrFuncEval idnest",
    "64": "varOrFuncEval → variableTail",
    "65": "varOrFuncEval → functionCallTail",
    "66": "variableTail → indice",
    "67": "functionCallTail → T_R_OPEN_PARENTHESIS aParams T_R_CLOSE_PARENTHESIS",
    "68": "idnest → T_R_DOT varOrFunc",
    "69": "idnest → EPSILON",
    "70": "variable → T_A_ID variableCont",
    "71": "variableCont → variableTail variableCont2",
    "72": "variableCont → functionCallTail functionCallTrap",
    "73": "variableCont2 → T_R_DOT T_A_ID variableCont",
    "74": "variableCont2 → EPSILON",
    "75": "functionCallTrap → T_R_DOT T_A_ID variableCont",
    "76": "indice → T_R_OPEN_BRACKET arithExpr T_R_CLOSE_BRACKET indice",
    "77": "indice → EPSILON",
    "78": "arraySize → T_R_OPEN_BRACKET T_A_INTEGER T_R_CLOSE_BRACKET arraySize",
    "79": "arraySize → EPSILON",
    "80": "type → T_A_ID",
    "81": "type → primitiveType",
    "82": "primitiveType → T_R_FLOAT",
    "83": "primitiveType → T_R_INT",
    "84": "fParams → type T_A_ID arraySize fParamsTail",
    "85": "fParams → EPSILON",
    "86": "aParams → expr aParamsTail",
    "87": "aParams → EPSILON",
    "88": "fParamsTail → T_R_COMMA type T_A_ID arraySize fParamsTail",
    "89": "fParamsTail → EPSILON",
    "90": "aParamsTail → T_R_COMMA expr aParamsTail",
    "91": "aParamsTail → EPSILON",
    "92": "assignOp → T_R_EQUALS",
    "93": "relOp → T_R_GREATER_THAN",
    "94": "relOp → T_R_GREATER_THAN_OR_EQUAL",
    "95": "relOp → T_R_IS_EQUALS",
    "96": "relOp → T_R_LESS_THAN",
    "97": "relOp → T_R_LESS_THAN_OR_EQUAL",
    "98": "relOp → T_R_LESS_THAN_OR_GREATER_THAN",
    "99": "addOp → T_R_MINUS",
    "100": "addOp → T_R_OR",
    "101": "addOp → T_R_PLUS",
    "102": "multOp → T_R_AND",
    "103": "multOp → T_R_DIVIDE",
    "104": "multOp → T_R_MULTIPLY",
    "105": "POP",
    "106": "SCAN"
}

predict_set = {
    "1": {
        "LHS": "prog",
        "RHS": ["@prog", "@classList", "classDeclList", "@funcDefList", "funcDefList", "T_R_PROGRAM", "funcBody", "@4,1", "T_R_SEMI_COLON"]},
    "2": {
        "LHS": "classDeclList",
        "RHS": ["classDecl", "classDeclList"]},
    "3": {
        "LHS": "classDeclList",
        "RHS": ["EPSILON"]},
    "4": {
        "LHS": "classDecl",
        "RHS": ["@classDecl", "T_R_CLASS", "@id", "T_A_ID", "@inherList", "classInherit", "T_R_OPEN_BRACE", "@membList", "classBody", "@4,1", "@2,1", "T_R_CLOSE_BRACE", "T_R_SEMI_COLON"]},
    "5": {
        "LHS": "classInherit",
        "RHS": ["T_R_COLON", "@id", "T_A_ID", "@2,1", "classInheritTail"]},
    "6": {
        "LHS": "classInherit",
        "RHS": ["EPSILON"]},
    "7": {
        "LHS": "classInheritTail",
        "RHS": ["T_R_COMMA", "@id", "T_A_ID", "@2,1", "classInheritTail"]},
    "8": {
        "LHS": "classInheritTail",
        "RHS": ["EPSILON"]},
    "9": {
        "LHS": "classBody",
        "RHS": ["classProp", "classPropTail"]},
    "10": {
        "LHS": "classBody",
        "RHS": ["EPSILON"]},
    "11": {
        "LHS": "classProp",
        "RHS": ["@type", "type", "@id", "T_A_ID"]},
    "12": {
        "LHS": "classPropTail",
        "RHS": ["@funcDecl", "T_R_OPEN_PARENTHESIS", "@fparamList", "fParams", "@4,3", "@2,1", "T_R_CLOSE_PARENTHESIS", "T_R_SEMI_COLON", "funcDecl"]},
    "13": {
        "LHS": "classPropTail",
        "RHS": ["@varDecl", "@dimList", "arraySize", "@4,3", "@2,1", "T_R_SEMI_COLON", "classBody"]},
    "14": {
        "LHS": "funcDecl",
        "RHS": ["@funcDecl", "funcDeclTail", "funcDecl"]},
    "15": {
        "LHS": "funcDecl",
        "RHS": ["EPSILON"]},
    "16": {
        "LHS": "funcDeclTail",
        "RHS": ["@type", "type", "@id", "T_A_ID", "T_R_OPEN_PARENTHESIS", "@fparamList", "fParams", "@4,1", "@2,1", "T_R_CLOSE_PARENTHESIS", "T_R_SEMI_COLON"]},
    "17": {
        "LHS": "funcDefList",
        "RHS": ["funcDef", "funcDefList"]},
    "18": {
        "LHS": "funcDefList",
        "RHS": ["EPSILON"]},
    "19": {
        "LHS": "funcDef",
        "RHS": ["@funcDef", "funcHead", "funcBody", "@6,1", "@2,1", "T_R_SEMI_COLON"]},
    "20": {
        "LHS": "funcHead",
        "RHS": ["@type", "type", "@id", "T_A_ID", "funcScope", "T_R_OPEN_PARENTHESIS", "@fparamList", "fParams", "T_R_CLOSE_PARENTHESIS"]},
    "21": {
        "LHS": "funcScope",
        "RHS": ["T_R_DOUBLE_COLON", "@id", "T_A_ID"]},
    "22": {
        "LHS": "funcScope",
        "RHS": ["@null", "EPSILON"]},
    "23": {
        "LHS": "funcBody",
        "RHS": ["T_R_OPEN_BRACE", "@statBlock", "funcBodyInner", "T_R_CLOSE_BRACE"]},
    "24": {
        "LHS": "funcBodyInner",
        "RHS": ["@id", "T_A_ID", "funcBodyDecl"]},
    "25": {
        "LHS": "funcBodyInner",
        "RHS": ["@type", "primitiveType", "varDeclTail", "funcBodyInner"]},
    "26": {
        "LHS": "funcBodyInner",
        "RHS": ["construct", "@2,1", "funcBodyStat"]},
    "27": {
        "LHS": "funcBodyInner",
        "RHS": ["EPSILON"]},
    "28": {
        "LHS": "funcBodyStat",
        "RHS": ["statementList"]},
    "29": {
        "LHS": "funcBodyDecl",
        "RHS": ["variableCont", "@assignStat", "assignOp", "expr", "@3,2", "@2,1", "T_R_SEMI_COLON", "funcBodyStat"]},
    "30": {
        "LHS": "funcBodyDecl",
        "RHS": ["varDeclTail", "funcBodyInner"]},
    "31": {
        "LHS": "varDeclTail",
        "RHS": ["@varDecl", "@id", "T_A_ID", "@dimList", "arraySize", "@4,2", "@2,1", "T_R_SEMI_COLON"]},
    "32": {
        "LHS": "construct",
        "RHS": ["@forStat", "T_R_FOR", "T_R_OPEN_PARENTHESIS", "@type", "type", "@id", "T_A_ID", "assignOp", "expr", "T_R_SEMI_COLON", "@relExpr", "relExpr", "T_R_SEMI_COLON", "@assignStat", "assignStat", "T_R_CLOSE_PARENTHESIS", "@statBlock", "statBlock", "@7,1", "T_R_SEMI_COLON"]},
    "33": {
        "LHS": "construct",
        "RHS": ["@ifStat", "T_R_IF", "T_R_OPEN_PARENTHESIS", "expr", "T_R_CLOSE_PARENTHESIS", "T_R_THEN", "@statBlock", "statBlock", "T_R_ELSE", "@statBlock", "statBlock", "@4,1", "T_R_SEMI_COLON"]},
    "34": {
        "LHS": "construct",
        "RHS": ["@getStat", "T_R_GET", "T_R_OPEN_PARENTHESIS", "variable", "@2,1", "T_R_CLOSE_PARENTHESIS", "T_R_SEMI_COLON"]},
    "35": {
        "LHS": "construct",
        "RHS": ["@putStat", "T_R_PUT", "T_R_OPEN_PARENTHESIS", "expr", "@2,1", "T_R_CLOSE_PARENTHESIS", "T_R_SEMI_COLON"]},
    "36": {
        "LHS": "construct",
        "RHS": ["@returnStat", "T_R_RETURN", "T_R_OPEN_PARENTHESIS", "expr", "@2,1", "T_R_CLOSE_PARENTHESIS", "T_R_SEMI_COLON"]},
    "37": {
        "LHS": "statement",
        "RHS": ["@assignStat", "assignStat", "@2,1", "T_R_SEMI_COLON"]},
    "38": {
        "LHS": "statement",
        "RHS": ["construct", "@2,1"]},
    "39": {
        "LHS": "statementList",
        "RHS": ["statement", "statementList"]},
    "40": {
        "LHS": "statementList",
        "RHS": ["EPSILON"]},
    "41": {
        "LHS": "assignStat",
        "RHS": ["variable", "assignOp", "expr", "@3,1"]},
    "42": {
        "LHS": "statBlock",
        "RHS": ["T_R_OPEN_BRACE", "statementList", "T_R_CLOSE_BRACE"]},
    "43": {
        "LHS": "statBlock",
        "RHS": ["statement"]},
    "44": {
        "LHS": "statBlock",
        "RHS": ["EPSILON"]},
    "45": {
        "LHS": "expr",
        "RHS": ["arithExpr", "exprTail"]},
    "46": {
        "LHS": "exprTail",
        "RHS": ["@relExpr", "@relOp", "relOp", "arithExpr", "@4,2"]},
    "47": {
        "LHS": "exprTail",
        "RHS": ["EPSILON"]},
    "48": {
        "LHS": "relExpr",
        "RHS": ["arithExpr", "@relOp", "relOp", "arithExpr", "@4,1"]},
    "49": {
        "LHS": "arithExpr",
        "RHS": ["term", "arithExprTail"]},
    "50": {
        "LHS": "arithExprTail",
        "RHS": ["@addOp", "addOp", "term", "@3,2", "arithExprTail"]},
    "51": {
        "LHS": "arithExprTail",
        "RHS": ["EPSILON"]},
    "52": {
        "LHS": "sign",
        "RHS": ["@sign", "T_R_MINUS"]},
    "53": {
        "LHS": "sign",
        "RHS": ["@sign", "T_R_PLUS"]},
    "54": {
        "LHS": "term",
        "RHS": ["factor", "termTail"]},
    "55": {
        "LHS": "termTail",
        "RHS": ["@multOp", "multOp", "factor", "@3,2", "termTail"]},
    "56": {
        "LHS": "termTail",
        "RHS": ["EPSILON"]},
    "57": {
        "LHS": "factor",
        "RHS": ["T_R_OPEN_PARENTHESIS", "arithExpr", "T_R_CLOSE_PARENTHESIS"]},
    "58": {
        "LHS": "factor",
        "RHS": ["@num", "T_A_FLOAT"]},
    "59": {
        "LHS": "factor",
        "RHS": ["@num", "T_A_INTEGER"]},
    "60": {
        "LHS": "factor",
        "RHS": ["@not", "T_R_NOT", "factor", "@2,1"]},
    "61": {
        "LHS": "factor",
        "RHS": ["@var", "varOrFunc"]},
    "62": {
        "LHS": "factor",
        "RHS": ["sign", "factor", "@2,1"]},
    "63": {
        "LHS": "varOrFunc",
        "RHS": ["@id", "T_A_ID", "varOrFuncEval", "@2,1", "idnest"]},
    "64": {
        "LHS": "varOrFuncEval",
        "RHS": ["@dataMember", "variableTail"]},
    "65": {
        "LHS": "varOrFuncEval",
        "RHS": ["@fCall", "@aParams", "functionCallTail"]},
    "66": {
        "LHS": "variableTail",
        "RHS": ["@indexList", "indice", "@3,2"]},
    "67": {
        "LHS": "functionCallTail",
        "RHS": ["T_R_OPEN_PARENTHESIS", "aParams", "@3,2", "T_R_CLOSE_PARENTHESIS"]},
    "68": {
        "LHS": "idnest",
        "RHS": ["T_R_DOT", "varOrFunc"]},
    "69": {
        "LHS": "idnest",
        "RHS": ["EPSILON"]},
    "70": {
        "LHS": "variable",
        "RHS": ["@id", "T_A_ID", "variableCont"]},
    "71": {
        "LHS": "variableCont",
        "RHS": ["@dataMember", "variableTail", "variableCont2", "@2,2"]},
    "72": {
        "LHS": "variableCont",
        "RHS": ["@fCall", "@aParams", "functionCallTail", "functionCallTrap", "@2,2"]},
    "73": {
        "LHS": "variableCont2",
        "RHS": ["T_R_DOT", "@id", "T_A_ID", "variableCont"]},
    "74": {
        "LHS": "variableCont2",
        "RHS": ["@var", "EPSILON"]},
    "75": {
        "LHS": "functionCallTrap",
        "RHS": ["T_R_DOT", "@id", "T_A_ID", "variableCont"]},
    "76": {
        "LHS": "indice",
        "RHS": ["T_R_OPEN_BRACKET", "arithExpr", "@2,1", "T_R_CLOSE_BRACKET", "indice"]},
    "77": {
        "LHS": "indice",
        "RHS": ["EPSILON"]},
    "78": {
        "LHS": "arraySize",
        "RHS": ["T_R_OPEN_BRACKET", "@num", "T_A_INTEGER", "@2,1", "T_R_CLOSE_BRACKET", "arraySize"]},
    "79": {
        "LHS": "arraySize",
        "RHS": ["EPSILON"]},
    "80": {
        "LHS": "type",
        "RHS": ["T_A_ID"]},
    "81": {
        "LHS": "type",
        "RHS": ["primitiveType"]},
    "82": {
        "LHS": "primitiveType",
        "RHS": ["T_R_FLOAT"]},
    "83": {
        "LHS": "primitiveType",
        "RHS": ["T_R_INT"]},
    "84": {
        "LHS": "fParams",
        "RHS": ["@fparam", "@type", "type", "@id", "T_A_ID", "@dimList", "arraySize", "@4,1", "@2,1", "fParamsTail"]},
    "85": {
        "LHS": "fParams",
        "RHS": ["EPSILON"]},
    "86": {
        "LHS": "aParams",
        "RHS": ["expr", "@2,1", "aParamsTail"]},
    "87": {
        "LHS": "aParams",
        "RHS": ["EPSILON"]},
    "88": {
        "LHS": "fParamsTail",
        "RHS": ["T_R_COMMA", "@fparam", "@type", "type", "@id", "T_A_ID", "@dimList", "arraySize", "@4,1", "@2,1", "fParamsTail"]},
    "89": {
        "LHS": "fParamsTail",
        "RHS": ["EPSILON"]},
    "90": {
        "LHS": "aParamsTail",
        "RHS": ["T_R_COMMA", "expr", "aParamsTail"]},
    "91": {
        "LHS": "aParamsTail",
        "RHS": ["EPSILON"]},
    "92": {
        "LHS": "assignOp",
        "RHS": ["T_R_EQUALS"]},
    "93": {
        "LHS": "relOp",
        "RHS": ["T_R_GREATER_THAN"]},
    "94": {
        "LHS": "relOp",
        "RHS": ["T_R_GREATER_THAN_OR_EQUAL"]},
    "95": {
        "LHS": "relOp",
        "RHS": ["T_R_IS_EQUALS"]},
    "96": {
        "LHS": "relOp",
        "RHS": ["T_R_LESS_THAN"]},
    "97": {
        "LHS": "relOp",
        "RHS": ["T_R_LESS_THAN_OR_EQUAL"]},
    "98": {
        "LHS": "relOp",
        "RHS": ["T_R_LESS_THAN_OR_GREATER_THAN"]},
    "99": {
        "LHS": "addOp",
        "RHS": ["T_R_MINUS"]},
    "100": {
        "LHS": "addOp",
        "RHS": ["T_R_OR"]},
    "101": {
        "LHS": "addOp",
        "RHS": ["T_R_PLUS"]},
    "102": {
        "LHS": "multOp",
        "RHS": ["T_R_AND"]},
    "103": {
        "LHS": "multOp",
        "RHS": ["T_R_DIVIDE"]},
    "104": {
        "LHS": "multOp",
        "RHS": ["T_R_MULTIPLY"]},
}
