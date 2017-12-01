#!/bin/bash

default:

dist:
	tar -czvf lab3b-204650577.tar.gz README Makefile lab3b.py
clean:
	rm -f *.tar.gz lab3b
