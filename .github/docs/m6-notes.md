# Módulo 6 - Introdução ao Design de Código

> [retornar](../../README.md) para a página anterior

## Sumário

- [Módulo 6 - Introdução ao Design de Código](#módulo-6---introdução-ao-design-de-código)
  - [Sumário](#sumário)
  - [Atributos, Médotos e Classes Privadas](#atributos-médotos-e-classes-privadas)
    - [Métodos e Atributos Privados](#métodos-e-atributos-privados)
    - [Classes Privadas (usando nested classes)](#classes-privadas-usando-nested-classes)
    - [Encapsulamento por Convenção](#encapsulamento-por-convenção)
    - [Métodos e Atributos Privados com Decoradores](#métodos-e-atributos-privados-com-decoradores)
    - [Classes Privadas (usando métodos estáticos)](#classes-privadas-usando-métodos-estáticos)
    - [Encapsulamento por Convenção em Métodos de Acesso](#encapsulamento-por-convenção-em-métodos-de-acesso)
    - [Atributos Privados com Property](#atributos-privados-com-property)
    - [Classes Privadas com Métodos de Fábrica](#classes-privadas-com-métodos-de-fábrica)
    - [Métodos e Atributos Privados com Convenção de Nomeação](#métodos-e-atributos-privados-com-convenção-de-nomeação)
    - [Atributos Privados com Métodos de Acesso](#atributos-privados-com-métodos-de-acesso)
  - [Questionário Avaliativo do Módulo 6](#questionário-avaliativo-do-módulo-6)

## Atributos, Médotos e Classes Privadas

Em Python, a convenção é que tudo é público por padrão, o que significa que métodos e atributos podem ser acessados de fora da classe. No entanto, é possível definir métodos e atributos como privados, o que impede o acesso externo. Aqui estão alguns exemplos de como trabalhar com métodos, atributos e classes privadas em Python:

### Métodos e Atributos Privados

```python
class MinhaClasse:
    def __init__(self):
        self.__atributo_privado = 10  # Atributo privado
    
    def __metodo_privado(self):
        print("Este é um método privado")

    def metodo_publico(self):
        print("Este é um método público")
        self.__metodo_privado()  # Método privado acessível dentro da classe
        print(self.__atributo_privado)  # Atributo privado acessível dentro da classe

# Criando uma instância da classe
obj = MinhaClasse()

# Tentando acessar métodos e atributos privados de fora da classe
# Isso resultará em um erro
obj.__metodo_privado()
print(obj.__atributo_privado)
```

### Classes Privadas (usando nested classes)

```python
class Outer:
    def __init__(self):
        self.__inner = self.__Inner()  # Instanciando uma classe interna

    class __Inner:
        def __init__(self):
            print("Instância da classe interna criada")

# Tentando acessar a classe interna de fora da classe externa
# Isso resultará em um erro
obj = Outer.__Inner()

# Criando uma instância da classe externa
obj = Outer()
```

### Encapsulamento por Convenção

Embora Python não tenha modificadores de acesso como em outras linguagens, é comum usar uma convenção de nomeação para indicar que um método ou atributo deve ser tratado como privado. Isso é feito prefixando o nome com um sublinhado único ou duplo. No entanto, isso é mais uma convenção, e não uma regra rígida:

```python
class MinhaClasse:
    def __init__(self):
        self._atributo_protected = 20  # Atributo "protegido" por convenção
    
    def _metodo_protected(self):
        print("Este é um método 'protegido'")

# Ainda é possível acessar métodos e atributos "protegidos",
# mas é uma indicação de que não deveriam ser acessados diretamente.
obj = MinhaClasse()
print(obj._atributo_protected)
obj._metodo_protected()
```

### Métodos e Atributos Privados com Decoradores

```python
class MinhaClasse:
    def __init__(self):
        self.__atributo_privado = 10  # Atributo privado
    
    def __metodo_privado(self):
        print("Este é um método privado")

    def metodo_publico(self):
        print("Este é um método público")
        self.__metodo_privado()  # Método privado acessível dentro da classe
        print(self.__atributo_privado)  # Atributo privado acessível dentro da classe

    # Decorador property para acessar o atributo privado
    @property
    def atributo_privado(self):
        return self.__atributo_privado

# Criando uma instância da classe
obj = MinhaClasse()

# Usando o decorador property para acessar o atributo privado
print(obj.atributo_privado)

# Tentando acessar métodos e atributos privados diretamente
# Fora da classe resultará em um erro
obj.__metodo_privado()
print(obj.__atributo_privado)
```

### Classes Privadas (usando métodos estáticos)

```python
class Outer:
    def __init__(self):
        self.__inner = self.__Inner()  # Instanciando uma classe interna

    class __Inner:
        def __init__(self):
            print("Instância da classe interna criada")

        @staticmethod
        def metodo_privado():
            print("Este é um método privado estático")

# Criando uma instância da classe externa
obj = Outer()

# Tentando acessar a classe interna de fora da classe externa
# Isso resultará em um erro
obj = Outer.__Inner()

# Chamando o método privado estático da classe interna
obj.__Inner.metodo_privado()
```

### Encapsulamento por Convenção em Métodos de Acesso

```python
class MinhaClasse:
    def __init__(self):
        self._atributo_protected = 20  # Atributo "protegido" por convenção
    
    def _metodo_protected(self):
        print("Este é um método 'protegido'")

    # Métodos de acesso para atributo "protegido"
    def get_atributo_protected(self):
        return self._atributo_protected

    def set_atributo_protected(self, valor):
        self._atributo_protected = valor

# Criando uma instância da classe
obj = MinhaClasse()

# Usando métodos de acesso para atributo "protegido"
print(obj.get_atributo_protected())
obj.set_atributo_protected(30)
print(obj.get_atributo_protected())

# Tentando acessar diretamente o atributo "protegido"
# ou chamar o método "protegido" resultará em um erro
print(obj._atributo_protected)
obj._metodo_protected()
```

### Atributos Privados com Property

```python
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # Atributo privado

    # Método getter usando property
    @property
    def nome(self):
        return self.__nome

    # Método setter usando property
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string")

# Criando uma instância da classe
pessoa = Pessoa("João")

# Acessando o atributo privado usando property
print(pessoa.nome)  # Saída: João

# Alterando o nome usando property
pessoa.nome = "Maria"
print(pessoa.nome)  # Saída: Maria

# Tentando acessar diretamente o atributo privado
# resultará em um erro
print(pessoa.__nome)
```

### Classes Privadas com Métodos de Fábrica

```python
class Fabrica:
    class __Produto:
        def __init__(self, nome):
            self.nome = nome

    @staticmethod
    def criar_produto(nome):
        return Fabrica.__Produto(nome)

# Criando uma instância da classe interna diretamente
# resultará em um erro
produto = Fabrica.__Produto("Produto A")

# Criando um produto usando o método de fábrica
produto = Fabrica.criar_produto("Produto B")
print(produto.nome)  # Saída: Produto B
```

### Métodos e Atributos Privados com Convenção de Nomeação

```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # Atributo "privado" por convenção

    def _metodo_privado(self):
        print("Este é um método 'privado'")

    # Método público que acessa o atributo e chama o método "privado"
    def saudacao(self):
        print(f"Olá, meu nome é {self._nome}.")
        self._metodo_privado()

# Criando uma instância da classe
pessoa = Pessoa("João")

# Usando o método público
pessoa.saudacao()

# Tentando acessar o atributo e chamar o método "privado" diretamente
# Não gera erro, mas é uma convenção indicando que não deveriam ser acessados diretamente
print(pessoa._nome)
pessoa._metodo_privado()
```

### Atributos Privados com Métodos de Acesso

```python
class Carro:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privadoP

    # Métodos de acesso para os atributos privados
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

# Criando uma instância da classe
carro = Carro("Toyota", "Corolla")

# Usando métodos de acesso para obter os atributos privados
print(carro.get_marca())  # Saída: Toyota
print(carro.get_modelo())  # Saída: Corolla

# Usando métodos de acesso para alterar os atributos privados
carro.set_marca("Honda")
carro.set_modelo("Civic")

# Imprimindo os atributos alterados
print(carro.get_marca())  # Saída: Honda
print(carro.get_modelo())  # Saída: Civic
```

## Questionário Avaliativo - Módulo 6

1 - *O que são testes de integração?* - **Resposta:** Testes que verificam a comunicação entre diferentes módulos de um sistema.

2 - *O que é o `pytest`?* - **Resposta:** Uma biblioteca para realizar testes em Python.

3 - *O que é uma exceção?* - **Resposta:** Uma condição que indica um erro durante a execução de um programa

4 - *Para que serve o parâmetro self em um método de uma classe?* - **Resposta:** Para referenciar a própria instância da classe dentro do método.

5 - *Para que serve um código HTTP 400?* - **Resposta:** Indica que a requisição foi mal-formada.

6 - *O que são testes unitários?* - **Resposta:** Testes que verificam o funcionamento de um único módulo em isolamento

7 - *Testes que verificam a usabilidade do sistema por diferentes tipos de usuários.* - **Resposta:** Ferramentas que facilitam a criação e execução de testes automatizados.

8 - *O que é um mock?* - **Resposta:** Um objeto falso que simula o comportamento de um objeto real para fins de teste.

9 - *Qual a principal vantagem de usar mocks em testes?* - **Resposta:** Aumentar a cobertura de testes do sistema em ambiente controlado.

10 - *O que é o design pattern Facade?* - **Resposta:** Um padrão de projeto que define como objetos podem interagir entre si.

11 - *O que é o design pattern Factory?* - **Resposta:** Um padrão de projeto que cria objetos de forma dinâmica

> [voltar](#módulo-6---introdução-ao-design-de-código) ao topo da página
>
> [retornar](../../README.md) para a página anterior
