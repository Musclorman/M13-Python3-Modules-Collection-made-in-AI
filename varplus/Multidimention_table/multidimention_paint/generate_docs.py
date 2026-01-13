# -*- coding: utf-8 -*-
"""
Documentation Generator Helper
Outil d'aide pour générer la documentation multilingue du module MultidimensionalPaint.
"""

from documentation_generator import DocumentationGenerator
import sys


def generate_docs(output_dir='.'):
    """
    Génère la documentation dans 8 langues.
    Generate documentation in 8 languages.

    Usage:
        python generate_docs.py                    # Generate in current directory
        python generate_docs.py /path/to/output    # Generate in specific directory
    """
    print("\n" + "=" * 70)
    print("MultidimensionalPaint - Documentation Generator")
    print("=" * 70 + "\n")

    generator = DocumentationGenerator(output_dir)
    results = generator.generate_all()

    print("\n" + "=" * 70)
    print("Summary / Résumé")
    print("=" * 70 + "\n")

    # Afficher les résultats
    for filename, success in sorted(results.items()):
        status = "✓" if success else "✗"
        print(f"  {status} {filename}")

    success_count = sum(1 for v in results.values() if v)
    total_count = len(results)

    print(f"\n  Total: {success_count}/{total_count} files generated")
    print(f"  Location: {output_dir}\n")
    print("=" * 70 + "\n")

    return results


if __name__ == '__main__':
    output_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    generate_docs(output_dir)
