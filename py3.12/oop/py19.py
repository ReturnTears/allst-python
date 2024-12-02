class ProtectedDemo:
    def __init__(self):
        self._protectedMember = "This is protected"

    def _protectedMth(self):
        return "This is protected method"

d = ProtectedDemo()
print(d._protectedMember)
print(d._protectedMth())

