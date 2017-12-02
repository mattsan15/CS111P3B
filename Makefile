#!/bin/bash

default:
	echo 'python lab3b.py $$1'>lab3b
	chmod 700 lab3b
dist:
	tar -czvf lab3b-004639538.tar.gz README Makefile lab3b.py
clean:
	rm -f *.tar.gz lab3b
