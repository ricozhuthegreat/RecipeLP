
import math

from utils.abstract.token import Token
from utils.abstract.stratagem import Stratagem

class Naive_Sequence(Stratagem):

    # Make class iterable
    def __init__(self, start = 0):
        self.num = start

    def __init__(self, sequence, start = 0):
        self.num = start
        self.sequence = sequence
        self.tokens = []

    # Iterator methods
    def __iter__(self):
        return iter(self.tokens[self.num])

    def __next__(self):
        num = self.num
        if num < len(tokens):
            self.num += 1
        return num
    
    # Symbolic tokenization methods

    # Non-recursive implementation of a partition token generator (simple python sublist algorithm)
    def naive_tokenize(self):
        base = []   
        lists = [base]
        for i in range(len(self.sequence)): 
            orig = lists[:] 
            new = self.sequence[i] 
            for j in range(len(lists)): 
                lists[j] = lists[j] + [new]
                current_token = Token(lists[j])
            lists = orig + lists
        return lists

    def context_tokenize(self):
        pass

    def local_context_tokenize(self):
        pass

    # Universal token methods

    # Sort the self.tokens data structure by length of sublists/tokens
    def sort_tokens_length(self):
        pass