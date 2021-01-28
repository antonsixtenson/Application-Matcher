import pdftotext

class ReadPDFCV():

    def open_cv(self, file):

        with open(file, "rb") as f:
            cv_pdf = pdftotext.PDF(f)

        for page in cv_pdf:
            return page


