import _random
import sys
from _typeshed import SupportsLenAndGetItem
from collections.abc import Callable, Iterable, MutableSequence, Sequence, Set as AbstractSet
from fractions import Fraction
from typing import Any, ClassVar, NoReturn, TypeVar

if sys.version_info >= (3, 9):
    __all__ = [
        "Random",
        "SystemRandom",
        "betavariate",
        "choice",
        "choices",
        "expovariate",
        "gammavariate",
        "gauss",
        "getrandbits",
        "getstate",
        "lognormvariate",
        "normalvariate",
        "paretovariate",
        "randbytes",
        "randint",
        "random",
        "randrange",
        "sample",
        "seed",
        "setstate",
        "shuffle",
        "triangular",
        "uniform",
        "vonmisesvariate",
        "weibullvariate",
    ]
else:
    __all__ = [
        "Random",
        "seed",
        "random",
        "uniform",
        "randint",
        "choice",
        "sample",
        "randrange",
        "shuffle",
        "normalvariate",
        "lognormvariate",
        "expovariate",
        "vonmisesvariate",
        "gammavariate",
        "triangular",
        "gauss",
        "betavariate",
        "paretovariate",
        "weibullvariate",
        "getstate",
        "setstate",
        "getrandbits",
        "choices",
        "SystemRandom",
    ]

_T = TypeVar("_T")

class Random(_random.Random):
    VERSION: ClassVar[int]
    def __init__(self, x: Any = ...) -> None: ...
    # Using other `seed` types is deprecated since 3.9 and removed in 3.11
    if sys.version_info >= (3, 9):
        def seed(self, a: float | str | bytes | bytearray | None = ..., version: int = ...) -> None: ...  # type: ignore[override]
    else:
        def seed(self, a: Any = ..., version: int = ...) -> None: ...

    def getstate(self) -> tuple[Any, ...]: ...
    def setstate(self, state: tuple[Any, ...]) -> None: ...
    def getrandbits(self, __k: int) -> int: ...
    def randrange(self, start: int, stop: int | None = ..., step: int = ...) -> int: ...
    def randint(self, a: int, b: int) -> int: ...
    if sys.version_info >= (3, 9):
        def randbytes(self, n: int) -> bytes: ...

    def choice(self, seq: SupportsLenAndGetItem[_T]) -> _T: ...
    def choices(
        self,
        population: SupportsLenAndGetItem[_T],
        weights: Sequence[float | Fraction] | None = ...,
        *,
        cum_weights: Sequence[float | Fraction] | None = ...,
        k: int = ...,
    ) -> list[_T]: ...
    if sys.version_info >= (3, 11):
        def shuffle(self, x: MutableSequence[Any]) -> None: ...
    else:
        def shuffle(self, x: MutableSequence[Any], random: Callable[[], float] | None = ...) -> None: ...
    if sys.version_info >= (3, 11):
        def sample(self, population: Sequence[_T], k: int, *, counts: Iterable[int] | None = ...) -> list[_T]: ...
    elif sys.version_info >= (3, 9):
        def sample(
            self, population: Sequence[_T] | AbstractSet[_T], k: int, *, counts: Iterable[int] | None = ...
        ) -> list[_T]: ...
    else:
        def sample(self, population: Sequence[_T] | AbstractSet[_T], k: int) -> list[_T]: ...

    def random(self) -> float: ...
    def uniform(self, a: float, b: float) -> float: ...
    def triangular(self, low: float = ..., high: float = ..., mode: float | None = ...) -> float: ...
    def betavariate(self, alpha: float, beta: float) -> float: ...
    def expovariate(self, lambd: float) -> float: ...
    def gammavariate(self, alpha: float, beta: float) -> float: ...
    if sys.version_info >= (3, 11):
        def gauss(self, mu: float = ..., sigma: float = ...) -> float: ...
        def normalvariate(self, mu: float = ..., sigma: float = ...) -> float: ...
    else:
        def gauss(self, mu: float, sigma: float) -> float: ...
        def normalvariate(self, mu: float, sigma: float) -> float: ...

    def lognormvariate(self, mu: float, sigma: float) -> float: ...
    def vonmisesvariate(self, mu: float, kappa: float) -> float: ...
    def paretovariate(self, alpha: float) -> float: ...
    def weibullvariate(self, alpha: float, beta: float) -> float: ...

# SystemRandom is not implemented for all OS's; good on Windows & Linux
class SystemRandom(Random):
    def getrandbits(self, k: int) -> int: ...  # k can be passed by keyword
    def getstate(self, *args: Any, **kwds: Any) -> NoReturn: ...
    def setstate(self, *args: Any, **kwds: Any) -> NoReturn: ...

# ----- random function stubs -----

_inst: Random = ...
seed = _inst.seed
random = _inst.random
uniform = _inst.uniform
triangular = _inst.triangular
randint = _inst.randint
choice = _inst.choice
randrange = _inst.randrange
sample = _inst.sample
shuffle = _inst.shuffle
choices = _inst.choices
normalvariate = _inst.normalvariate
lognormvariate = _inst.lognormvariate
expovariate = _inst.expovariate
vonmisesvariate = _inst.vonmisesvariate
gammavariate = _inst.gammavariate
gauss = _inst.gauss
betavariate = _inst.betavariate
paretovariate = _inst.paretovariate
weibullvariate = _inst.weibullvariate
getstate = _inst.getstate
setstate = _inst.setstate
getrandbits = _inst.getrandbits
if sys.version_info >= (3, 9):
    randbytes = _inst.randbytes
