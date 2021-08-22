from config import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    cidade = db.Column(db.String(254))
    bairro = db.Column(db.String(254))
    senha = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'{self.id}, {self.nome}, '+\
               f'{self.email}, {self.telefone}, ' +\
                f'{self.cidade}, {self.bairro}, ' +\
                f'{self.senha}'
    
    # método padrão json
    def json(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "email" : self.email,
            "telefone" : self.telefone,
            "cidade" : self.cidade,
            "bairro" : self.bairro,
            "senha" : self.senha
        }


# classe Encontrado para lista de animais cadastrados como Encontrados
class Encontrado(Pessoa):
    # atributos do animal encontrado
    id_encontrado = db.Column(db.Integer, primary_key=True)
    idade = db.Column(db.String(254))
    coleira = db.Column(db.String(254))
    sexo = db.Column(db.String(254))
    tamanho = db.Column(db.String(254))
    pelagem = db.Column(db.String(254))
    especie = db.Column(db.String(254))
    raca = db.Column(db.String(254))
    cor = db.Column(db.String(254))
    descricao = db.Column(db.String(254))
    cidade_encontrado = db.Column(db.String(254))
    bairro_encontrado = db.Column(db.String(254))
    rua_encontrado = db.Column(db.String(254))

    #chave estrangeira
    id_pessoa = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable= False)
    
    
    # método para expressar o animal encontrado em forma de texto
    def __str__(self):
        return f'{self.id_encontrado}, {self.idade}, '+\
               f'{self.coleira}, {self.sexo}, ' +\
                f'{self.tamanho}, {self.pelagem}, ' +\
                f'{self.especie}, {self.raca}, ' +\
                f'{self.cor}, {self.descricao}, ' +\
                f'{self.cidade_encontrado}, {self.bairro_encontrado}, ' +\
                f'{self.rua_encontrado}' 
    
    # método padrão json
    def json(self):
        return {
            "id" : self.id_encontrado,
            "idade" : self.idade,
            "coleira" : self.coleira,
            "sexo" : self.sexo,
            "tamanho" : self.tamanho,
            "pelagem" : self.pelagem,
            "especie" : self.especie,
            "raca" : self.raca,
            "cor" : self.cor,
            "descricao" : self.descricao,
            "cidade" : self.cidade_encontrado,
            "bairro" : self.bairro_encontrado,
            "rua" : self.rua_encontrado
        }

# teste das classe
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()
    
    # teste da classe Pessoa
    p1 = Pessoa(nome = "Julia", email = "ladevigj@gmail123.com", telefone = "55 5555-5555", 
                cidade = "cidade_pessoa", bairro =  "bairro_pessoa", senha = "senha123")
    p2 = Pessoa(nome = "Kathia", email = "k.ladevig2@hotmail.com.br", telefone = "11 1111-1111", 
                cidade = "cidade_pessoa2", bairro =  "bairro_pessoa2", senha = "senha456")       
    #persistir
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    todas = db.session.query(Pessoa).all()
    for p in todas:
        print(p)
        print(p.json())

    # teste da classe Encontrado
    ani1 = Encontrado(idade = "4 anos", coleira = "toda verde", sexo = "fêmea", tamanho = "grande", pelagem = "longa", especie = "cachorro", raca = "vira-lata",
                cor = "preta", descricao = "cachorra com as orelhas compridas",
                cidade_encontrado = "Indaial", bairro_encontrado =  "Estrada das Areias", rua_encontrado = "Marechal Floriano Peixoto")
    
    ani2 = Encontrado(idade = "2 anos", coleira = "preta com estrelinhas brancas", sexo = "macho", tamanho = "médio", pelagem = "curta", especie = "cachorro", raca = "vira-lata",
                cor = "branco" , descricao = "cão muito medroso e com patas longas",
                cidade_encontrado = "Indaial", bairro_encontrado =  "Estrada das Areias", rua_encontrado = "Marechal Floriano Peixoto")
    
    # persistir
    db.session.add(ani1)
    db.session.add(ani2)
    db.session.commit()
    todos = db.session.query(Encontrado).all()
    for animal in todos:
        print(animal)
        print(animal.json())