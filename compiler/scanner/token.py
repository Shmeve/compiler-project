import re
from compiler.tools import constants
from compiler.tools import error_messages as em


class Token:
    def __init__(self, line: int=0, column: int=0, token: str="", lexeme: str=""):
        self.line: int = line
        self.column: int = column
        self.token: str = token
        self.lexeme: str = lexeme

    def is_error(self) -> bool:
        """
        Check if current token represents an error condition.

        :return: bool
        """
        return bool(re.match('^T_E_', self.token))

    def get_error_message(self) -> str:
        """
        Return the correct error message for the current error token/state.

        :return: str
        """
        if self.token is constants.T_E_LEADING_ZERO:
            return em.T_E_LEADING_ZERO

        if self.token is constants.T_E_TRAILING_ZERO:
            return em.T_E_TRAILING_ZERO

        if self.token is constants.T_E_FLOAT_FORMAT:
            return em.T_E_FLOAT_FORMAT

        if self.token is constants.T_E_BLOCK_COMMENT_FORMAT:
            return em.T_E_BLOCK_COMMENT_FORMAT

        if self.token is constants.T_E_UNEXPECTED_CHAR:
            return em.T_E_UNEXPECTED_CHAR

        return ""
