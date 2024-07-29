---
id: CSCI-316_Tao-Summer-2024
aliases: []
tags:
  - problem-set
---

## Problem Sets

Collections of problems given by professor Tao.

- highly likely for questions from the book to be the exam questions.

**Summer 2024 Book**
![[Programming language pragmatics-Morgan Kaufmann.pdf]]

### Problem Set from Chapter 2

- [x] Question 2.1 A ([[regex-and-cfg]])
      Strings in C. These are delimited by double quotes ("), and may not contain
      newline characters. They may contain double-quote or backslash characters
      if and only if those characters are “escaped” by a preceding backslash.
      You may find it helpful to introduce shorthand notation to represent any
      character that is not a member of a small specified set.

      The first quote starts the matching, ([^"\\] | \\.) repeats for all characters
      that is not a double quote or escaped backslash, where the Kleene star will
      concatenate until a double quote.

      **ANSWER** "([^"\\] | \\.)\*"
