import sys

#---------------------------OBRIGATORIO-----------------------------------#


def get_reference(reference):
    try:
        with open(reference, "r") as ref:
            reads = [i for i in ref.readlines() if ">" not in i]
            treated_reads = []
            for n in reads:
                treat = n.replace("\n", "")
                treated_reads.append(treat)
            return "".join(treated_reads)
    except FileNotFoundError:
        print(f"Arquivo {reference} não encontrado. Verifique o diretório de trabalho e execute a análise novamente")
    except PermissionError:
        print(f"O usuário não tem permissão para acessar o arquivo {reference}. Contate o suporte de TI para mais informações")
    except MemoryError:
        print(f"O dipositivo não tem memória RAM suficiente para a análise do arquivo {reference}. Feche alguns programas e tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

#---------------------------OBRIGATORIO-----------------------------------#

def get_gene_list(gene):
    try:
        gene_list = [a for a in gene]
        print(gene_list)
        return gene_list
    except Exception as e:
        print(f"Ocorreu um erro inesperado na obtenção da lista de nucleotídeos sequenciados: {e}. Tente novamente.")

#------------------------------OBRIGATORIO---------------------------------#

def get_reference_list(reference):
    try:
        reference_list = [b for b in reference]
        print(reference_list)
        return reference_list
    except Exception as e:
        print(f"Ocorreu um erro inesperado na obtenção da lista de nucleotídeos de referência: {e}. Tente novamente.")

#------------------------------OBRIGATORIO----------------------------------#

def get_analysis(list_gene, list_reference, name, user):
    try:
        counter = 0
        with open(f"analysis_{name}_{user}.csv", "w") as sheet:
            sheet.write("posicao,referencia,sequenciado\n")
        for sequenced, reference in zip(list_gene, list_reference):
            counter += 1
            if sequenced != reference:
                with open(f"analysis_{name}_{user}.csv", "a") as sheet:
                    sheet.write(f"{counter},{reference},{sequenced}\n")
        return "Arquivo CSV criado."
    except Exception as e:
        print(f"Ocorreu um problema na obtenção dos SNPs: {e}. Tente novamente")

#-----------------------------OPCIONAL------------------------------------#

def fill_gene_sequence(gene_list, reference_list):
    while len(gene_list) < len(reference_list):
        gene_list.append("N")
    return gene_list

#-----------------------------OPCIONAL------------------------------------#

def fill_reference_sequence(gene_list, reference_list):
    while len(reference_list) < len(gene_list):
        reference_list.append("N")
    return reference_list

#-------------------------------------------------------------------------#


if len(sys.argv) < 3:
    raise IndexError("Número de argumentos inválidos.")

gene_sequenced = sys.argv[1]
gene_name = sys.argv[2]
gene_reference = sys.argv[3]
user_ = sys.argv[4]

reference_ = get_reference(gene_reference)
gene_list_ = get_gene_list(gene_sequenced)
reference_list_ = get_reference_list(reference_)
if len(gene_list_) != len(reference_list_):
    if len(gene_list_) < len(reference_list_):
        gene_list_ = fill_gene_sequence(gene_list_, reference_list_)
    elif len(reference_list_) < len(gene_list_):
        reference_list_ = fill_reference_sequence(gene_list_, reference_list_)
print(get_analysis(gene_list_, reference_list_, gene_name, user_))


