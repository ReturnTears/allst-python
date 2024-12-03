class BaseCls:
    pass

class DerivedCls(BaseCls):
    pass

class DerivedCls2(BaseCls):
    pass

class DerivedCls3(DerivedCls, DerivedCls2):
    pass

print(DerivedCls3.__mro__)

