from dataclasses import dataclass


class NormalSingleton:
    _instance = None

    value1: int
    value2: int

    def __new__(cls, **kwargs) -> 'NormalSingleton':
        if cls._instance is None:
            cls._instance = super(NormalSingleton, cls).__new__(cls)
            for key, value in kwargs.items():
                setattr(cls._instance, key, value)

        return cls._instance


@dataclass(frozen=True)
class LobustSingleton:
    _instance = None

    value1: int
    value2: int

    def __new__(cls, **kwargs) -> 'LobustSingleton':
        if cls._instance is None:
            cls._instance = super(LobustSingleton, cls).__new__(cls)
            for key, value in kwargs.items():
                # :NOTE dataclassのfrozenで外部から書き換えをブロックしているが、
                # 初回コンストラクトしたときもFrozenInstanceErrorとなるため、
                # 親クラスの__setattr__で初回のみ書き換えを許容
                object.__setattr__(cls._instance, key, value)

        return cls._instance

    def __init__(self, **kwargs):
        if self._instance is not None:
            for key, value in kwargs.items():
                if getattr(self._instance, key) != value:
                    raise TypeError('This class is singleton. Can\'t init again')
