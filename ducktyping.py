class pycharm():
    def __init__(self):
        print('i am init')
    def execute(self):
        print('code executed')
        print('code has succesfully compiled in 0.01 seec')
class vscode(pycharm):
    def execute(self):
        super()
        print('yeaah its compiled')
        print('code is running with no errors')
        print('error')                
class laptop():
    def code(self,ide):
        ide.execute()
lap1=laptop()   
ide=vscode()
lap1.code(ide)             
