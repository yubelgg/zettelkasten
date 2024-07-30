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
> direction LR
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
