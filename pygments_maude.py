"This module provides Pygments lexers for the Maude language and its interactive environment. "
"Copyright https://github.com/pthariensflame/pygments-maude"

from pygments.lexer import RegexLexer, words, bygroups, using
from pygments.token import *

__all__ = ['MaudeLexer']

class MaudeLexer(RegexLexer):
    "A Pygments lexer for the Maude language."

    name = 'Maude'
    aliases = ['maude']
    filenames = ['*.maude']
    mimetypes = ['text/x-maude']

    tokens = {
        'root': [
            (r'\*\*\*\(', Comment.Multiline, 'multiline-comment'),
            (r'(?:\*\*\*|---).*?$', Comment.Single),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r'\s+', Whitespace),
            (words([
                ",",
                "(",
                ")",
                "[",
                "]",
                "{",
                "}",
            ],
                   prefix=r'(?:(?<!\`)|^)',
                   suffix=r'(?:(?!\`)|$)'),
             Punctuation),
            (r"(?:(?<=[\s,\(\)\[\]\{\}])|^)\.(?:(?=[\s,\(\)\[\]\{\}])|$)", Punctuation),
            (words([
                "&",
                "abort",
                "advise",
                "advisories",
                "advisory",
                "alias",
                "aliases",
                "all",
                "assoc",
                "associative",
                "attr",
                "attribute",
                "body",
                "break",
                "breakdown",
                "cd",
                "clear",
                "cmd",
                "color",
                "comm",
                "command",
                "commutative",
                "components",
                "conceal",
                "cond",
                "condition",
                "config",
                "configuration",
                "constructor",
                "cont",
                "continue",
                "ctor",
                "debug",
                "deselect",
                "ditto",
                "do",
                "e",
                "E",
                "eof",
                "erew",
                "erewrite",
                "ex",
                "exclude",
                "extend",
                "extending",
                "flat",
                "flattened",
                "format",
                "frew",
                "frewrite",
                "from",
                "frozen",
                "gather",
                "gc",
                "get",
                "graph",
                "id-hook",
                "id:",
                "idem",
                "idempotent",
                "identity:",
                "in",
                "inc",
                "include",
                "including",
                "irredundant",
                "is",
                "iter",
                "iterated",
                "kinds",
                "left",
                "load",
                "loop",
                "ls",
                "match",
                "memo",
                "message",
                "metadata",
                "mixfix",
                "module",
                "modules",
                "msg",
                "newline",
                "nonexec",
                "norm",
                "normalize",
                "number",
                "obj",
                "object",
                "off",
                "on",
                "op-hook",
                "otherwise",
                "owise",
                "paren",
                "parens",
                "parentheses",
                "parse",
                "path",
                "poly",
                "polymorphic",
                "popd",
                "pr",
                "prec",
                "precedence",
                "print",
                "profile",
                "protect",
                "protecting",
                "push",
                "pwd",
                "q",
                "quit",
                "rat",
                "rational",
                "red",
                "reduce",
                "resume",
                "reveal",
                "rew",
                "rewrite",
                "right",
                "s.t.",
                "search",
                "select",
                "set",
                "show",
                "special",
                "stats",
                "step",
                "strat",
                "strategy",
                "subst",
                "substitution",
                "such",
                "summary",
                "term-hook",
                "that",
                "timing",
                "to",
                "trace",
                "unify",
                "variant",
                "variants",
                "verbose",
                "views",
                "where",
                "whole",
                "with",
                "xmatch",
            ],
                   prefix=r'(?:(?<=[\s,\(\)\[\]\{\}])|^)',
                   suffix=r'(?:(?=[\s,\(\)\[\]\{\}])|$)'),
             Keyword),
            (words([
                "endfm",
                "endfth",
                "endm",
                "endth",
                "endv",
                "fmod",
                "fth",
                "mod",
                "th",
                "view",
            ],
                   prefix=r'(?:(?<=[\s,\(\)\[\]\{\}])|^)',
                   suffix=r'(?:(?=[\s,\(\)\[\]\{\}])|$)'),
             Keyword.Namespace),
            (words([
                "=/=",
                "==",
                "BOOL",
                "BOOL-OPS",
                "Bool",
                "EXT-BOOL",
                "TRUTH",
                "TRUTH-VALUE",
                "_=/=_",
                "_==_",
                "_and-then_",
                "_and_",
                "_implies_",
                "_or-else_",
                "_or_",
                "_xor_",
                "and",
                "and-then",
                "else",
                "false",
                "fi",
                "if",
                "if_then_else_fi",
                "implies",
                "not",
                "not_",
                "or",
                "or-else",
                "then",
                "true",
                "xor",
            ],
                   prefix=r'(?:(?<=[\s,\(\)\[\]\{\}])|^)',
                   suffix=r'(?:(?=[\s,\(\)\[\]\{\}])|$)'),
             Keyword.Pseudo),
            (words([
                "ceq",
                "ceqs",
                "cmb",
                "cmbs",
                "cq",
                "crl",
                "crls",
                "eq",
                "eqs",
                "label",
                "labels",
                "mb",
                "mbs",
                "op",
                "ops",
                "rl",
                "rls",
                "rule",
                "rules",
                "sort",
                "sorts",
                "subsort",
                "subsorts",
                "var",
                "vars",
            ],
                   prefix=r'(?:(?<=[\s,\(\)\[\]\{\}])|^)',
                   suffix=r'(?:(?=[\s,\(\)\[\]\{\}])|$)'),
             Keyword.Declaration),
            (words([
                "->",
                ":",
                ":=",
                "*",
                "/\\",
                "+",
                "<",
                "<=?",
                "=?",
                "=",
                "=>",
                "~>",
            ],
                   prefix=r'(?:(?<=[\s,\(\)\[\]\{\}])|^)',
                   suffix=r'(?:(?=[\s,\(\)\[\]\{\}])|$)'),
             Operator),
            (r'[+-]?[0-9]+', Number.Integer),
            (r'[^\s,\(\)\[\]\{\}]+', Name),
        ],
        'multiline-comment': [
            (r'[^\(\)]+', Comment.Multiline),
            (r'\(', Comment.Multiline, '#push'),
            (r'\)', Comment.Multiline, '#pop'),
        ],
    }

class MaudeLogLexer(RegexLexer):
    "A Pygments lexer for Maude interaction logs."

    name = 'MaudeLog'
    aliases = ['maude-log']
    filenames = ['*.maude-log']
    alias_filenames = ['*.txt',
                       '*.log']
    mimetypes = ['text/plain']

    tokens = {
        'root': [
            (r'^((?:Maude)?>)(.*?)$', bygroups(Generic.Prompt,
                                               using(MaudeLexer))),
            (r'^.+?$', Generic.Output),
        ],
    }
