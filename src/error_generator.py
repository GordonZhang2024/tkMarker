#!/usr/bin/env python3

"""
Module error_generator
======================

Generate a Markdown syntax error or warning.
"""

class ErrorGenerator:
    """
    Class ErrorGenerator
    ====================

    The error generator for tkMarker.
    """
    def generate(self, level: int, text: str):
        """
        Function generate()
        ===================

        Generate an error.
        """
        match level:
            case 0:
                self.print('WARNING ')
            case 1:
                self.print('ERROR')
        self.print(text, '\n')
    def print(self, *values):
        print(values, flush=True, end='')

