import os
import subprocess
import requests

def welcome(user):
    print(f"Bem vindo à ferramenta de análise de dados da JHS, {user}!")
    print("Este script foi desenvolvido pelo time de desenvolvedores da JHS, sendo de uso restrito de seus colaboradores.")

# ---------------------------------------------- #

def get_reference(entry):
    while True:
        parameters = {
            "db": "nuccore",
            "id": f"{entry}",
            "rettype": "fasta",
            "retmode": "text"
        }
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        gene = requests.get(url, params=parameters)

        if gene.status_code == 200:
            try:
                with open(F"reference_{entry}.fasta", "w") as ref:
                    ref.write(gene.text)
                return f"reference_{entry}.fasta"
            except PermissionError:
                print("O usuário não tem permissão para criar arquivos. Contate o time de TI para mais informações")
        if gene.status_code == 404:
            raise FileNotFoundError("O gene não foi encontrado. Insira novamente os dados")


#------------------------------------------------#

def get_analysis(gene, gene_name, gene_reference, user):
    sub = ["python", "run_analysis.py", gene, gene_name, gene_reference, user]
    subprocess.run(sub, cwd=os.path.dirname(__file__))

#-------------------------------------------------#

if __name__ == '__main__':
    user_ = input("Insira o nome de usuário: ")
    welcome(user_)
    while True:
        selection = int(input("Insira a opção desejada: \n 1 - Análise de dados de sequenciamento de gene in situ \n : "))
        if selection == 1:
            try:
                gene_name_ = input("Insira o nome do gene sequenciado: ")
                gene_sequence_ = input("Insira o gene sequenciado: ")
                entry_ = input("Insira o código genbank do gene de referência: ")
                gene_reference_ = get_reference(entry_)
                get_analysis(gene_sequence_, gene_name_, gene_reference_, user_)
                break
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}. Tente novamente")
        else:
            raise ValueError("Opção inválida, tente novamente.")
