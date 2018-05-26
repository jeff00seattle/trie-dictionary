# -*- coding: utf-8 -*-

from .trie import Trie

try:
    _basestring = basestring
except NameError:
    _basestring = str

class StringTrie(Trie):
    """:class:`Trie` variant accepting strings with a separator as keys.

    The trie accepts strings as keys which are split into components using
    a separator specified during initialisation ("/" by default).

    Canonical example where this class can be used is when keys are paths.  For
    example, it could map from a path to a request handler::

        def handle_root(): pass
        def handle_admin(): pass
        def handle_admin_images(): pass

        handlers = StringTrie()
        handlers[''] = handle_root
        handlers['/admin'] = handle_admin
        handlers['/admin/images'] = handle_admin_images

        request_path = '/admin/images/foo'

        handler = handlers.longest_prefix(request_path)
    """

    def __init__(self, *args, **kwargs):
        """Initialises the trie.

        Except for a ``separator`` named argument, all other arguments are
        interpreted the same way :func:`Trie.update` interprets them.

        Args:
            *args: Passed to super class initialiser.
            **kwargs: Passed to super class initialiser.
            separator: A separator to use when splitting keys into paths used by
                the trie.  "/" is used if this argument is not specified.  This
                named argument is not specified on the function's prototype
                because of Python's limitations.
        """
        separator = kwargs.pop('separator', '/')
        if not isinstance(separator, _basestring):
            raise TypeError('separator must be a string')
        if not separator:
            raise ValueError('separator can not be empty')
        self._separator = separator
        super(StringTrie, self).__init__(*args, **kwargs)

    @classmethod
    def fromkeys(cls, keys, value=None, separator='/'):  # pylint: disable=arguments-differ
        trie = cls(separator=separator)
        for key in keys:
            trie[key] = value
        return trie

    def _path_from_key(self, key):
        return key.split(self._separator)

    def _key_from_path(self, path):
        return self._separator.join(path)