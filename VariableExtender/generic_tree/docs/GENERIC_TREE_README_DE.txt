Generischer Baum - Umfassende Baumdatenstruktur
===============================================

Übersicht

`generic_tree.py` bietet eine vollständige Implementierung einer generischen n-ären Baumstruktur, die es ermöglicht, alle Arten von Werten in einer hierarchischen Organisation zu speichern und zu manipulieren.

Hauptmerkmale

✓ Unterstützung für alle Werttypen - Ganzzahlen, Strings, Floats, Wörterbücher, Listen, benutzerdefinierte Objekte
✓ N-äre Struktur - Jeder Knoten kann unbegrenzte Kinder haben
✓ Metadaten-Unterstützung - Schlüssel-Wert-Paare pro Knoten
✓ Mehrere Durchlaufmodi - PRE_ORDER, POST_ORDER, LEVEL_ORDER, IN_ORDER
✓ Suchfunktionen - DFS, BFS, nach Wert, nach Prädikat
✓ JSON-Serialisierung - Natives JSON speichern/laden
✓ Funktionale Operationen - Map, Filter, Reduce, Apply
✓ Baumanalyse - Höhe, Tiefe, Ausgleichsprüfung, Blattexytraktion
✓ Baumbehandlung - Sortieren, Umkehren, Klonen

Klassen

TreeNode

Stellt einen einzelnen Knoten im Baum dar.

node = TreeNode(value=5)
node.add_child(10)
node.set_metadata("farbe", "rot")

Hauptmethoden

| Methode | Beschreibung |
|---------|-------------|
| add_child(value) | Kind hinzufügen und Kindknoten zurückgeben |
| add_node(node) | Vorhandenen Knoten als Kind hinzufügen |
| remove_child(node) | Kind entfernen |
| get_child_by_index(index) | Kind nach Index abrufen |
| get_child_by_value(value) | Kind nach Wert abrufen |
| get_children_by_predicate(func) | Kinder abrufen, die Prädikat entsprechen |
| child_count() | Anzahl der Kinder |
| is_leaf() | Überprüfen, ob Knoten ein Blatt ist |
| is_root() | Überprüfen, ob Knoten die Wurzel ist |
| get_depth() | Tiefe von der Wurzel abrufen |
| get_path_to_root() | Pfad zur Wurzel abrufen |
| set_metadata(key, value) | Metadaten setzen |
| get_metadata(key, default=None) | Metadaten abrufen |
| has_metadata(key) | Überprüfen, ob Metadaten vorhanden sind |
| clear_metadata() | Alle Metadaten löschen |
| clone(deep=True) | Knoten klonen |

Tree

Verwaltet die gesamte Baumstruktur.

tree = Tree(root_value="Wurzel")
child = tree.add_child(tree.root, "Kind")

Hauptmethoden

| Methode | Beschreibung |
|---------|-------------|
| add_child(parent, value) | Kind zum Parent hinzufügen |
| add_node(parent, node) | Vorhandenen Knoten hinzufügen |
| remove_child(parent, child) | Kind entfernen |
| get_node_by_value(value) | Knoten nach Wert finden |
| get_nodes_by_predicate(func) | Knoten nach Prädikat finden |
| get_all_leaf_nodes() | Alle Blattknoten abrufen |
| get_all_nodes() | Alle Knoten abrufen |
| get_node_count() | Gesamtknotenzahl |
| get_height() | Baumhöhe |
| traverse(mode, start=None) | Baum durchlaufen |
| to_dict() | In Wörterbuch konvertieren |
| to_json(indent=None) | In JSON konvertieren |
| from_dict(data) | Aus Wörterbuch erstellen |
| from_json(json_str) | Aus JSON erstellen |
| save_to_file(filepath) | In JSON-Datei speichern |
| load_from_file(filepath) | Aus JSON-Datei laden |
| map(func) | Funktion auf alle Knoten anwenden |
| filter(predicate) | Gefilterten Baum erstellen |
| find_path(value) | Pfad zum Wert finden |
| get_common_ancestor(n1, n2) | Gemeinsamen Vorfahren finden |
| print_tree() | Formatierten Baum drucken |
| clear() | Baum löschen |
| reverse_children() | Kinderreihenfolge umkehren |
| sort_children(key=None) | Kinder sortieren |
| depth_first_search(value) | DFS-Suche |
| breadth_first_search(value) | BFS-Suche |
| apply(func) | Funktion auf alle Knoten anwenden |
| reduce(func, initial=None) | Zu einzelnem Wert reduzieren |
| get_siblings(node) | Geschwisterknoten abrufen |
| get_subtree_height(node) | Unterabaumhöhe abrufen |
| is_balanced() | Überprüfen, ob ausgeglichen |

Anwendungsbeispiele

Baum erstellen

tree = Tree(root_value="Wurzel")
child1 = tree.add_child(tree.root, "Kind 1")
child2 = tree.add_child(tree.root, "Kind 2")
grandchild = tree.add_child(child1, "Enkelin")

tree.print_tree()

Suchen

# Nach Wert
node = tree.get_node_by_value("Enkelin")

# Nach Prädikat
string_nodes = tree.get_nodes_by_predicate(lambda x: isinstance(x, str))

# DFS/BFS
node = tree.depth_first_search("Kind 1")

Serialisierung

# Speichern
tree.save_to_file("mein_baum.json")

# Laden
tree = Tree.load_from_file("mein_baum.json")

Reale Anwendungsfälle

1. Dateisysteme
2. Organisationshierarchien
3. Menüstrukturen
4. DOM-Bäume
5. Kategoriehierarchien
6. Abhängigkeitsgraphen

Autor

KI-Assistent - 12. Januar 2026
