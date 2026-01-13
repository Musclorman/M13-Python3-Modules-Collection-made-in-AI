# MenuMaker - Documentação em Português

## 🎯 Visão Geral

MenuMaker é um módulo Python que facilita a criação de interfaces de menu interativas em aplicações CLI (Command Line Interface). Permite criar menus complexos com navegação intuitiva.

## ✨ Características Principais

1. **Menus Hierárquicos** - Suporte para menus aninhados e submenus
2. **Navegação Intuitiva** - Seleção com número ou letra
3. **Ações Personalizadas** - Vincular funções a itens de menu
4. **Estilos Configuráveis** - Personalizar aparência e comportamento
5. **Validação** - Validar seleções de usuário automaticamente
6. **Histórico** - Rastrear histórico de seleções
7. **Temas** - Múltiplos temas de cores disponíveis
8. **Interatividade** - Suporte para entrada interativa

## 🚀 Início Rápido

### Criar Menu Simples
```python
from menu import Menu, MenuItem

# Criar menu
menu = Menu("Menu Principal")
menu.add_item(MenuItem("1", "Opção 1", lambda: print("Opção 1 selecionada")))
menu.add_item(MenuItem("2", "Opção 2", lambda: print("Opção 2 selecionada")))
menu.add_item(MenuItem("q", "Sair", None))

# Exibir e executar
menu.display()
```

### Menu com Submenus
```python
# Menu principal
main_menu = Menu("Menu Principal")

# Submenu
sub_menu = Menu("Submenu")
sub_menu.add_item(MenuItem("a", "Ação A", lambda: print("A")))
sub_menu.add_item(MenuItem("b", "Ação B", lambda: print("B")))

# Adicionar submenu ao principal
main_menu.add_submenu(MenuItem("s", "Submenu", sub_menu))

main_menu.display()
```

## 📊 Componentes Principais

### Classe Menu
```python
class Menu:
    """Representa um menu interativo."""
    
    def __init__(self, título, estilos=None):
        """Inicializa um menu com título."""
        self.titulo = título
        self.itens = []
        self.estilos = estilos or {}
    
    def add_item(self, item):
        """Adiciona um item ao menu."""
        self.itens.append(item)
    
    def add_submenu(self, submenu):
        """Adiciona um submenu."""
        self.itens.append(submenu)
    
    def display(self):
        """Exibe o menu e aguarda entrada."""
        # Lógica de exibição
        pass
```

### Classe MenuItem
```python
class MenuItem:
    """Representa um item de menu."""
    
    def __init__(self, chave, descrição, ação=None):
        """Inicializa um item de menu."""
        self.chave = chave
        self.descrição = descrição
        self.ação = ação
    
    def executar(self):
        """Executa a ação do item."""
        if self.ação:
            self.ação()
```

## 💡 Exemplos de Uso

### Menu de Aplicação
```python
from menu import Menu, MenuItem

def calcular_soma():
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    print(f"Soma: {a + b}")

def calcular_produto():
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    print(f"Produto: {a * b}")

# Criar menu
menu = Menu("Calculadora Simples")
menu.add_item(MenuItem("1", "Somar", calcular_soma))
menu.add_item(MenuItem("2", "Multiplicar", calcular_produto))
menu.add_item(MenuItem("q", "Sair", None))

# Executar
while True:
    menu.display()
    escolha = input("Selecione: ").strip()
    if escolha == "q":
        break
```

### Menu de Configuração
```python
config_menu = Menu("Configurações")
config_menu.add_item(MenuItem("1", "Mudar Idioma", lambda: print("Idioma alterado")))
config_menu.add_item(MenuItem("2", "Mudar Tema", lambda: print("Tema alterado")))
config_menu.add_item(MenuItem("3", "Resetar Padrões", lambda: print("Padrões resetados")))
config_menu.add_item(MenuItem("b", "Voltar", None))
```

## 🎨 Personalização

### Estilos
```python
# Definir estilos personalizados
estilos = {
    "cores": {
        "título": "azul",
        "item": "branco",
        "seleção": "amarelo"
    },
    "separador": "=" * 40,
    "prefixo": "> "
}

menu = Menu("Menu Estilizado", estilos=estilos)
```

### Temas
```python
# Temas pré-definidos
TEMA_CLARO = {"bg": "branco", "fg": "preto"}
TEMA_ESCURO = {"bg": "preto", "fg": "branco"}
TEMA_ALTO_CONTRASTE = {"bg": "amarelo", "fg": "preto"}
```

## 📚 Referência da API

| Método | Descrição |
|--------|-----------|
| `add_item(item)` | Adiciona item ao menu |
| `add_submenu(submenu)` | Adiciona submenu |
| `display()` | Exibe menu e aguarda entrada |
| `get_item(chave)` | Recupera item por chave |
| `clear()` | Limpa todos os itens |
| `set_estilos(estilos)` | Define estilos |
| `get_historico()` | Retorna histórico de seleções |

## 🧪 Testes

Execute os testes com:

```bash
python test_menumaker.py
```

## 🔗 Módulos Relacionados

- [Generic Tree](../../generic_tree/) - Estrutura de árvore
- [Multidimensional Table](../Multidimention_table/) - Tabelas de dados
- [MultidimensionalPaint](../Multidimention_table/multidimention_paint/) - Visualização

## 📝 Informações da Versão

- **Versão**: 1.0.0
- **Status**: Estável
- **Linguagem**: Python 3.7+
- **Licença**: MIT

## 📄 Licença

Este projeto é licenciado sob a licença MIT.
