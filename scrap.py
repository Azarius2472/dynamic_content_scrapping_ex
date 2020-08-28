import sys  
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWidgets import QApplication  
  
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  
  
url = 'https://enter.unn.ru/preport/stat/index.php?list=1&level=2&spec=281474976711225&fac=281474976710980&fin=281474976719885&form=0'  
r = Render(url)  
html = r.frame.toHtml()
print(html)  