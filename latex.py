import subprocess
import os

head = '''
    \documentclass{ctexart}
    
    \\usepackage{tabularx}
    \\begin{document}
    \\begin{tabularx}{\\textwidth}{|l|X|} 
    \\hline
'''
tail = '\\hline\n\\end{tabularx}\n\n\\end{document}\n'


def convertPDF(argDict, context):
    # subprocess.call('mkdir tmp', shell=True)
    textNum = 0
    for p in context:
        textNum += len(p)
    # print(context)
    texText = head + '\\textbf{稿件标题}&\\multicolumn{1}{|c|}{\\textbf{' + argDict['topic'] + '}}\\\\\n' \
              + '\\hline\n' + '\\textbf{编稿者}&\\multicolumn{1}{|c|}{' + 'proto' + '}\\\\\n'  \
              + '\\hline\n' + '\\textbf{正文字数}&\\multicolumn{1}{|c|}{' + str(textNum) + '}\\\\\n' + '\\hline\n' \
              + '\\textbf{新闻发生时间}&\\multicolumn{1}{|c|}{' + argDict[
                  'time'] + '}\\\\\n' + '\\hline\n' + '正文&' #+ context + '\\\\\n' + tail
    for p in context:
        texText += p
        texText += '\\newline\n'
    texText += '\\\\\n' + tail
    with open('target.tex', 'w') as f:
        f.write(texText)
    subprocess.call('xelatex target.tex', shell=True)
    subprocess.call('mv target.pdf /home/unclebiglu/nginx_data/fakenews/target.pdf', shell=True)
