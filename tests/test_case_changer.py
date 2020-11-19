import pytest

from case_changer import *

__author__ = 'Philipp Tempel'
__email__ = 'python@philipptempel.me'


@pytest.mark.parametrize(
        ('inpt', 'expected'),
        (
                ('test', 'test'),
                ('test string', 'testString'),
                ('Test String', 'testString'),
                ('TestV2', 'testV2'),
                ('_foo_bar_', 'fooBar'),
                ('version 1.2.10', 'version_1_2_10'),
                ('version 1.21.0', 'version_1_21_0'),
        )
)
def test_camel_case(inpt: str, expected: str):
    assert camel_case(inpt) == expected


@pytest.mark.parametrize(
        ('inpt', 'expected'),
        (
                ("", ""),
                ("test", "Test"),
                ("test string", "Test String"),
                ("Test String", "Test String"),
                ("TestV2", "Test V2"),
                ("version 1.2.10", "Version 1 2 10"),
                ("version 1.21.0", "Version 1 21 0"),
        )
)
def test_capital_case(inpt: str, expected: str):
    assert capital_case(inpt) == expected


@pytest.mark.parametrize(
        ('inpt', 'expected'),
        (
                ("", ""),
                ("test", "TEST"),
                ("test string", "TEST_STRING"),
                ("Test String", "TEST_STRING"),
                ("dot.case", "DOT_CASE"),
                ("path/case", "PATH_CASE"),
                ("TestV2", "TEST_V2"),
                ("version 1.2.10", "VERSION_1_2_10"),
                ("version 1.21.0", "VERSION_1_21_0"),
        )
)
def test_constant_case(inpt: str, expected: str):
    assert constant_case(inpt) == expected


@pytest.mark.parametrize(
        ('inpt', 'expected'),
        (
                ("", ""),
                ("test", "test"),
                ("test string", "test.string"),
                ("Test String", "test.string"),
                ("dot.case", "dot.case"),
                ("path/case", "path.case"),
                ("TestV2", "test.v2"),
                ("version 1.2.10", "version.1.2.10"),
                ("version 1.21.0", "version.1.21.0"),
        )
)
def test_dot_case(inpt: str, expected: str):
    assert dot_case(inpt) == expected


@pytest.mark.parametrize(
        ('inpt', 'expected'),
        (
                ("", ""),
                ("test", "Test"),
                ("test string", "Test-String"),
                ("Test String", "Test-String"),
                ("TestV2", "Test-V2"),
                ("version 1.2.10", "Version-1-2-10"),
                ("version 1.21.0", "Version-1-21-0"),
        )
)
def test_header_case(inpt: str, expected: str):
    assert header_case(inpt) == expected


@pytest.mark.parametrize(
        ('inpt', 'expected'),
        (
                # Single words.
                ("test", "test"),
                ("TEST", "test"),
                # Camel case.
                ("testString", "test string"),
                ("testString123", "test string123"),
                ("testString_1_2_3", "test string 1 2 3"),
                ("x_256", "x 256"),
                ("anHTMLTag", "an html tag"),
                ("ID123String", "id123 string"),
                ("Id123String", "id123 string"),
                ("foo bar123", "foo bar123"),
                ("a1bStar", "a1b star"),
                # Constant case.
                ("CONSTANT_CASE ", "constant case"),
                ("CONST123_FOO", "const123 foo"),
                # Random cases.
                ("FOO_bar", "foo bar"),
                ("XMLHttpRequest", "xml http request"),
                ("IQueryAArgs", "i query a args"),
                # Non-alphanumeric separators.
                ("dot.case", "dot case"),
                ("path/case", "path case"),
                ("snake_case", "snake case"),
                ("snake_case123", "snake case123"),
                ("snake_case_123", "snake case 123"),
                # Punctuation.
                ('"quotes"', "quotes"),
                # Space between number parts.
                ("version 0.45.0", "version 0 45 0"),
                ("version 0..78..9", "version 0 78 9"),
                ("version 4_99/4", "version 4 99 4"),
                # Whitespace.
                ("  test  ", "test"),
                # Number string input.
                ("something_2014_other", "something 2014 other"),
                # https://github.com/blakeembrey/change-case/issues/21
                ("amazon s3 data", "amazon s3 data"),
                ("foo_13_bar", "foo 13 bar"),
        )
)
def test_no_case(inpt: str, expected: str):
    assert no_case(inpt) == expected


@pytest.mark.parametrize(
        ('inpt', 'expected'),
        (
                ("", ""),
                ("test", "test"),
                ("test string", "test-string"),
                ("Test String", "test-string"),
                ("TestV2", "test-v2"),
                ("version 1.2.10", "version-1-2-10"),
                ("version 1.21.0", "version-1-21-0"),
        )
)
def test_param_case(inpt: str, expected: str):
    assert param_case(inpt) == expected


@pytest.mark.parametrize(
        ('inpt', 'expected'),
        (
                ("", ""),
                ("test", "Test"),
                ("test string", "TestString"),
                ("Test String", "TestString"),
                ("TestV2", "TestV2"),
                ("version 1.2.10", "Version_1_2_10"),
                ("version 1.21.0", "Version_1_21_0"),
        )
)
def test_pascal_case(inpt: str, expected: str):
    assert pascal_case(inpt) == expected


@pytest.mark.parametrize(
        ('inpt', 'expected'),
        (
                ("", ""),
                ("test", "test"),
                ("test string", "test/string"),
                ("Test String", "test/string"),
                ("TestV2", "test/v2"),
                ("version 1.2.10", "version/1/2/10"),
                ("version 1.21.0", "version/1/21/0"),
        )
)
def test_path_case(inpt: str, expected: str):
    assert path_case(inpt) == expected


@pytest.mark.parametrize(
        ('inpt', 'expected'),
        (
                ("", ""),
                ("test", "Test"),
                ("test string", "Test string"),
                ("Test String", "Test string"),
                ("TestV2", "Test v2"),
                ("version 1.2.10", "Version 1 2 10"),
                ("version 1.21.0", "Version 1 21 0"),
        )
)
def test_sentence_case(inpt: str, expected: str):
    assert sentence_case(inpt) == expected


@pytest.mark.parametrize(
        ('inpt', 'expected'),
        (
                ("", ""),
                ("_id", "id"),
                ("test", "test"),
                ("test string", "test_string"),
                ("Test String", "test_string"),
                ("TestV2", "test_v2"),
                ("version 1.2.10", "version_1_2_10"),
                ("version 1.21.0", "version_1_21_0"),
        )
)
def test_snake_case(inpt: str, expected: str):
    assert snake_case(inpt) == expected


if __name__ == "__main__":
    pytest.main()
