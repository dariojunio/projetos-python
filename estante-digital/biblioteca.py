class Biblioteca():
  def __init__(self):
    self.catalogo = []

  def adicionar_livro(self, livro_novo):
      self.catalogo.append(livro_novo)
      print(f'O livro {livro_novo.titulo} foi guardado com sucesso!!')

  def listar_livros(self):
    for livros in self.catalogo:
      livros.exibir_infos()

  def emprestar_livro(self, titulo_buscado):
   for emp_livro in self.catalogo:
     if emp_livro.titulo == titulo_buscado:
      if emp_livro.disponivel:
          emp_livro.disponivel = False
          print(f"O livro '{titulo_buscado}' foi emprestado com sucesso!")
      else:
          print(f"Desculpe, '{titulo_buscado}' já está emprestado.")
      return
   print(f"O livro '{titulo_buscado}' não existe no catálogo.")
