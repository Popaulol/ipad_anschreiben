#!/bin/sh
qpdf --empty --pages ./book/pdf/output.pdf 1-8 ./AlternativenTabelle.pdf 1 ./book/pdf/output.pdf 9-z -- ./Anschreiben.pdf
