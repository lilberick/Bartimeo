# Leer libro: Detectar texto de un libro y escucharlo
1. Instalación en la Raspberry Pi
	1. tesseract-ocr
		```
		$ sudo apt install tesseract-ocr
		$ tesseract -v
		```
	2. idiomas para tesseract-ocr
		1. español
			1. idioma
				```
				$ sudo apt install tesseract-ocr-spa
				```
			2. diccionario
				```
				$ sudo apt install hunspell-es
				```
		2. japones
			1. idioma
				```
				$ sudo apt install tesseract-ocr-jpn
				```
	3. gTTS
		```
		$ sudo pip3 install gTTS
		```
	4. mplayer
		```
		$ sudo apt install mplayer
		```
2. Script para usar el gpio27
	1. Contenido del script: `bartimeo.sh`
		```bash
		#!/bin/bash
		i=0
		while true; do
			if [ $(gpio read 2) == 0 ]; then
				raspistill -o $i.jpg
				tesseract $i.jpg texto$i -l spa
				gtts-cli -l 'es' -f texto$i.txt -o $i.mp3
				mplayer $i.mp3
				i=$((i+1))
				echo listo papi
			fi
		done
		```
	2. Le damos permiso de ejecución
		```
		$ chmod +x bartimeo.sh
		```
	3. Ejecutamos
		```
		$ ./bartimeo.sh
		```
3. Como usarlo
	1. Enfocamos la cámara sobre el texto del libro   
		![](.img/1.jpg)
	2. Presionamos el pulsador   
	3. De la imagen podremos extraer el texto en un archivo .txt   
		![](.img/2.png)
	4. Se generará un archivo .mp3 y se ejecutará, por tanto podremos escucharlo   
		[Click para escuchar el audio](test/4.mp3)
