import pandas as pd

class Data():

    def __init__(self):
        self.rastCls = pd.DataFrame()
        self.kwCls = pd.DataFrame([], columns=['Category','System', 'Subsystem', 'Function'])
        self.classified = {}
        self.count = pd.DataFrame()
        self.hierarchy = {}
        self.userCls = pd.DataFrame()
        self.plots = {}
        self.breakdown = pd.DataFrame()

    def reset(self):
        self.kwCls = pd.DataFrame([], columns=['Category','System', 'Subsystem', 'Function'])
        self.classified = {}
        self.count = pd.DataFrame()
        self.userCls = pd.DataFrame()
        self.plots = {}
        self.breakdown = pd.DataFrame()

    def setRastCls(self, file):
        self.rastCls = file
    
    def setKwCls(self, file):
        self.kwCls = file

    def getRastCls(self):
        return self.rastCls

    def getKwCls(self):
        return self.kwCls

    def setClassified(self, files):
        self.classified = files

    def getClassified(self):
        return self.classified

    def setCount(self, file):
        self.count = file

    def getCount(self):
        return self.count

    def setHierarchy(self, file):
        self.hierarchy = file

    def getHierarchy(self):
        return self.hierarchy

    def setUserCls(self, file):
        self.userCls = file

    def getUserCls(self):
        return self.userCls

    def setPlots(self, file):
        self.plots = file

    def getPlots(self):
        return self.plots

    def setBreakdown(self, file):
        self.breakdown = file

    def getBreakdown(self):
        return self.breakdown