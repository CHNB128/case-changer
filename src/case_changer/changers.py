from __future__ import annotations

import re as _re
from typing import Callable, Sequence, Tuple, Union

__author__ = 'Philipp Tempel'
__email__ = 'p.tempel@tudelft.nl'

DEFAULT_STRIP_REGEXP = _re.compile(r'[^A-Z0-9]+', _re.IGNORECASE)

DEFAULT_SPLIT_REGEXP = [
        _re.compile(r'([a-z0-9])([A-Z])'),
        _re.compile(r'([A-Z])([A-Z][a-z])'),
]


def _replace(string: str,
             reg: Union[_re.Pattern, Sequence[_re.Pattern]],
             value: str) -> str:
    """
    Replace text in string using a regular expression

    Parameters
    ----------
    string : str
        Input string in which to replace text.
    reg : _re.Pattern | Sequence[_re.Pattern]
        Single pattern or sequence of patterns which to substitute. In case
        of sequence of patterns, substitutions will occur from left to right.
    value : str
        Value to use in regexp-substitution.
    Returns
    -------
    s : str
        Replaced string.
    """

    try:
        for reg_ in reg:
            string = reg_.sub(value, string)
    except TypeError:
        string = reg.sub(value, string)
    finally:
        return string


def _change_case(s: str,
                 delimiter: str,
                 transform: Union[
                     Callable[[str], str],
                     Tuple[Callable[[str], str], Callable[[str], str]],
                 ]):
    """
    Change case of words in a string separated by a certain delimiter.

    Parameters
    ----------
    s : str
         Original string with words separated by :code:`delimiter`, each of
         which is to be changed in case.
    delimiter : str
        Delimiter between words in :code:`s` to use for splitting the string
        into parts.
    transform : Callable[[str], str] | Tuple[Callable[[str], str], Callable[[
    str], str]]
        A transformation callback or a list of transformation callbacks. Each
        callback must take one argument (the original word) and return the
        case-changed word. If :code:`transform` is a single callback, then it
        will be applied to every word. This can be useful if every word
        should be e.g., upper-cased. If :code:`transform` is a tuple of two
        callbacks, then the first callback :code:`transform[0]` will be
        applied to only the first word, and the remaining words will be
        processed by the second callback :code:`transform[1]`.

    Returns
    -------
    s : str
        Case-changed string.
    """
    ss: str = _replace(
            _replace(s, DEFAULT_SPLIT_REGEXP, "\\1\0\\2"),
            DEFAULT_STRIP_REGEXP,
            "\0")

    try:
        start = 0
        end = len(ss)
        while ss[start] == "\0":
            start += 1
        while ss[end - 1] == "\0":
            end -= 1

        # split word into pieces
        words = ss[start:end].split("\0")

        if not isinstance(transform, Tuple):
            transform = (transform, transform)

        words = [transform[0](words[0])] + [transform[1](w) for w in words[1:]]

        # words = transform[0](words[0], 0) + \
        #         + [transform(w, idx) for idx, w in enumerate(words, start=1)]

        return delimiter.join(words)
    except IndexError:
        return s


def _replace_separator_by(string: str, sep: str, by: str):
    """
    Replace a given separator in the string by another value

    Parameters
    ----------
    string : str
        Input string.
    sep : str
        Separator to replace in :code:`string`.
    by : str
        Value to replace :code:`sep` with.

    Returns
    -------
    string : str
        Replaced string.
    """
    return _re.sub(r'({})'.format(sep), by, string)


def camel_case(s: str):
    """
    Transform into a string with the separator denoted by the next word
    capitalized.

    Parameters
    ----------
    s : str
        Original string to transform.

    Returns
    -------
    s : str
        Transformed string.
    """
    return _change_case(s, '', (str.lower,
                                lambda w: f'_{w}'
                                if w.isnumeric() else w.capitalize()))


def capital_case(s: str):
    """
    Transform into a space separated string with each word capitalized.

    Parameters
    ----------
    s : str
        Original string to transform.

    Returns
    -------
    s : str
        Transformed string.
    """
    return _change_case(s, ' ', str.capitalize)


def constant_case(s: str):
    """
    Transform into upper case string with an underscore between words.

    Parameters
    ----------
    s : str
        Original string to transform.

    Returns
    -------
        Transformed string.
    """
    return _change_case(s, '_', str.upper)


def dot_case(s: str):
    """
    Transform into a lower case string with a period between words.

    Parameters
    ----------
    s : str
        Original string to transform.

    Returns
    -------
        Transformed string.
    """
    return _change_case(s, '.', str.lower)


def header_case(s: str):
    """
    Transform into a dash separated string of capitalized words.

    Parameters
    ----------
    s : str
        Original string to transform.

    Returns
    -------
        Transformed string.
    """
    return _change_case(s, '-', str.capitalize)


def no_case(s: str):
    """
    Transform into a lower cased string with spaces between words.

    Parameters
    ----------
    s : str
        Original string to transform.

    Returns
    -------
        Transformed string.
    """
    return _change_case(s, ' ', str.lower)


def param_case(s: str):
    """
    Transform into a lower cased string with dashes between words.

    Parameters
    ----------
    s : str
        Original string to transform.

    Returns
    -------
        Transformed string.
    """
    return _change_case(s, '-', str.lower)


def pascal_case(s: str):
    """
    Transform into a string of capitalized words without separators.

    Parameters
    ----------
    s : str
        Original string to transform.

    Returns
    -------
        Transformed string.
    """
    return _change_case(s, '', (str.capitalize,
                                lambda w: f'_{w}'
                                if w.isnumeric() else w.capitalize()))


def path_case(s: str):
    """
    Transform into a lower case string with slashes between words.

    Parameters
    ----------
    s : str
        Original string to transform.

    Returns
    -------
        Transformed string.
    """
    return _change_case(s, '/', str.lower)


def sentence_case(s: str):
    """
    Transform into a lower case with spaces between words, then capitalize
    the string.

    Parameters
    ----------
    s : str
        Original string to transform.

    Returns
    -------
        Transformed string.
    """
    return _change_case(s, ' ', (str.capitalize, str.lower))


def snake_case(s: str):
    """
    Transform into a lower case string with underscores between words.

    Parameters
    ----------
    s : str
        Original string to transform.

    Returns
    -------
        Transformed string.
    """
    return _change_case(s, '_', str.lower)

def _to_case(case_fn):
    def convert(value):
        if type(value) == str:
            return case_fn(value)
        elif type(value) == list:
            return list(map(convert, value))
        elif type(value) == tuple:
            return tuple(map(convert, value))
        elif type(value) == set:
            return set(map(convert, value))
        elif type(value) == OrderedDict:
            _d = {}
            for k, v in value.items():
                _value = value[k]
                if type(_value) == dict:
                    _value = convert(_value)
                _d[case_fn(k)] = _value
            return _d
        elif type(value) == dict:
            _d = {}
            for k, v in value.items():
                _value = value[k]
                if type(_value) == dict:
                    _value = convert(_value)
                _d[case_fn(k)] = _value
            return _d
        else:
            return value
    return convert

to_camel = _to_case(camel_case)
to_snake = _to_case(snake_case)

__all__ = [
        'camel_case',
        'capital_case',
        'constant_case',
        'dot_case',
        'header_case',
        'no_case',
        'param_case',
        'pascal_case',
        'path_case',
        'sentence_case',
        'snake_case',
        'to_snake',
        'to_camel',
]
