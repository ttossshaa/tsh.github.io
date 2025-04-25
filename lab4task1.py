from Bio import SeqIO

def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C') #Подсчитывет количество гуанинов (G) и цитозинов (C) в последовательности 
    return gc_count / len(sequence)

def sort_records_by_gc(gb_file):
    records = [] #пустой список
    for record in SeqIO.parse(gb_file, "genbank"):
        gc_content = calculate_gc_content(str(record.seq).upper()) #upper преобразует строку в верхний регистр
        records.append((record, gc_content))

    records.sort(key=lambda x: x[1])#указывает, что сортировка должна выполняться на основе второго элемента каждого кортежа

    for record, gc_content in records:
        print(f"{record.id}: {record.description}, GC = {gc_content}")

file_path = "C:\\python\\sequence.gb"
sort_records_by_gc(file_path)   
