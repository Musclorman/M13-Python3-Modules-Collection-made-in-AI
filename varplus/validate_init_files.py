# -*- coding: utf-8 -*-
"""
Script de Validation - Vérification de la Cohérence des __init__.py

Ce script vérifie que tous les fichiers __init__.py contiennent
les informations correctes sur le projet variableplus.
"""

import os
import sys

def check_init_file(filepath, module_name=None):
    """Vérifier un fichier __init__.py"""
    print(f"\n{'='*70}")
    print(f"Checking: {module_name or os.path.basename(os.path.dirname(filepath))}")
    print(f"Path: {filepath}")
    print('='*70)
    
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Vérifications
    checks = {
        'Project name (variableplus)': '__project__' in content or 'variableplus' in content,
        'Author (Musclor13)': 'Musclor13' in content,
        'AI Assistance mention': 'AI' in content or 'assistance' in content.lower(),
        'MIT License': 'MIT' in content,
        'No email address': '@' not in content or 'example.com' not in content,
        'Version defined': '__version__' in content,
        'Copyright notice': '__copyright__' in content or 'Copyright' in content,
    }
    
    # Afficher les résultats
    all_passed = True
    for check_name, result in checks.items():
        status = "✓" if result else "❌"
        print(f"{status} {check_name}")
        if not result:
            all_passed = False
    
    return all_passed

def main():
    """Main validation"""
    print("\n" + "█"*70)
    print("█ variableplus - __init__.py Validation Report")
    print("█"*70)
    
    base_path = "c:\\Users\\Musclor13\\Documents\\PYTHON\\variableplus"
    
    files_to_check = {
        '__init__.py': 'Root Project',
        'generic_tree\\__init__.py': 'generic_tree Module',
        'MenuMaker\\__init__.py': 'MenuMaker Module',
        'Multidimention_table\\__init__.py': 'Multidimention_table Module',
        'Multidimention_table\\multidimention_paint\\__init__.py': 'multidimention_paint Module',
    }
    
    results = {}
    
    for relative_path, module_name in files_to_check.items():
        full_path = os.path.join(base_path, relative_path)
        results[module_name] = check_init_file(full_path, module_name)
    
    # Résumé final
    print(f"\n\n{'='*70}")
    print("VALIDATION SUMMARY")
    print('='*70)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for module_name, result in results.items():
        status = "✓ PASS" if result else "❌ FAIL"
        print(f"{status}: {module_name}")
    
    print(f"\nTotal: {passed}/{total} modules passed validation")
    
    if passed == total:
        print("\n🎉 All validations passed! The project is properly configured.")
    else:
        print(f"\n⚠️  {total - passed} module(s) need attention.")
    
    print("="*70)

if __name__ == '__main__':
    main()
