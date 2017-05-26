Resultados_hw5.pdf: ej1.jpg hist1.jpg RvsLihelihood.jpg CvsLihelihood.jpg model.jpg Resultados_hw5.tex
	pdflatex Resultados_hw5.tex

model.jpg: CircuitoRC.txt circuitoRC.py
	python	circuitoRC.py

CvsLihelihood.jpg: CircuitoRC.txt circuitoRC.py
	python	circuitoRC.py

RvsLihelihood.jpg: CircuitoRC.txt circuitoRC.py
	python	circuitoRC.py

hist1.jpg: datos.txt plots_canal_ionico.py 
	python plots_canal_ionico.py

ej1.jpg: datos.txt plots_canal_ionico.py 
	python plots_canal_ionico.py

datos.txt: Canal_ionico.txt Canal_ionico1.txt canal_ionico.c
	gcc -lm canal_ionico.c
	./a.out > datos.txt
