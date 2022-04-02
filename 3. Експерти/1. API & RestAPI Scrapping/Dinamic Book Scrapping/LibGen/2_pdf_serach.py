# Диляна Хаджиматева
# докт. към КИТ, ФМИ, СУ "Св.Климент Охридски"
# н.р-л: доц. Валерия Симеонова
# дисц. Откриване на знания, проф. Иван Койчев
# 2021

# Описание на проекта:
# част 2: Откриване на знания в свалените книги: претърсване САМО на съдържанието,
# и ако е намерена информация по зададените критерии във VOCABULARY, то се прави токенизатор.
# Токенизаторът се експортва в pandas dataframe oбект, и по идея последните две колони трябва да съдържат
# от коя страница започва въпросната точка и на коя свършва. След това, като се използва токенизатора се
# извличат въпросните страници от .pdf-a, и по този начин се филтрира необходимата информация от pdf файла,
# която ни интересува.
# Логика на скрипта:

# ------------------------------Имплементация------------------------------

# Необходими модули:
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import io
import pandas as pd

# Първоначални настройки:
pages_to_be_processed=20
folder_path='./MyBooks/Theory/'
filelist=sorted(os.listdir(folder_path))
vocabulary=['cluster','clusterization','unsupervised']
fname_prefix="cleaned_"
fname_sufix='.pdf'
problem_files=[]

def print_pdf_lines_1(Input_File,page,line=-1):
    # Тестов Вариант 1 на прочитане .pdf файла ред по ред
    pdfFileObj = open(Input_File, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(page)
    pages_text = pageObj.extractText()
    if line==-1:
        print(io.StringIO(pages_text).readline()) # отпечатва първия ред
    else:
        print(list(io.StringIO(pages_text))[line])
    return 'Done'

def print_pdf_lines_2(Input_File):
    # Тестов Вариант 2 на прочитане .pdf файла ред по ред
    def get_pdf_content_lines(In_File):
        pdf_reader = PdfFileReader(open(In_File,'rb'))
        for page in pdf_reader.pages:
            for line in page.extractText().splitlines():
                yield line

    for line in get_pdf_content_lines(Input_File):
        print(line)

def print_pdf_lines_3(Input_File):
    # Тестов Вариант 3 на прочитане .pdf файла ред по ред
    # Връща многоредов текст, по-добро от останалите варианти, но пак не върши работа
    pdf_reader = PdfFileReader(open(Input_File,'rb'))
    content = "\n".join(page.extractText().strip() for page in pdf_reader.pages)
    content = ' '.join(content.split())
    return content

def get_tokens(current_line:str):
    # Токенизиране само на онези линии от текущата страница, които завършват на число
    global vocabulary
    tokens = dict()
    try:
        int(current_line[-1])
        check=True
    except:
        check=False
    if check:
        print(current_line)
        for v in vocabulary:
            print(current_line)
            if current_line.count(v)==0:
                tokens[v]=0
            else: tokens[v]+=1
        tokens['from_page'] = int(current_line.split(' ')[-1])
    else:
        for v in vocabulary:
            tokens[v]=0
        tokens['from_page'] = 0

    return tokens

def get_first_n_pages(Input_File):
    # Функцията създава съкратена версия на оригиналния .pdf от първите 20 стр.
    # и връща името на новия файл
    global pages_to_be_processed
    global folder_path
    in_file = PdfFileReader(open(Input_File, 'rb'), strict=False)
    pdfWriter = PdfFileWriter()
    for page_number in range(pages_to_be_processed):
        input_page = in_file.getPage(page_number)
        pdfWriter.addPage(input_page)
    Output_File=folder_path+'20_'+Input_File[Input_File.find('ISBN'):]
    with open(Output_File, "wb") as output:
        pdfWriter.write(output)
    output.close()
    return Output_File

def get_between_pages(Input_File,from_page,to_page):
    # Функцията създава съкратена версия на оригиналния .pdf от # стр. до # стр.
    # и връща името на новия файл
    global pages_to_be_processed
    global folder_path
    in_file = PdfFileReader(open(Input_File, 'rb'), strict=False)
    pdfWriter = PdfFileWriter()
    for page_number in range(from_page,to_page+1):
        input_page = in_file.getPage(page_number)
        pdfWriter.addPage(input_page)
    Output_File=folder_path+'cleaned_'+Input_File[Input_File.find('_')+1:]
    with open(Output_File, "wb") as output:
        pdfWriter.write(output)
    output.close()
    return Output_File

def get_pages(Input_File):
    # Оригиналната обработка
    # Работи с предположението, че връща редовете, така както ги виждаме
    # Реално, номерата на страниците излизат в началото на реда
    global pages_to_be_processed
    global vocabulary

    # Зареждане на файла с първите 20 стр.
    pdf_to_parse=get_first_n_pages(Input_File)
    readf=open(pdf_to_parse,'rb')
    # Четене на всеки ред от pdf-a
    nonempty_lines = [line.strip() for line in readf if line != "\n"]
    print(nonempty_lines[:5])
    # Токенизация
    tokenizer = []
    for line in nonempty_lines:
        ln_tok=get_tokens(line)
        tokenizer.append(ln_tok)
    # Извличане на необходимите страници за .pdf файла
    tokens_data_set_for_file=pd.DataFrame(tokenizer)
    # добавяне на още една колона, която да посочва страницата, до която да се извлече текста
    new_col=list(tokens_data_set_for_file.iloc[1:,-1])
    new_col=[int(n) for n in new_col]
    in_file=PdfFileReader(open(Input_File,'rb'))
    new_col.append(in_file.getNumPages())
    tokens_data_set_for_file['to_page']=new_col
    print('tokens_data_set_for_file: \n')
    print(tokens_data_set_for_file)

    conditions=[]
    for v in range(len(vocabulary)):
        conditions.append(tokens_data_set_for_file.iloc[:, v] == 0)
    full_condition=True
    for i in conditions:
        full_condition=full_condition & i
    fc=~full_condition
    cleaned_data_set=tokens_data_set_for_file[fc]
    print('cleaned_data_set: \n')
    print(cleaned_data_set)
    from_page=list(cleaned_data_set.iloc[:,-2])
    from_page = [int(n) for n in from_page]
    to_page=list(cleaned_data_set.iloc[:,-1])

    # Извличане от страница до страница
    for i in range(len(from_page)):
        printed_text='pages: %d - %d...' %(from_page[i],to_page[i]+1)
        try:
            get_between_pages(from_page[i],to_page[i])
            printed_text+="processed succesifully"
        except:
            printed_text+='aborted'
            pass
        print(printed_text)
    print('Done')

    return "Done"

def main_processing():
    global folder_path
    global filelist
    for file in filelist:
        input_fname = folder_path + file
        check=True
        if file.endswith(".pdf"):
            try:
                PdfFileReader(input_fname,strict=False)
                check=True
            except:
                check=False
            if check:
                output_fname = folder_path+fname_prefix+file
                get_pages(input_fname,output_fname)
            else:
                problem_files.append(input_fname)

    print("Problem files:\n")

    for i in problem_files:
        print(i)

# # Стартиране на програмата:
# main_processing()

# ТЕСТВАНЕ на отпечатване на редовете

full_path=folder_path+filelist[1]
print(full_path)
# print_pdf_lines_1(full_path,10)

# print_pdf_lines_1(full_path,page=10,line=15)
# # 132 трябва да се разглежда като: предходната точка от съдържанието да започва на 13-та страница,
# # а ReverseClustering трябва да е точка 2 от съдържанието

# print_pdf_lines_2(full_path)
# # Връща подобен резултат на print_pdf_lines_1

# print_pdf_lines_3(full_path)
