# 1. Upar wale Agent project mein ek teesra tool add karo: ReverseTool jo string ulta kare.
class ReverseTool():

    def __init__(self):
        super().__init__('reverse', 'Reverse the string')

    def run(self, text):
        return text[::-1]


print(ReverseTool().run('Hello, world!'))
