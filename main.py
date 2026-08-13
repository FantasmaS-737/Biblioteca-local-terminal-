import json
import os

class Biblioteca():
	def __init__(self, nome_arquivo="Biblioteca.json"):
		self.nome_arquivo = nome_arquivo
		self.livros = self._carregar()
			
	def _carregar(self):
		try:
			with open(self.nome_arquivo, "r", encoding="utf-8") as f:
				return json.load(f)
		except(FileNotFoundError, json.JSONDecodeError):
				return []
				
	def _salvar(self):
				with open(self.nome_arquivo, "w", encoding="utf-8") as f:
					json.dump(self.livros, f, indent=4, ensure_ascii=False)
					
	def adicionar(self):
		titulo = input("titulo: ")
		descricao = input("descricao: ")
		autor = input("autor: ")
		
		if titulo:
			add_livro={
				"titulo": titulo,
				"descricao": descricao,
				"lido": False,
				"autor":autor,
				"favorito": False
			}
			self.livros.append(add_livro)
			self._salvar()
			print("livro adicionado com com sucesso")
		else:
			print("o titulo e obrigatorio")
	
	def listar(self):
		if not self.livros:
			print("voce nao tem nenhum livro")
			
		else:
			
			for i, livro in enumerate(self.livros, 1):
				stats =  "[x]" if livro["lido"] else "[ ]"
				print(f"{i}-{stats} {livro['titulo']}")

	def remover(self):
		if self.livros:
			self.listar()
			indice = int(input("digitre o indice do livro que voce quer excluir: "))
			if 1 <= indice <= len(self.livros):
				removida= self.livros.pop(indice - 1)
				self._salvar()
				print("removida com sucesso")
			else:
				print("coloque um digito valido")
		else:
			print("voce nao tem nenhum livro para poder remover")
			
	def favoritar(self):
		if self.livros:
			self.listar()
			indice = int(input("voce quer favoritar qual livro: "))
			if 1 <= indice <= len(self.livros):
				self.livros[indice - 1]["favorito"] = True
				self._salvar()
				print("livro favoritado com sucesso")
		else:
			print("voce nao tem nenhum livro")		
		
	def favoritos(self):
		if not self.livros:
			print("voce nao tem nenhum livro")
		favoritos = [livro for livro in self.livros if livro["favorito"]]
		
		if not favoritos:
			print("voce nao tem nenhum livro favorito")
			
		else:
			for i, livro in enumerate(favoritos, 1):
				stats = "[x]" if livro["lido"] else "[ ]"
				print(f"{i}-{stats} {livro['titulo']}")
				
	def ler(self):
		if not self.livros:
			print("voce nao tem nenhum livr salvo")
		else:
			self.listar()
			indice = int(input("digite o indice do livro que voce leu: "))
			if 1 <= indice <= len(self.livros):
				self.livros[indice - 1]["lido"] = True
				self._salvar()
				print("marcado como lido com sucesso")
			else:
				print("digite um numero valido")
				return
	
	def especifico(self):
		if not self.livros:
			print("voce não tem nenhum livro")
			
		else:
			self.listar()
			indice = int(input("voce quer ver qual filme em específico(indice): "))
			if 1 <= indice <= len(self.livros):
				livro = self.livros[indice - 1]
				print("================")
				print("")
				print(livro["titulo"])
				print("")
				print(livro["autor"])
				print("")
				print("----------------------------------")
				print("")
				print(livro["descricao"])
				print("")
				print("================")
			
			else:
				print("coloque um numero valido")
				

def main():
	b = Biblioteca()
	
	while True:
		os.system("cls" if os.name == "nt" else "clear")
		print("==========BIBLIOTECA=========")
		print("")
		print("1-listar")
		print("2-listar(favoritos)")
		print("3-adicionar")
		print("4-remover")
		print("5-favoritar")
		print("6-marca como lido")
		print("7-mostrar detalhes")
		print("8-sair")
		print("")
		
		opcao = input("qual voce vai escolher: ")
		
		if opcao == "1":
			b.listar()
			input("")
		
		elif opcao == "2":
			b.favoritos()
			input("")
		
		elif opcao == "3":
			b.adicionar()
			input("")
		
		elif opcao == "4":
			b.remover()
			input("")
		
		elif opcao == "5":
			b.favoritar()
			input("")
			
		elif opcao == "6":
			b.ler()
			input("")

		elif opcao == "7":
			b.especifico()
			input("")
		
		elif opcao == "8":
			break
			
		else:
			print("digite um numero valido")
			continue 

print("ate mais")

if __name__ == "__main__":
	main()			