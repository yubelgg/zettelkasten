---
id: regex-and-cfg
aliases: []
tags:
  - notes
---

# Regular Expressions and Context Free Grammar

## Regular Expressions

Regular expressions (regex) are sequences of characters that define a search
pattern, primarily for use in pattern matching with strings. They are used in
many programming languages for tasks such as searching, replacing, and parsing
text. Regular expressions are particularly powerful for string manipulation and
text analysis.

Tokens are the building blocks of programs. Amount of tokens vary from language
to language.

Example of some tokens:

- keywords
- identifiers
- symbols

A regular expression is one of:

1. a character
2. the empty string
3. two regular expressions next to each other **(concatenation)**
4. two regular expressions next to each other with a pipe(|) as an **OR** operator
5. a regular expression followed by a **Kleene star**, a concatenation of zero or more strings

## Context Free Grammer

Context-free grammars (CFGs) are formal grammars used to define the syntax of
programming languages. Each of the rules in a context-free grammar is known as
a production. The symbols on the left-hand sides of the productions are known as
variables, or non-terminals.

**Terminals:** are the set of digits on the very last production

**Non-Terminals:** those that don't end the production like E, T, F

```
E -> E + T | T
T -> T * F | F
F -> ( E ) | digit
digit -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```
