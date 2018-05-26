# -*- coding: utf-8 -*-

try:
    from trie import Trie
except ImportError:
    from .trie import Trie

class CharTrie(Trie):
    """A variant of a :class:`Trie` which accepts strings as keys.

    The only difference between :class:`CharTrie` and
    :class:`Trie` is that when :class:`CharTrie` returns keys
    back to the client (for instance in keys() method is called), those keys are
    returned as strings.

    Canonical example where this class can be used is a dictionary of words in
    a natural language.  For example::

        >>> t = CharTrie()
        >>> t['wombat'] = True
        >>> t['woman'] = True
        >>> t['man'] = True
        >>> t['manhole'] = True
        >>> t.has_subtrie('wo')
        True
        >>> t.has_key('man')
        True
        >>> t.has_subtrie('man')
        True
        >>> t.has_subtrie('manhole')
        False
    """

    def _key_from_path(self, path):
        return ''.join(path)
