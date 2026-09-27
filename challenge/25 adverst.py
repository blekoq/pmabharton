import re# import library re
txt = "The rain in Spain"# mencari kata "Spain" dalam string txt
x  = re.search(r"\bSpain\b", txt)# mencetak hasil pencarian
print (x.span())# mencetak posisi awal dan akhir dari kata "Spain" dalam string txt