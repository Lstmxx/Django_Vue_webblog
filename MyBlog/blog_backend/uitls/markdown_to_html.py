import sys
import markdown
import codecs
def md_to_html():
    filename= "C:\\Users\\Administrator\\Desktop\\vue_django学习笔记\\vue与django数据互通.md"
    input_file = codecs.open(filename,mode='r',encoding="utf-8")
    text = input_file.read()
    input_file.close()
    out_put_html = codecs.open('test.html',mode='w',encoding="utf-8")
    
    html = markdown.markdown(text,extensions=['markdown.extensions.fenced_code',                              
                    'markdown.extensions.codehilite'])
    out_put_html.write(html)
    out_put_html.close()
    return html
