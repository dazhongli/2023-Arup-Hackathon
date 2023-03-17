import os
import subprocess


def print_report(notebook_name="Report_Generation.ipynb", filename='report'):
    command = ["jupyter", "nbconvert", "--no-input", notebook_name,
               "--to", "html", '--output', filename+'.html']
    result = subprocess.run(command, capture_output=True)
    os.startfile(filename+'.html')
