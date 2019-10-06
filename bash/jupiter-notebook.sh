#!/bin/bash
#docker run -d --rm -p 8888:8888 -p 4040:4040  -v ~:/home/cradulescu/git/Complete-Python-3-Bootcamp jupyter/all-spark-notebook
docker run -it -d -p 8888:8888 -p 4040:4040 -v /home/cradulescu/git/Complete-Python-3-Bootcamp:/home/jovyan/workspace jupyter/all-spark-notebook