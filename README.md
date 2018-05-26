# trie-dictionary
Using a Trie to perform word-lookup.

## Introduction

[Trie data structure](http://en.wikipedia.org/wiki/Trie>), also known as radix
or prefix tree, is a tree associating keys to values where all the descendants
of a node have a common prefix (associated with that node).

## Example
The following loads GZip file ```words_alpha.txt.gz``` containing 370000 words to build a trie data structure.

```bash
> python3 trie_dictionary.py

Dictionary test
===============
Load Dictionary
Loaded Dictionary: 370099

Start typing...
'f' is a word
'f' is a prefix of a word
'fa' is a word
'fa' is a prefix of a word
'fal' is a prefix of a word
'fall' is a word
'fall' is a prefix of a word
'falli' is a prefix of a word
'fallin' is a prefix of a word
'falling' is a word
'falling' is a prefix of a word
Exiting
```
