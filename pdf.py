import PyPDF2
import sys

try:
    inputs = sys.argv[2:]
    function_choice = sys.argv[1].lower()
    template = PyPDF2.PdfFileReader(open(sys.argv[2], 'rb'))
    watermark = PyPDF2.PdfFileReader(open(sys.argv[3], 'rb'))

except IndexError:
    print('This program will allow you to merge or watermark pdf files. Be sure the files and this program are in the '
          'same folder.')
    function_choice = input('Do you want to merge or watermark?: ')
    # need to extend this to accept any number of pdfs
    if function_choice.lower() == 'merge':
        first_file = input('Please enter the name of your first pdf. Be sure to include ".pdf" at the end: ')
        second_file = input('Please enter the name of your second pdf. Be sure to include ".pdf" at the end: ')
        inputs = [first_file, second_file]
        print('Thanks.')
    elif function_choice.lower() == 'watermark':
        template = PyPDF2.PdfFileReader(open(input('Please enter the name of your pdf to put the watermark on. '
                                                   'Include ".pdf" at the end: '), 'rb'))
        watermark = PyPDF2.PdfFileReader(open(input('Please enter the name of your pdf watermark. Include ".pdf" at '
                                                    'the end: '), 'rb'))
        print('Thanks.')

if function_choice == 'merge':
    def pdf_merger(pdf_list):
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list:
            merger.append(pdf)

        merger.write('merged.pdf')


    pdf_merger(inputs)
    print('Files have been merged.')
elif function_choice == 'watermark':
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermarked.pdf', 'wb') as file:
            output.write(file)
    print('File has been watermarked.')


