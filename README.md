# textgrid-to-pho-pl
A basic automatic close copy speech synthesis program that converts a .TextGrid file to .pho file, generating every possible pitch for each phone.

I started this project out of pure curiosity. I wanted to see how well (how close to human speech) can Mbrola's speech synthesis sound.

In theory the more times we measure the F0 frequency of each phone the more accurate should Mbrola's output sound. 
The program takes the .TextGrid file and gets every possible pitch value for every voice, parses the output and then converts it into a mbrola-friendly .pho file.
Please note that in order to achieve the best results one should use a well-annotated .TextGrid file.


Usage:
Run main.py and follow the instructions. Remember that the input script is case sensitive (e.g. type example.TextGrid instead of example.textgrid)
