from typing import Iterable, Iterator, Optional

from django.core.files.storage import Storage

def matches_patterns(path: str, patterns: Iterable[str]) -> bool: ...
def get_files(
    storage: Storage, ignore_patterns: Optional[Iterable[str]] = ..., location: str = ...
) -> Iterator[str]: ...
def check_settings(base_url: Optional[str] = ...) -> None: ...
