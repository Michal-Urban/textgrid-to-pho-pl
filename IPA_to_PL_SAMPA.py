#       IPA to Polish SAMPA dictionary
#       Michał Urban, 2022

IPA_to_PL_SAMPA = {     #   This dictionary should be, but probably is not complete
    "ɨ\t" : "I\t",      #   If problems occur, check:
    "ɪ\t" : "I\t",      #   phon.ucl.ac.uk/home/sampa/pol-uni.htm
    "ɛ̃w̃" : "e~\t",      #   www.fon.hum.uva.nl/praat/manual/Phonetic_symbols__consonants.html
    "ɛj̃" : "e~\t",      #   baltoslav.eu/ipa/
    "õ\t" : "o~\t",
    "w̃\t" : "o~\t",
    "ɔ̃w̃" : "o~\t",
    "ʂ\t" : "S\t",
    "sz" : "Z\t",
    "ɕ\t" : "s'\t",
    "ʑ\t" : "z'\t",
    "tɕ" : "ts'",
    "ɖʐ" : "dz'\t",
    "ɲ\t" : "n'\t",
    "ɛŋ" : "N\t",
    "ɔ\t" : "o\t",
    "ʋ\t" : "v\t",
    "ɛ\t" : "e\t",
    "ɜ\t" : "e\t"
    }

def convert(input, output):     # converts an input file from IPA to Polish SAMPA based on the IPA_to_PL_SAMPA dictionary
    import codecs
    with codecs.open(input, "r", encoding="utf-8") as input_file:
        with codecs.open(output, "w", encoding="utf-8") as output_file:
            for line in input_file:
                new_line = line
                if new_line != "\n":
                    x = line[0:2]
                    if x in IPA_to_PL_SAMPA:
                        new_line = new_line.replace(new_line[0:2], IPA_to_PL_SAMPA[new_line[0:2]])
                output_file.write(new_line)
