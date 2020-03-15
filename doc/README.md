Introduction:

This toolbox contain programs that handle FASTA and FASTQ files and perform basic tasks in order to for example get an overview of their sequences before continue with more complex analyses. 



Example on how to run the programs:

* Export FASTQ-file to FASTA format.
./fastq_to_fasta.py fastq_file output_fasta

* Output multiline FASTA-file to single line.
./multiline_to_singleline.py input_fasta output_fasta

* Calculate maximum, minimum and average sequence lengths.
./calculate_lengths.py single_line_fasta_file start_max start_min

* Quick quality check of FASTQ-file. Output a file with id + average quality (between 0-94).
./quick.quality.py fastq_file quality_scores.txt

* Produce reverse complement file of input FASTA-file.
./reverse_complement.py fasta_file reverse_complement_file

* Calculate overall GC-content and codon base position GC-contents (GC, GC1, GC2, GC3).
./get_gc_counts.py fasta_file

* Concatenate sequence lines if they belong to the same id.
./concatenate_seqs_w_same_id_lines.py input_fasta output_concat_fasta

* Translate all six reading frames from a single line fasta file.
./translate_frames_from_file singleline_fasta



Download toolbox:



Dependencies:
Python3 must be downloaded to run the programs included in the toolbox.


Contact:
Alma Hurtig (alma.hurtig@hotmail.com)
