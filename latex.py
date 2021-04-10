import subprocess
import os

head = '\documentclass{ctexart}\n\n\\usepackage{tabularx}\n\n\\begin{document}\n\\begin{tabularx}{\\textwidth}{|l|X|} \n\\hline\n'
tail = '\\hline\n\\end{tabularx}\n\n\\end{document}\n'


def convertPDF(argDict, context):
    # subprocess.call('mkdir tmp', shell=True)
    textNum = 0
    for p in context:
        textNum += len(p)
    subprocess.call('touch tmp/target.tex', shell=True)
    # print(context)
    texText = head + '\\textbf{稿件标题}&\\multicolumn{1}{|c|}{\\textbf{' + argDict['topic'] + '}}\\\\\n' \
              + '\\hline\n' + '\\textbf{正文字数}&\\multicolumn{1}{|c|}{' + str(textNum) + '}\\\\\n' + '\\hline\n' \
              + '\\textbf{新闻发生时间}&\\multicolumn{1}{|c|}{' + argDict[
                  'time'] + '}\\\\\n' + '\\hline\n' + '正文&' #+ context + '\\\\\n' + tail
    for p in context:
        texText += p
        texText += '\\newline\n'
    texText += '\\\\\n' + tail
    with open('tmp/target.tex', 'w') as f:
        f.write(texText)
    subprocess.call('xelatex tmp/target.tex', shell=True)
