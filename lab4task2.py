from Bio import SeqIO

def translate_cds(record, feature):
    if feature.type == "CDS":
        start = feature.location.start #Получает начальную позицию CDS из объекта feature.location и сохраняет ее в переменной start
        end = feature.location.end #Получает конечную позицию CDS из объекта feature.location и сохраняет ее в переменной end
        strand = feature.location.strand #информация о направлении цепи ДНК, Значение 1 означает прямую цепь, -1 - обратную
        
        if strand == 1:
            coding_seq = record.seq[start:end]
        else:
            coding_seq = record.seq[start:end].reverse_complement()
        
        try:
            protein_seq = str(coding_seq.translate(to_stop=True))#Транслирует последовательность CDS в аминокислотную последовательность,выполняет трансляцию,останавливается на стопкодоне
            return protein_seq, start, end, strand
        except Exception as e:
            print(f"Error translating CDS in {record.id}: {e}")
            return None, None, None, None
    return None, None, None, None #Возвращает None для белковой последовательности, начальной и конечной позиций и информации о направлении цепи, если feature.type не равно "CDS"

def process_genbank_file(gb_file):
    
    translations = []
    
    for record in SeqIO.parse(gb_file, "genbank"):        
        for feature in record.features:
            protein_seq, start, end, strand = translate_cds(record, feature)
            if protein_seq:
                translations.append((record, feature, protein_seq, start, end, strand))
        
    print("CDS Translations:")
    for record, feature, protein_seq, start, end, strand in translations:
        print(f"Record: {record.id}: {record.description}")
        print(f"Coding sequence location = [{start+1}:{end}]({'Forward' if strand == 1 else 'Reverse'})")
        print(f"Translation = \n{protein_seq}\n")

if __name__ == "__main__":
    file_path = "C:\\python\\sequence.gb"
    process_genbank_file(file_path)
