from dataclasses import FrozenInstanceError

from singleton import NormalSingleton, LobustSingleton


if __name__ == '__main__':
    # NormalSingletonでのインスタンス変数の書き換え挙動
    ns: NormalSingleton = NormalSingleton(value1=1, value2=3)
    print(f'NormalSingleton first construct: value1 = {ns.value1}, value2 = {ns.value2}')

    ns1: NormalSingleton = NormalSingleton(value1=3, value2=4)
    print(f'NormalSingleton second construct: value1 = {ns1.value1}, value2 = {ns1.value2}')

    assert (ns.value1 == ns1.value1 and ns.value2 == ns1.value2), 'not same value'

    ns.value1 = 5
    print(f'NormalSingleton assign value1: value1 = {ns.value1}, value2 = {ns.value2}')

    # LobustSingletonでのインスタンス変数の書き換え挙動
    ls: LobustSingleton = LobustSingleton(value1=1, value2=3)
    print(f'LobustSingleton first colstruct: value1 = {ls.value1}, value2 = {ls.value2}')

    try:
        # 違う変数でコンストラクトする場合は、TypeErrorで例外キャッチ
        ls1: LobustSingleton = LobustSingleton(value1=3, value2=4)
    except TypeError as e:
        print(f'ERROR: {e}')

    try:
        # 外部からインスタンス変数を書き換える場合は、frozenでブロック
        ls.value1 = 5
    except FrozenInstanceError as e:
        print(f'ERROR: {e}')
