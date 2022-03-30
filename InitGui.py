

class SubWorkbench(Workbench):

    def __init__(self):

        from pathlib import Path
        import welcom
        self.__class__.Icon = str(Path(welcom.__file__).parent.absolute()  / 'sub.svg')
        self.__class__.MenuText = "SSSSSSS"
        self.__class__.ToolTip = "Sub Workbench"

    def Initialize(self):
        print('ssssss started')

    def Activated(self):
        print('sssss activated')

Gui.addWorkbench(SubWorkbench())
