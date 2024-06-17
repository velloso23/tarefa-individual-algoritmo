class ObraDeArte:
    def __init__(self, titulo, autor, data_criacao):
        self.titulo = titulo
        self.autor = autor
        self.data_criacao = data_criacao
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.data_criacao})"

def ordenar_por_titulo(obras):
    return sorted(obras, key=lambda obra: obra.titulo)

if __name__ == "__main__":
    obras = [
        ObraDeArte("Monalisa", "Leonardo da Vinci", 1503),
        ObraDeArte("A Noite Estrelada", "Vincent van Gogh", 1889),
        ObraDeArte("O Grito", "Edvard Munch", 1893)
    ]
    
    print("Obras de arte antes da ordenação:")
    for obra in obras:
        print(obra)
    
    obras_ordenadas = ordenar_por_titulo(obras)
    
    print("\nObras de arte ordenadas por título:")
    for obra in obras_ordenadas:
        print(obra)

import pickle

class ObraDeArte:
    def __init__(self, titulo, autor, data_criacao):
        self.titulo = titulo
        self.autor = autor
        self.data_criacao = data_criacao
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.data_criacao})"
    
    def to_dict(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'data_criacao': self.data_criacao
        }
    
    @classmethod
    def from_dict(cls, obra_dict):
        return cls(obra_dict['titulo'], obra_dict['autor'], obra_dict['data_criacao'])

def salvar_obras(obras, filename):
    with open(filename, 'wb') as file:
        pickle.dump([obra.to_dict() for obra in obras], file)

def carregar_obras(filename):
    try:
        with open(filename, 'rb') as file:
            obras_dict = pickle.load(file)
            return [ObraDeArte.from_dict(obra_dict) for obra_dict in obras_dict]
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    obras = [
        ObraDeArte("Monalisa", "Leonardo da Vinci", 1503),
        ObraDeArte("A Noite Estrelada", "Vincent van Gogh", 1889),
        ObraDeArte("O Grito", "Edvard Munch", 1893)
    ]
    
    salvar_obras(obras, 'obras_de_arte.dat')
    obras_carregadas = carregar_obras('obras_de_arte.dat')
    print("Obras de arte carregadas:")
    for obra in obras_carregadas:
        print(obra)

import pickle

class ObraDeArte:
    def __init__(self, titulo, autor, data_criacao):
        self.titulo = titulo
        self.autor = autor
        self.data_criacao = data_criacao
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.data_criacao})"
    
    def to_dict(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'data_criacao': self.data_criacao
        }
    
    @classmethod
    def from_dict(cls, obra_dict):
        return cls(obra_dict['titulo'], obra_dict['autor'], obra_dict['data_criacao'])
def salvar_obras(obras, filename):
    try:
        with open(filename, 'wb') as file:
            pickle.dump([obra.to_dict() for obra in obras], file)
    except (IOError, pickle.PickleError) as e:
        print(f"Erro ao salvar obras de arte: {e}")
def carregar_obras(filename):
    obras_carregadas = []
    try:
        with open(filename, 'rb') as file:
            obras_dict = pickle.load(file)
            obras_carregadas = [ObraDeArte.from_dict(obra_dict) for obra_dict in obras_dict]
    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")
    except (IOError, pickle.PickleError) as e:
        print(f"Erro ao carregar obras de arte: {e}")
    return obras_carregadas

if __name__ == "__main__":
    obras = [
        ObraDeArte("Monalisa", "Leonardo da Vinci", 1503),
        ObraDeArte("A Noite Estrelada", "Vincent van Gogh", 1889),
        ObraDeArte("O Grito", "Edvard Munch", 1893)
    ]
    
    salvar_obras(obras, 'obras_de_arte.dat')
    obras_carregadas = carregar_obras('obras_de_arte.dat')
    print("Obras de arte carregadas:")
    for obra in obras_carregadas:
        print(obra)
