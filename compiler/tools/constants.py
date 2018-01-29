# T_A: Tokens for Atomic Lexical Elements
T_A_ID = "T_A_ID"
T_A_INTEGER = "T_A_INTEGER"
T_A_FLOAT = "T_A_FLOAT"

# T_R: Tokens for Reserved Keywords and Operators
T_R_EQUALS = "T_R_EQUALS"
T_R_IS_EQUALS = "T_R_IS_EQUALS"
T_R_LESS_THAN = "T_R_LESS_THAN"
T_R_LESS_THAN_OR_GREATER_THAN = "T_R_LESS_THAN_OR_GREATER_THAN"
T_R_LESS_THAN_OR_EQUAL = "T_R_LESS_THAN_OR_EQUAL"
T_R_GREATER_THAN = "T_R_GREATER_THAN"
T_R_GREATER_THAN_OR_EQUAL = "T_R_GREATER_THAN_OR_EQUAL"
T_R_SEMI_COLON = "T_R_SEMI_COLON"
T_R_COMMA = "T_R_COMMA"
T_R_DOT = "T_R_DOT"
T_R_COLON = "T_R_COLON"
T_R_DOUBLE_COLON = "T_R_DOUBLE_COLON"
T_R_PLUS = "T_R_PLUS"
T_R_MINUS = "T_R_MINUS"
T_R_MULTIPLY = "T_R_MULTIPLY"
T_R_LINE_COMMENT = "T_R_LINE_COMMENT"
T_R_BLOCK_COMMENT = "T_R_BLOCK_COMMENT"
T_R_DIVIDE = "T_R_DIVIDE"
T_R_OPEN_PARENTHESIS = "T_R_OPEN_PARENTHESIS"
T_R_CLOSE_PARENTHESIS = "T_R_CLOSE_PARENTHESIS"
T_R_OPEN_BRACE = "T_R_OPEN_BRACE"
T_R_CLOSE_BRACE = "T_R_CLOSE_BRACE"
T_R_OPEN_BRACKET = "T_R_OPEN_BRACKET"
T_R_CLOSE_BRACKET = "T_R_CLOSE_BRACKET"
T_R_AND = "T_R_AND"
T_R_NOT = "T_R_NOT"
T_R_OR = "T_R_OR"
T_R_IF = "T_R_IF"
T_R_THEN = "T_R_THEN"
T_R_ELSE = "T_R_ELSE"
T_R_FOR = "T_R_FOR"
T_R_CLASS = "T_R_CLASS"
T_R_INT = "T_R_INT"
T_R_FLOAT = "T_R_FLOAT"
T_R_GET = "T_R_GET"
T_R_PUT = "T_R_PUT"
T_R_RETURN = "T_R_RETURN"
T_R_PROGRAM = "T_R_PROGRAM"

# T_E: Tokens for Error Conditions
T_E_LEADING_ZERO = "T_E_LEADING_ZERO"
T_E_TRAILING_ZERO = "T_E_TRAILING_ZERO"
T_E_FLOAT_FORMAT = "T_E_FLOAT_FORMAT"
T_E_BLOCK_COMMENT_FORMAT = "T_E_BLOCK_COMMENT_FORMAT"
T_E_UNEXPECTED_FORMAT = "T_E_UNEXPECTED_FORMAT"

# Reserved identifiers
RESERVED_IDS = {
    "and": T_R_AND,
    "not": T_R_NOT,
    "or": T_R_OR,
    "if": T_R_IF,
    "then": T_R_THEN,
    "else": T_R_ELSE,
    "for": T_R_FOR,
    "class": T_R_CLASS,
    "int": T_R_INT,
    "float": T_R_FLOAT,
    "get": T_R_GET,
    "put": T_R_PUT,
    "return": T_R_RETURN,
    "program": T_R_PROGRAM
}
