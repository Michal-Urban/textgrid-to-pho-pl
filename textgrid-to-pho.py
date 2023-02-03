#       .TextGrid to .pho converter v1
#       Tested with Praat v6.3.03 and MBROLA v3.3
#       
#
#       Michał Urban, January 2022
#
#


import codecs
import parselmouth

wavfile = str(input("Enter .wav filename: "))
textgridfile = str(input("Enter .TextGrid filename: "))
sound = parselmouth.Sound(wavfile)

with codecs.open(textgridfile, "r", encoding="utf-8") as file:
    content = file.read()

#   Getting durations of each phone:
lines = content.split("\n")
xmin_lines = [line for line in lines if "xmin" in line]
xmin_values = [float(line.split("=")[1]) for line in xmin_lines]
xmax_lines = [line for line in lines if "xmax" in line]
xmax_values = [float(line.split("=")[1]) for line in xmax_lines]
durations = []
for i in range(len(xmax_values)):
    durations.append(xmax_values[i] - xmin_values[i])
durations = durations[2:]

#   Making the "text_values" array (corresponding to the "durations" array) 
text_lines = [line for line in lines if "text" in line]
text_values = [str(line.split("=")[1]) for line in text_lines]
for i in range(len(text_values)):
    text_values[i] = text_values[i].replace('"', '')
    text_values[i] = text_values[i].replace(' ', '')
    text_values[i] = text_values[i].replace('\r', '')

#   For quick debugging purposes:
#   print(text_values)
#   print(durations)

#   Getting the first .pho file, filled with every possible pitch
output = codecs.open("output.pho", "w", encoding="utf-8")
for i in range(len(text_values)):
    output.write(text_values[i] + "	" + str(round(durations[i]*1000)))
    output.write("	")
    for j in range(100):
        try:
            output.write(str(j) + "	" + str(round(sound.to_pitch().get_value_at_time(xmin_values[i]+j*(durations[i]/100), unit="HERTZ")))+"	")      # Had to be rounded, MBROLA doesn't take floats :(
        except ValueError:
            continue
    output.write(4*"\n")

#   Converting the output.pho file to SAMPA
from IPA_to_PL_SAMPA import IPA_to_PL_SAMPA, convert
input = "output.pho"
output = "output-converted.pho"
convert(input, output)

