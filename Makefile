# CC = gcc


graph:
		dot -Tsvg graph.gv > graph.svg

clear_gv:
		rm ./*.gv

clear_svg:
		rm ./*.svg

clear:
		rm  *.gv *.svg 
