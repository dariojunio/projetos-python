class Livro():
  def __init__(self, titulo, autor, paginas):
    self.titulo = titulo
    self.autor = autor
    self.paginas = paginas
    self.disponivel = True

  def exibir_infos(self):
    status = 'Diposnivel!' if self.disponivel else 'Emprestado'
    print(f'O livro {self.titulo} do autor {self.autor} tem {self.paginas} paginas e está {status} !')
