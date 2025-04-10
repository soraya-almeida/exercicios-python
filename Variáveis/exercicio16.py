#Peça o nome e o curso de um aluno e exiba uma frase como: "Fulano está matriculado no curso de X".

nome = str(input("Informe seu nome: "))
curso = str(input("Informe seu curso: "))

print(nome, "está matriculado(a) no curso", curso)

#CORREÇÃO⬇️

nome = input("Nome: ")
curso = input("Curso: ")
print(f"{nome} está matriculado no curso de {curso}")
