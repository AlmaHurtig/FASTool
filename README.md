Introduction:

This toolbox contain programs that handle FASTA and FASTQ files and perform basic tasks in order to for example get an overview of their sequences before continuing with more complex analyses. 


Example on how to run the programs:

* Export FASTQ-file to FASTA format:
./fastq_to_fasta.py fastq_file output_fasta

* Output multiline FASTA-file to single line:
./multiline_to_singleline.py input_fasta output_fasta

* Calculate maximum, minimum and average sequence lengths:
./calculate_lengths.py single_line_fasta_file start_max start_min

* Calculate overall GC-content and codon base position GC-contents (GC, GC1, GC2, GC3):
./get_gc_counts.py fasta_file

* Quick quality check of FASTQ-file. Output a file with id + average quality (between 0-94):
./quick.quality.py fastq_file quality_scores.txt

* Produce reverse complement file of input FASTA-file:
./reverse_complement.py fasta_file reverse_complement_file

* Concatenate sequence lines if they belong to the same id:
./concatenate_seqs_w_same_id.py input_fasta output_concat_fasta

* Translate all six reading frames from a single line fasta file:
./translate_frames_from_file.py singleline_fasta output_file

* Translate a single line FASTA/sequence file:
./translate_sequence.py singleline_fasta output_file


Download toolbox:
Clone the repository: https://github.com/AlmaHurtig/toolbox_fasta-fastq.git.

Dependencies:
Python3 (version 3.7.4) must be downloaded to run the programs included in the toolbox.

Contact:
Alma Hurtig (alma.hurtig@hotmail.com)
