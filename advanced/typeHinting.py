def func(n:int) -> str:
    print(n)
    return f"My Param {n}"
    

func("jek")
# pip install mypy
# mypy typeHinting.py (For Error)

def listParam(param:list[int]):
    print(param)

listParam([1,2])