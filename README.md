📚 Sistema de Gerenciamento de Biblioteca

Um simples sistema de gerenciamento de livros em Python, com persistência de dados em JSON. Permite adicionar, listar, remover, favoritar, marcar como lido e ver detalhes de livros.

🚀 Funcionalidades

· Adicionar livro – Insira título, descrição e autor.
· Listar todos os livros – Exibe todos os livros com indicação de lido/não lido.
· Listar favoritos – Mostra apenas os livros marcados como favoritos.
· Remover livro – Remove um livro pelo índice da lista.
· Favoritar livro – Marca um livro como favorito.
· Marcar como lido – Altera o status de leitura de um livro.
· Ver detalhes – Exibe título, autor e descrição de um livro específico.

🛠️ Tecnologias Utilizadas

· Python 3 – Linguagem de programação.
· JSON – Formato de arquivo para persistência de dados.

📂 Estrutura do Projeto

```
.
├── Biblioteca.py          # Código principal
├── Biblioteca.json        # Arquivo de dados (criado automaticamente)
└── README.md              # Este arquivo
```

📦 Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone ou baixe o repositório.
3. Navegue até o diretório do projeto.
4. Execute o programa:

```bash
python Biblioteca.py
```

🖥️ Interface

O programa é executado no terminal, com um menu interativo:

```
==========BIBLIOTECA=========

1-listar
2-listar(favoritos)
3-adicionar
4-remover
5-favoritar
6-marca como lido
7-mostrar detalhes
8-sair
```

Basta digitar o número da opção desejada e seguir as instruções.

📄 Persistência

Os dados são salvos automaticamente no arquivo Biblioteca.json no mesmo diretório do script. Caso o arquivo não exista, ele será criado na primeira execução.

🔧 Personalização

· O nome do arquivo JSON pode ser alterado no construtor da classe Biblioteca.
· Os campos de cada livro são: titulo, descricao, autor, lido (booleano) e favorito (booleano).

🧪 Exemplo de Uso

```python
# Adicionar um livro
Título: O Senhor dos Anéis
Descrição: Uma aventura épica na Terra-média.
Autor: J.R.R. Tolkien

# Listar livros
1-[ ] O Senhor dos Anéis

# Favoritar
Digite o índice do livro para favoritar: 1
Livro favoritado com sucesso!

# Listar favoritos
1-[ ] O Senhor dos Anéis
```

📝 Licença

Este projeto é de uso livre para fins educacionais e de estudo.

---

sinta-se à vontade para contribuir, sugerir melhorias no codigo ou me dando dicas do que devo melhorar pois sou inciante no mundo da programacao!