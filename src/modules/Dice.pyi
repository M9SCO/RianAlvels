class Dice:

    def __init__(self, throw: int, face: int, retain_f: callable(list[int]) = None,
                 retain_n: int | None = None) -> None:
        ...

    def __repr__(self) -> str: ...

    def to_str(self,
               view_retains:bool=False,
               startswith_retain:str='',
               endswith_retain:str=''): ...

    @property
    def throw(self) -> int: ...

    @property
    def face(self) -> int: ...

    @property
    def retains(self) -> None | list[int]: ...

    @property
    def result(self) -> int | list[int]: ...

    @property
    def _all_result(self) -> list[int]: ...

    def _get_retains(self) -> None | list[int]: ...
