from sikuli.Sikuli import *
import os
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)
from soundCloudTestImages import *
from util import *
from regionDictionary import *

class soundCloudTest(util):
    myImages = soundCloudTestImages()

    def searchForTermsFromDataFile(self):
        for i in range(len(self.termsArr)):	
            self.searchForMusic(self.termsArr[i]," Terms from data File ")
    
    def searchForMusic(self,term,testName):
        try:
            self.clearMouse()
            self.reg.getReg("topHalf").click(self.myImages.getImage("searchButton"))
            wait(2)
            self.clearSearch()
            type(term)
            type(Key.ENTER)
            wait(4)
            if not exists(self.myImages.getImage("cantFindAnything")):
                self.passed(testName + term)				
            else:
                self.failed(testName + term)								
        except FindFailed:
            self.failed(testName + term)

    def clearSearch(self):
        try:
            self.reg.getReg("topHalf").click(self.myImages.getImage("searchButton"))
            wait(2)
            type("a",KEY_CTRL)
            type(Key.DELETE)
            wait(4)
        except FindFailed:
            self.failed("Clear Search  Field")
                           



            
    
    



    