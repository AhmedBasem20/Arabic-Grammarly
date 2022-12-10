import xml.sax
import pandas as pd
from xml.sax.saxutils import escape
import re
articles = []

class articlesHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
      
#(?=<!)(.*)(?<=-->)
    def characters(self, content):
        if self.current == "Text":
            self.Text = content
            
    def endElement(self, name):
        if self.current == "Text":
            text=self.Text
            #text = s[s.find('سبأنت:')+len('سبأنت:'):s.rfind('سبأ')]
            articles.append(text)
            
        
handler = articlesHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('abuelkhair_dataset/Echoroukonline_utf_8.xml')

articles_df = pd.DataFrame(data=articles, columns=['articles'])
articles_df.to_csv('Echorouk_articles.csv', index=False)
print(articles_df)