# -*- coding: utf-8 -*-

import collections as _collections

from .trie import (Trie, _SENTINEL)

class PrefixSet(_collections.MutableSet):  # pylint: disable=abstract-class-not-used
    """A set of prefixes.

    :class:`pygtrie.PrefixSet` works similar to a normal set except it is said
    to contain a key if the key or it's prefix is stored in the set.  For
    instance, if "foo" is added to the set, the set contains "foo" as well as
    "foobar".

    The set supports addition of elements but does *not* support removal of
    elements.  This is because there's no obvious consistent and intuitive
    behaviour for element deletion.
    """

    def __init__(self, iterable=None, factory=Trie, **kwargs):
        """Initialises the prefix set.

        Args:
            iterable: A sequence of keys to add to the set.
            factory: A function used to create a trie used by the
                    :class:`pygtrie.PrefixSet`.
            kwargs: Additional keyword arguments passed to the factory function.
        """
        super(PrefixSet, self).__init__()
        trie = factory(**kwargs)
        if iterable:
            trie.update((key, True) for key in iterable)
        self._trie = trie

    def copy(self):
        """Returns a copy of the prefix set."""
        return self.__class__(self._trie)

    def clear(self):
        """Removes all keys from the set."""
        self._trie.clear()

    def __contains__(self, key):
        """Checks whether set contains key or its prefix."""
        return bool(self._trie.shortest_prefix(key)[1])

    def __iter__(self):
        """Return iterator over all prefixes in the set.

        See :func:`PrefixSet.iter` method for more info.
        """
        return self._trie.iterkeys()

    def iter(self, prefix=_SENTINEL):
        """Iterates over all keys in the set optionally starting with a prefix.

        Since a key does not have to be explicitly added to the set to be an
        element of the set, this method does not iterate over all possible keys
        that the set contains, but only over the shortest set of prefixes of all
        the keys the set contains.

        For example, if "foo" has been added to the set, the set contains also
        "foobar", but this method will *not* iterate over "foobar".

        If ``prefix`` argument is given, method will iterate over keys with
        given prefix only.  The keys yielded from the function if prefix is
        given does not have to be a subset (in mathematical sense) of the keys
        yielded when there is not prefix.  This happens, if the set contains
        a prefix of the given prefix.

        For example, if only "foo" has been added to the set, iter method called
        with no arguments will yield "foo" only.  However, when called with
        "foobar" argument, it will yield "foobar" only.
        """
        if prefix is _SENTINEL:
            return iter(self)
        elif self._trie.has_node(prefix):
            return self._trie.iterkeys(prefix=prefix)
        elif prefix in self:
            # Make sure the type of returned keys is consistent.
            # pylint: disable=protected-access
            return self._trie._key_from_path(self._trie._path_from_key(prefix)),
        else:
            return ()

    def __len__(self):
        """Returns number of keys stored in the set.

        Since a key does not have to be explicitly added to the set to be an
        element of the set, this method does not count over all possible keys
        that the set contains (since that would be infinity), but only over the
        shortest set of prefixes of all the keys the set contains.

        For example, if "foo" has been added to the set, the set contains also
        "foobar", but this method will *not* count "foobar".

        """
        return len(self._trie)

    def add(self, key):
        """Adds given key to the set.

        If the set already contains prefix of the key being added, this
        operation has no effect.  If the key being added is a prefix of some
        existing keys in the set, those keys are deleted and replaced by
        a single entry for the key being added.

        For example, if the set contains key "foo" adding a key "foobar" does
        not change anything.  On the other hand, if the set contains keys
        "foobar" and "foobaz", adding a key "foo" will replace those two keys
        with a single key "foo".

        This makes a difference when iterating over the keys or counting number
        of keys.  Counter intuitively, adding of a key can *decrease* size of
        the set.

        Args:
            key: Key to add.
        """
        if key not in self:
            self._trie[key:] = True

    def discard(self, key):
        raise NotImplementedError(
            'Removing keys from PrefixSet is not implemented.')

    def remove(self, key):
        raise NotImplementedError(
            'Removing keys from PrefixSet is not implemented.')

    def pop(self):
        raise NotImplementedError(
            'Removing keys from PrefixSet is not implemented.')