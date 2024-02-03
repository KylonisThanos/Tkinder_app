import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import os

#function for fasta file button
def count_bases_and_sequences(fasta_file):
    bases_count = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    sequence_count = 0
    sum = 0
    #sum = bases_count['A'] + bases_count['T'] + bases_count['G'] + bases_count['C']

    with open(fasta_file, 'r') as file:
        sequences = file.readlines()

    current_sequence = ''
    for line in sequences:
        line = line.strip()
        if line.startswith('>'):
            sequence_count += 1
            continue
        current_sequence += line
    
    for base in current_sequence:
        if base in bases_count:
            sum += 1
            bases_count[base] += 1

    return sequence_count, bases_count , sum 
#na to dw ligo afto edw
#function for fastq file button
def count_bases_and_sequences(fastq_file):
    bases_count = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    sequence_count_fastq = 0

    with open(fastq_file, 'r') as file:
        sequences = file.readlines()

    current_sequence = ''
    for line in sequences:
        line = line.strip()
        if line.startswith('@'):
            sequence_count_fastq += 1
            continue
        current_sequence += line
    
    for base in current_sequence:
        if base in bases_count:
            bases_count[base] += 1

    return sequence_count_fastq, bases_count

def process_fasta_file():
    filename = filedialog.askopenfilename(initialdir="/home/", title="Select a .fasta file", filetypes=(("FASTA files", "*.fasta"), ("All files", "*.*")))
    if filename:
        sequence_count, base_counts , sum = count_bases_and_sequences(filename)
        message = f"Number of Sequences: {sequence_count}\nA: {base_counts['A']}, T: {base_counts['T']}, G: {base_counts['G']}, C: {base_counts['C']} , sum : {sum}"
        messagebox.showinfo("File Information", message)


def process_fastq_file():
    filename = filedialog.askopenfilename(initialdir="/home/", title="Select a .fastq file", filetypes=(("FASTQ files", "*.fastq"), ("All files", "*.*")))
    if filename:
        sequence_count, base_counts = count_bases_and_sequences(filename)
        message = f"Number of Sequences: {sequence_count}\nA: {base_counts['A']}, T: {base_counts['T']}, G: {base_counts['G']}, C: {base_counts['C']}"
        messagebox.showinfo("File Information", message)


root = tk.Tk()
root.title("DNA Base Counter Application")
root.geometry("1000x800")

script_dir = os.path.dirname(os.path.abspath(__file__))

#photo icon , panw aristera.
icon_path = os.path.join(script_dir, "scientist.png")
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(True, icon)

#photo sto background
background_path = os.path.join(script_dir, "scientist.png")
background_image = Image.open(background_path)
background_photo = ImageTk.PhotoImage(background_image)


background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  

#list with all the file types showing as buttons on the application.
file_types = ('FASTQ', 'FASTA', 'GB', 'GBK', 'SAM', 'BAM', 'BED', 'GFF', 'GTF')
var = tk.StringVar()
var.set(file_types[0])

def cb():
    print(var.get())

for index, x in enumerate(file_types):
    if x == 'FASTA':
        radio_button = tk.Radiobutton(root, text=x, variable=var, value=x, relief=tk.RAISED, bg="lightpink", width=15, height=2, cursor="hand2", command=process_fasta_file)
    elif x == 'FASTQ':        
        radio_button = tk.Radiobutton(root, text=x, variable=var, value=x, relief=tk.RAISED, bg="lightpink", width=15, height=2, cursor="hand2", command=process_fastq_file)
    else:
        radio_button = tk.Radiobutton(root, text=x, variable=var, value=x, relief=tk.RAISED, bg="lightpink", width=15, height=2, cursor="hand2", command=cb)
    radio_button.place(x=50, y=50 + index * 45)
 

button_quit= Button(root , text= "Exit Program" ,relief=tk.SUNKEN ,borderwidth=2, bg="lightblue" ,width=15,height=2, padx=10, pady=5, cursor="hand2" ,highlightcolor="yellow",command= root.quit )
button_quit.place(x=250, y=700 )

root.mainloop()

