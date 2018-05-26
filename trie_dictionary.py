# -*- coding: utf-8 -*-

import gzip
import sys

try:
    from char_trie import CharTrie
except ImportError:
    from .char_trie import CharTrie


try:
    import termios
    import tty

    def getch():
        """Reads single character from standard input."""
        attr = termios.tcgetattr(0)
        try:
            tty.setraw(0)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(0, termios.TCSADRAIN, attr)

except ImportError:
    try:
        from msvcrt import getch  # pylint: disable=import-error
    except ImportError:
        sys.exit(0)

print("Dictionary test")
print("===============")

t = CharTrie()


print("Load Dictionary")
word_counter = 0
word_file = "words_alpha.txt.gz"
with gzip.open(word_file, 'r') as f:
    for line in f:
        word_counter += 1
        word = line.decode('ascii').rstrip()
        t[word] = True
print("Loaded Dictionary: {0}".format(word_counter))

print("Start typing...")
text = ''
while True:
    ch = getch()
    if ord(ch) < 32:
        print('Exiting')
        break

    text += ch
    value = t.get(text)
    if value is False:
        print('Exiting')
        break

    if value is not None:
        print(repr(text), 'is a word')

    if t.has_subtrie(text):
        print(repr(text), 'is a prefix of a word')
    else:
        print(repr(text), 'is not a prefix, going back to empty string')
        text = ''