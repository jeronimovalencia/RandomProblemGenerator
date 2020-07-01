RandomProblems.docx : RandomProblems.tex
	pandoc RandomProblems.tex -o RandomProblems.docx
	rm RandomProblems.tex

RandomProblems.tex : RandomProblemGenerator.py
	python3 RandomProblemGenerator.py > RandomProblems.tex
	

