#!/usr/bin/env python
import os
import sys
for line in sys.stdin:
	filename = os.environ["map_input_file"]
	line = line.strip()
	line = line.replace("*", "")
	line = line.replace(".", "")
        line = line.replace("?", "")
	line = line.replace("'", "")
        line = line.replace(",", "")
        line = line.replace(":", "")
        line = line.replace(";", "")
        line = line.replace("(", "")
        line = line.replace("&", "")
        line = line.replace(")", "")
        line = line.replace("]", "")
        line = line.replace("[", "")
        line = line.replace("\t", " ")
        line = line.replace("-", " d")
        line = line.replace("!", " ")
        word_list = (str(line).strip().split(" "))
        for word in word_list:
		word = word.strip().lower()
		if word and word not in word_list:
			sys.stdout.write(("{0}@{1},{2}\n".format(word, filename, 1)))

