#Extrair do pdf anexo os dados dos Quadros 30,31,32 (Tabela de categoria do Padrão TISS);
#Salvar dados dessas tabelas em csvs;
#Zipar todos os csvs num arquivo "Teste_Intuitive_Care_{seu_nome}.zip".


#Comando no terminal: pip install tabula 
#Módulo para pegar os dados do PDF
import tabula

#ZipFile serve para zipar os arquivos CSV
import zipfile


#Pega as tabelas das páginas selecionadas
tabula.read_pdf("Componente Organizacional.pdf", pages=[79])
tabula.read_pdf("Componente Organizacional.pdf", pages=[79, 80, 81, 82, 83, 84])
tabula.read_pdf("Componente Organizacional.pdf", pages=[85])

#Transforma em CSV
tabula.convert_into("Componente Organizacional.pdf", "tabela_de_tipo_de_demandante.csv", output_format="csv", pages=[79])
tabula.convert_into("Componente Organizacional.pdf", "tabela_de_categoria_do_Padrão_TISS.csv", output_format="csv", pages=[79, 80, 81, 82, 83, 84])
tabula.convert_into("Componente Organizacional.pdf", "tabela_de_tipo_de_solicitação.csv", output_format="csv", pages=[85])

#Junta os arquivos em .zip
arquivoZipado = zipfile.ZipFile("Teste_Intuitive_Care_Carlos_Cesar.zip", "w")
arquivoZipado.write("tabela_de_tipo_de_demandante.csv")
arquivoZipado.write("tabela_de_categoria_do_Padrão_TISS.csv")
arquivoZipado.write("tabela_de_tipo_de_solicitação.csv")

#Comando para rodar o código no terminal: python teste2TransformaçãoDeDados.py 

