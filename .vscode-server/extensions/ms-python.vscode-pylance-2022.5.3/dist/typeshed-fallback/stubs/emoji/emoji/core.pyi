from typing import Pattern
from typing_extensions import Literal

_DEFAULT_DELIMITER: str

def emojize(
    string: str,
    use_aliases: bool = ...,
    delimiters: tuple[str, str] = ...,
    variant: Literal["text_type", "emoji_type", None] = ...,
    language: str = ...,
) -> str: ...
def demojize(string: str, use_aliases: bool = ..., delimiters: tuple[str, str] = ..., language: str = ...) -> str: ...
def get_emoji_regexp(language: str = ...) -> Pattern[str]: ...
def emoji_lis(string: str, language: str = ...) -> list[dict[str, int | str]]: ...
def distinct_emoji_lis(string: str) -> list[str]: ...
def emoji_count(string: str) -> int: ...
