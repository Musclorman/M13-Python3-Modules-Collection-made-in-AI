# Generic Tree - Documentação em Português

## 🌳 Visão Geral

Generic Tree (Árvore Genérica) é um módulo Python que implementa uma estrutura de dados de árvore flexível e poderosa. Suporta árvores n-árias com qualquer número de filhos por nó.

## ✨ Características Principais

1. **Árvore N-Ária** - Suporta qualquer número de filhos por nó
2. **Nós Genéricos** - Qualquer objeto pode ser armazenado como valor do nó
3. **Navegação Flexível** - Acesso fácil a pais, filhos e irmãos
4. **Busca e Traversal** - Múltiplas estratégias de busca (BFS, DFS)
5. **Manipulação de Árvore** - Adicionar, remover e reorganizar nós
6. **Conversão para String** - Representação visual da árvore
7. **Clonagem** - Criar cópias profundas de árvores
8. **Serialização** - Salvar e carregar árvores

## 🚀 Início Rápido

```python
from generic_tree import GenericTree, Node

# Criar uma árvore simples
root = Node("Raiz")
child1 = Node("Filho 1")
child2 = Node("Filho 2")

root.add_child(child1)
root.add_child(child2)

# Acessar elementos
print(f"Raiz: {root.value}")
print(f"Filhos: {[child.value for child in root.children]}")

# Buscar em largura (BFS)
for node in root.bfs_traversal():
    print(node.value)
```

## 📊 Estrutura de Nós

```python
class Node:
    """Representa um nó na árvore."""
    
    def __init__(self, value):
        """Inicializa um nó com um valor."""
        self.value = value
        self.children = []
        self.parent = None
    
    def add_child(self, child_node):
        """Adiciona um nó filho."""
        self.children.append(child_node)
        child_node.parent = self
    
    def remove_child(self, child_node):
        """Remove um nó filho."""
        self.children.remove(child_node)
        child_node.parent = None
```

## 🔍 Operações de Busca

### Busca em Profundidade (DFS)
```python
# Traversal em profundidade
for node in root.dfs_traversal():
    print(node.value)
```

### Busca em Largura (BFS)
```python
# Traversal em largura
for node in root.bfs_traversal():
    print(node.value)
```

### Busca de Valor
```python
# Encontrar nó com valor específico
found_node = root.find_node("Filho 1")
```

## 📈 Exemplos de Uso

### Criar uma Hierarquia de Organização
```python
empresa = Node("Empresa")
departamento = Node("TI")
equipe = Node("Desenvolvimento")

empresa.add_child(departamento)
departamento.add_child(equipe)

# Obter caminho da raiz
path = equipe.get_path_to_root()
print([n.value for n in path])
```

### Calcular Profundidade
```python
profundidade = node.get_depth()
print(f"Profundidade do nó: {profundidade}")
```

### Contar Nós
```python
total_nós = len(list(root.dfs_traversal()))
print(f"Total de nós: {total_nós}")
```

## 🧪 Testes

O módulo inclui suite completa de testes:

```bash
python test_generic_tree.py
```

## 📚 Referência Completa da API

| Método | Descrição |
|--------|-----------|
| `add_child(child)` | Adiciona um nó filho |
| `remove_child(child)` | Remove um nó filho |
| `dfs_traversal()` | Traversal em profundidade |
| `bfs_traversal()` | Traversal em largura |
| `find_node(value)` | Encontra nó por valor |
| `get_depth()` | Retorna profundidade do nó |
| `get_height()` | Retorna altura da subárvore |
| `get_path_to_root()` | Retorna caminho até raiz |
| `is_leaf()` | Verifica se é folha |
| `clone()` | Cria cópia profunda |

## 📝 Informações da Versão

- **Versão**: 1.0.0
- **Status**: Estável
- **Linguagem**: Python 3.7+
- **Licença**: MIT

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor leia CONTRIBUTING.md para detalhes.

## 📄 Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.
