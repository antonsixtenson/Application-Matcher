import read_cv

class Match():

    def __init__(self, cv, softKeys, hardKeys):
        self.softKeys = softKeys
        self.hardKeys = hardKeys
        self.cv = cv

    def match_keywords(self):
        pdf = read_cv.ReadPDFCV()
        cv = pdf.open_cv(self.cv)

        kw = None
        matches = 0

        for i, word in enumerate(self.softKeys):
            kw = i + 1
            if(word in cv.lower()):
                matches += 1

        perc = matches/kw * 100

        kw_2 = None
        matches_2 = 0

        for i, word in enumerate(self.hardKeys):
            kw_2 = i + 1
            if(word in cv.lower()):
                matches_2 += 1

        perc_2 = matches_2/kw_2 * 100

        return (perc_2, perc)