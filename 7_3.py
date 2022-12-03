import os
import fileinput
import pathlib
directory ='C:/Users/zahha/PycharmProjects/Python_projects'
files = os.listdir(directory)
text_files = []
for a in files:
    if '.txt' in a:
        text_files.append(a)
#print(text_files)
len_text_files = []
for file in text_files:
    with open(file, encoding='utf-8') as f:
        s = f.readlines()
        len_text_files.append(len(s))
#        print(type(s), len(s), s)
        f.close()
#print(len_text_files)
zip(len_text_files, text_files)
for len, file in zip(len_text_files, text_files):
    print(len,file)
len_text_files, text_files = zip(*sorted(zip(len_text_files, text_files)))
#print(len_text_files)
#print(text_files)

pth = 'C:/Users/zahha/PycharmProjects/Python_projects'
pattern = "*.txt"
files_path = pathlib.Path(pth)
list_files = text_files
#list_files = files_path.glob(pattern)
new_file = "output.all"
if list_files:
    with fileinput.FileInput(files=list_files, encoding='utf-8') as fr, open(new_file, 'w', encoding='utf-8') as fw:
        count = 0
        for line in fr:
            count += 1
            if fr.isfirstline():
                file_name = fr.filename()
                fw.write(f'\n{file_name}\n{count}\n')
            fw.write(line)





