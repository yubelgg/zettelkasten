---
id: CSCI-316_Tao-Summer-2024
aliases: []
tags:
  - problem-set
---

## Problem Sets

Collections of problems given by professor Tao.

- highly likely for questions from the book to be the exam questions.

> [!book]- **Summer 2024 Book**
> ![[Programming language pragmatics-Morgan Kaufmann.pdf]]

### Problem Set from Chapter 2

> [!Questions]- Question 2.1/2.2 A ([[regex-and-cfg]])
> Write regular expressions to capture the following.
> Strings in C. These are delimited by double quotes ("), and may not contain
> newline characters. They may contain double-quote or backslash characters
> if and only if those characters are “escaped” by a preceding backslash.
> You may find it helpful to introduce shorthand notation to represent any
> character that is not a member of a small specified set.
>
> The first quote starts the matching, **([^"\\] | \\.)** repeats for all characters
> that is not a double quote or escaped backslash and concatenate, where the Kleene
> star will concatenate until a double quote.
>
> **ANSWER:** `"(non-newline, ", \ | \\.)\*"` >
>
> **ANSWER:** `"([^"\\] | \\.)\*"`
>
> ```mermaid
> stateDiagram-v2
> direction LR
>
> [*] --> 1
> 1 --> 2: " (begin quote)
> 2 --> 3: newline
> 3 --> 2: \ (backslash)
> 2 --> 4: " (end quote)
> 4 --> [*]
> ```

> [!Questions]- Question 2.1/2.2 B
> Write regular expressions to capture the following.
> Comments in Pascal. These are delimited by `(* and *)` or by `{ and }`.
> They are not permitted to nest.
>
> **regex for `(* and *)`:** `\(\*[^*]*\*\)`
> Since both `(` and `*` have special meanings in regex, they need to be escaped with a `\`.
> This applies for the same for the closing `*` and the `)`.
> **`[^*]*`** will match(concatenate) characters that are not `*`, and will repeat til end.
>
> **regex for `{ and }`:** `\{[^}]*\}`
> Since `{` also have special meanings in regex, they need to be escaped with a `\`.
>
> **final regex:** `\(\*[^*]*\*\) | \{[^}]*\}`
>
> ```mermaid
> stateDiagram-v2
>
> [*] --> 1
> 1 --> 2: lparen
> 2 --> 3: asterisk
> 3 --> 3: non-asterisk
> 3 --> 4: asterisk
> 4 --> 5: rparen
> 5 --> [*]
> 4 --> 3: non-asterisk or rparen
> 1 --> 6: lbracket
> 6 --> 6: non rbracket
> 6 --> 7: rbracket
> 7 --> [*]
>
> ```

> [!Questions]- Question 2.1/2.2 C
> Numeric constants in C. These are octal, decimal, or hexadecimal integers, or
> decimal or hexadecimal floating-point values. An octal integer begins with 0,
> and may contain only the digits 0–7. A hexadecimal integer begins with 0x or
> 0X, and may contain the digits 0–9 and a/A–f/F. A decimal floating-point value
> has a fractional portion (beginning with a dot) or an exponent (beginning with
> E or e). Unlike a decimal integer, it is allowed to start with 0. A hexadecimal
> floating-point value has an optional fractional portion and a mandatory
> exponent (beginning with P or p). In either decimal or hexadecimal, there may
> be digits to the left of the dot, the right of the dot, or both, and the
> exponent itself is given in decimal, with an optional leading + or - sign. An
> integer may end with an optional U or u (indicating “unsigned”), and/or L or l
> (indicating “long”) or LL or ll (indicating “long long”). A floating-point
> value may end with an optional F or f (indicating “float”—single precision) or
> L or l (indicating “long”—double precision).
>
> > [!octal]- **Octal Integer:**
> >
> > - begins with 0 and can only contain digits 0-7.
> >
> >   **`0[0-7]+`**
> >
> > ```mermaid
> > stateDiagram-v2
> > direction LR
> >
> > [*] --> 1
> > 1 --> 2: zero
> > 2 --> 2: 0, 1, 2, 3, 4, 5, 6, 7
> > 2 --> [*]
> > ```
>
> > [!hex]- **Hexadecimal Integer:**
> >
> > - begins with 0x or 0X.
> > - may contain digits from 0-9 and a/A-f/F.
> >
> >   **`0[xX]([0-9a-fA-F]+)([uU] | [lL])`**
> >
> > ```mermaid
> > stateDiagram-v2
> >
> > [*] --> 1
> > 1 --> 2: x or X
> > 2 --> 3: 0-9 or a-f or A-F
> > 3 --> 3: 0-9 or a-f or A-F
> > 3 --> 4: u or U
> > 3 --> 6: l or L
> > 4 --> 5: l or L
> > 5 --> [*]
> > 6 --> [*]
> >
> > ```
>
> > [!dec]- **Decimal Floating-Point:**
> >
> > - has numbers on both sides of the dot.
> > - may have a exponent beginning with E or e.
> > - may begin with a 0.
> >
> >   **`(([0-9]+[.][0-9]*)|([.][0-9]+)|([0-9]+[.][0-9]+))([eE][+-]?[0-9]+)?([fFlL])?`**
> >
> > ```mermaid
> > stateDiagram-v2
> >
> > [*] --> 1
> > 1 --> 2: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
> > 2 --> 2: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
> > 2 --> 3: dot
> > 3 --> 4: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
> > 4 --> 4: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
> > 4 --> [*]
> > 4 --> 7: e or E
> > 7 --> 8: + or -
> > 8 --> 9: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
> > 9 --> 9: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
> > 9 --> [*]
> > 1 --> 5: dot
> > 5 --> 6: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
> > 6 --> 6: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
> > 6 --> [*]
> > 6 --> 10: e or E
> > 10 --> 11: + or -
> > 11 --> 12: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
> > 12 --> 12: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
> > 12 --> [*]
> > ```
>
> > [!hex]- **Hexadecimal Floating-Point:**
> >
> > - has a optional fractional portion.
> > - mandatory exponent partion (beginning with P or p).
> >
> >   **`0[xX]([0-9a-fA-F]+[.][0-9a-fA-F]*){1}([pP][+-]?[0-9]+)([fFlL])?`**
> >
> > ```mermaid
> > stateDiagram-v2
> >
> > [*] --> 1
> > 1 --> 6
> > 1 --> 2: x or X
> > 2 --> 3: 0-9 or a-f or A-F
> > 3 --> 3: 0-9 or a-f or A-F
> > 3 --> 4: dot
> > 4 --> 5: 0-9 or a-f or A-F
> > 5 --> 5: 0-9 or a-f or A-F
> > 5 --> 6: p or P
> > 6 --> 7: + or -
> > 7 --> 8: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
> > 8 --> 9: f, F, l, F
> > 9 --> [*]
> > ```

> [!questions]+ Question 2.1/2.2 D
> Floating-point constants in Ada. These match the definition of real in Example
> 2.3, except that (1) a digit is required on both sides of the decimal point, (2)
> an underscore is permitted between digits, and (3) an alternative numeric base
> may be specified by surrounding the non-exponent part of the number with pound signs,
> preceded by a base in decimal (e.g., 16#6.a7#e+2). In this latter case, the
> letters a . . f (both upper- and lowercase) are permitted as digits. Use of these
> letters in an inappropriate (e.g., decimal) number is an error, but need not be
> caught by the scanner.
