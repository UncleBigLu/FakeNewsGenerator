import subprocess
import os
head = '\documentclass{ctexart}\n\\begin{document}\n\\begin{tabular}{|l|c|} \n\\hline\n'
tail = '\\hline\n\\end{tabular}\n\n\\end{document}\n'
def convertPDF(argDict, context):
    #subprocess.call('mkdir tmp', shell=True)
    subprocess.call('touch tmp/target.tex', shell=True)
   # print(context)
    texText = head + '稿件标题&'+argDict['topic']+'\\\\\n'+'\\hline\n'+'正文字数&'+ str(len(context))+'\\\\\n'+'\\hline\n'\
            + '新闻发生时间&'+argDict['time']+'\\\\\n'+'\\hline\n'+'正文&'+context+'\\\\\n' + tail
    with open('tmp/target.tex', 'w') as f:
        f.write(texText)
    subprocess.call('xelatex tmp/target.tex', shell=True)



