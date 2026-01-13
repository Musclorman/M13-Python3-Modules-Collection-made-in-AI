#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PyPI Validation Script for variableplus
Validates that the project is ready for PyPI publication
"""

import sys
import re
from pathlib import Path
from typing import List


class PyPIValidator:
    """Validates project readiness for PyPI publication"""

    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.successes: List[str] = []

    def validate_all(self) -> bool:
        """Run all validation checks"""
        print("=" * 70)
        print("PyPI VALIDATION REPORT - variableplus")
        print("=" * 70)

        self._validate_setup_py()
        self._validate_pyproject_toml()
        self._validate_readme()
        self._validate_license()
        self._validate_init_files()
        self._validate_metadata()
        self._validate_no_emails()
        self._validate_modules()

        self._print_report()
        return len(self.errors) == 0

    def _validate_setup_py(self) -> None:
        """Validate setup.py configuration"""
        print("\n📦 Validating setup.py...")
        setup_file = self.project_root / "setup.py"

        if not setup_file.exists():
            self.errors.append("setup.py not found")
            return

        with open(setup_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for required fields
        if 'name=\'variableplus\'' not in content:
            self.errors.append("setup.py: Package name must be 'variableplus'")
        else:
            self.successes.append("✓ Package name correct: variableplus")

        if 'author=\'Musclor13\'' not in content:
            self.errors.append("setup.py: Author must be 'Musclor13'")
        else:
            self.successes.append("✓ Author correct: Musclor13")

        if 'generic-tree' in content and 'variableplus' not in content:
            self.warnings.append("setup.py: Old 'generic-tree' references found")

        if 'version=' not in content:
            self.errors.append("setup.py: Version not specified")
        else:
            self.successes.append("✓ Version specified")

    def _validate_pyproject_toml(self) -> None:
        """Validate pyproject.toml configuration"""
        print("\n📄 Validating pyproject.toml...")
        toml_file = self.project_root / "pyproject.toml"

        if not toml_file.exists():
            self.errors.append("pyproject.toml not found")
            return

        with open(toml_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for required fields
        if 'name = "variableplus"' not in content:
            self.errors.append("pyproject.toml: Package name must be 'variableplus'")
        else:
            self.successes.append("✓ pyproject.toml: Package name correct")

        if '{name = "Musclor13"}' not in content:
            self.warnings.append("pyproject.toml: Author should be 'Musclor13'")
        else:
            self.successes.append("✓ pyproject.toml: Author correct")

        if '[project]' not in content:
            self.errors.append("pyproject.toml: [project] section missing")
        else:
            self.successes.append("✓ pyproject.toml: [project] section present")

    def _validate_readme(self) -> None:
        """Validate README.md"""
        print("\n📖 Validating README.md...")
        readme_file = self.project_root / "README.md"

        if not readme_file.exists():
            self.errors.append("README.md not found in project root")
            return

        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for bilingual content
        if '## English' not in content:
            self.warnings.append("README.md: English section not found")
        else:
            self.successes.append("✓ README.md: English section present")

        if '## Français' not in content:
            self.warnings.append("README.md: French section not found")
        else:
            self.successes.append("✓ README.md: French section present")

        if 'variableplus' not in content:
            self.errors.append("README.md: Project name not mentioned")
        else:
            self.successes.append("✓ README.md: Project name present")

        if 'Musclor13' not in content:
            self.errors.append("README.md: Author name not mentioned")
        else:
            self.successes.append("✓ README.md: Author mentioned")

        # Check length
        if len(content) < 1000:
            self.warnings.append("README.md: Content seems short (< 1000 chars)")

    def _validate_license(self) -> None:
        """Validate LICENSE file"""
        print("\n⚖️ Validating LICENSE...")
        license_file = self.project_root / "LICENSE"

        if not license_file.exists():
            self.errors.append("LICENSE file not found")
            return

        with open(license_file, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'MIT' not in content and 'MIT License' not in content:
            self.warnings.append("LICENSE: MIT license not detected")
        else:
            self.successes.append("✓ LICENSE: MIT license present")

    def _validate_init_files(self) -> None:
        """Validate __init__.py files"""
        print("\n🐍 Validating __init__.py files...")

        init_files = [
            "variableplus/__init__.py",
            "generic_tree/__init__.py",
            "MenuMaker/__init__.py",
            "Multidimention_table/__init__.py",
            "Multidimention_table/multidimention_paint/__init__.py",
        ]

        for init_file in init_files:
            path = self.project_root / init_file
            if not path.exists():
                self.errors.append(f"Missing: {init_file}")
                continue

            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check for metadata
            if '__project__' in content or '__author__' in content:
                self.successes.append(f"✓ {init_file}: Contains metadata")
            else:
                self.warnings.append(f"{init_file}: Missing metadata")

    def _validate_metadata(self) -> None:
        """Validate metadata consistency"""
        print("\n🏷️ Validating metadata...")

        files_to_check = [
            "setup.py",
            "pyproject.toml",
            "README.md",
        ]

        version_found = False
        for file_name in files_to_check:
            file_path = self.project_root / file_name
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if 'version' in content.lower():
                    version_found = True

        if version_found:
            self.successes.append("✓ Version specified in config files")
        else:
            self.warnings.append("Version not found in any config file")

    def _validate_no_emails(self) -> None:
        """Validate that no email addresses are exposed"""
        print("\n📧 Validating privacy (no exposed emails)...")

        # Email pattern
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        files_to_check = [
            "setup.py",
            "pyproject.toml",
            "README.md",
            "__init__.py",
        ]

        emails_found = []
        for file_pattern in files_to_check:
            for file_path in self.project_root.rglob(file_pattern):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    matches = re.findall(email_pattern, content)
                    for match in matches:
                        if not match.startswith('example.') and \
                           'ai@example' not in match:
                            emails_found.append(f"{file_path}: {match}")
                except Exception:
                    pass

        if emails_found:
            for email in emails_found:
                self.warnings.append(f"Potential email exposure: {email}")
        else:
            self.successes.append("✓ No personal emails exposed")

    def _validate_modules(self) -> None:
        """Validate all required modules"""
        print("\n📚 Validating modules...")

        modules = ["generic_tree", "MenuMaker", "Multidimention_table"]

        for module in modules:
            module_path = self.project_root / module
            if module_path.exists():
                init_file = module_path / "__init__.py"
                if init_file.exists():
                    self.successes.append(f"✓ Module present: {module}")
                else:
                    self.errors.append(f"Missing __init__.py: {module}")
            else:
                self.errors.append(f"Module directory missing: {module}")

    def _print_report(self) -> None:
        """Print validation report"""
        print("\n" + "=" * 70)
        print("VALIDATION RESULTS")
        print("=" * 70)

        if self.successes:
            print(f"\n✅ SUCCESSES ({len(self.successes)}):")
            for success in self.successes:
                print(f"  {success}")

        if self.warnings:
            print(f"\n⚠️ WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  {warning}")

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  {error}")

        print("\n" + "=" * 70)
        if self.errors:
            status = f"FAILED - {len(self.errors)} error(s)"
            print(f"STATUS: {status}")
            print("         Fix errors before publishing to PyPI")
        else:
            status = "SUCCESS - Ready for PyPI"
            print(f"STATUS: {status}")

        print("=" * 70 + "\n")


def main():
    """Main function"""
    project_root = Path.cwd()
    validator = PyPIValidator(project_root)
    success = validator.validate_all()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
