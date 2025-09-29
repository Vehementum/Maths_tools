# Run Python to generate the .tex
python main.py

# If Python succeeded, compile LaTeX
if ($?) {
    pdflatex -output-directory=latex/output latex/src/student_worksheet.tex

    # Move PDF to root, overwrite if it already exists
    move -Force latex\output\student_worksheet.pdf .

    # Clean up auxiliary files
    Remove-Item latex\output\*.aux, latex\output\*.log, latex\output\*.out -ErrorAction SilentlyContinue
}
