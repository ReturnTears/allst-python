class PublicDemo:
    def __init__(self):
        self.pub = 'Public'
    
    def public_mth(self):
        return 'Public Method'

d = PublicDemo()
print(d.pub)
print(d.public_mth())

