#!/usr/bin/env python3
"""
Setup script for APA - Advanced Pavement Analytics

This script provides utilities for setting up the development environment
and installing the APA package.
"""

import os
import subprocess
import sys
from pathlib import Path


def create_virtualenv(venv_dir: str = 'venv_apa') -> None:
    """
    Create a virtual environment for development.
    
    Args:
        venv_dir: Name of the virtual environment directory
    """
    if not os.path.exists(venv_dir):
        subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])
        print(f"✓ Virtual environment created at {venv_dir}")
    else:
        print(f"✓ Virtual environment already exists at {venv_dir}")


def install_requirements(venv_dir: str = 'venv_apa') -> None:
    """
    Install requirements in the virtual environment.
    
    Args:
        venv_dir: Name of the virtual environment directory
    """
    if sys.platform == "win32":
        pip_path = os.path.join(venv_dir, 'Scripts', 'pip')
    else:
        pip_path = os.path.join(venv_dir, 'bin', 'pip')
    
    # Install requirements
    subprocess.check_call([pip_path, 'install', '-r', 'requirements.txt'])
    print("✓ Requirements installed")
    
    # Install the package in development mode
    subprocess.check_call([pip_path, 'install', '-e', '.'])
    print("✓ APA package installed in development mode")


def install_dev_requirements(venv_dir: str = 'venv_apa') -> None:
    """
    Install development requirements.
    
    Args:
        venv_dir: Name of the virtual environment directory
    """
    if sys.platform == "win32":
        pip_path = os.path.join(venv_dir, 'Scripts', 'pip')
    else:
        pip_path = os.path.join(venv_dir, 'bin', 'pip')
    
    # Install development dependencies
    subprocess.check_call([pip_path, 'install', '-e', '.[dev]'])
    print("✓ Development requirements installed")


def setup_pre_commit() -> None:
    """Set up pre-commit hooks."""
    try:
        subprocess.check_call(['pre-commit', 'install'])
        print("✓ Pre-commit hooks installed")
    except subprocess.CalledProcessError:
        print("⚠ Pre-commit not available, skipping hook installation")
    except FileNotFoundError:
        print("⚠ Pre-commit not found, skipping hook installation")


def run_tests() -> None:
    """Run the test suite."""
    try:
        subprocess.check_call(['pytest', 'tests/', '-v'])
        print("✓ All tests passed")
    except subprocess.CalledProcessError:
        print("✗ Some tests failed")
    except FileNotFoundError:
        print("⚠ pytest not found, skipping tests")


def main():
    """Main setup function."""
    print(" Setting up APA development environment...")
    
    # Create virtual environment
    create_virtualenv()
    
    # Install requirements
    install_requirements()
    
    # Ask if user wants to install dev requirements
    response = input("\n📦 Install development requirements? (y/n): ").lower().strip()
    if response in ['y', 'yes']:
        install_dev_requirements()
        setup_pre_commit()
    
    # Ask if user wants to run tests
    response = input("\n🧪 Run tests? (y/n): ").lower().strip()
    if response in ['y', 'yes']:
        run_tests()
    
    print("\n✅ Setup complete!")
    print("\nTo activate the virtual environment:")
    if sys.platform == "win32":
        print(f"  {os.path.join('venv_apa', 'Scripts', 'activate')}")
    else:
        print(f"  source venv_apa/bin/activate")
    
    print("\nTo run the APA CLI:")
    print("  apa --help")


if __name__ == "__main__":
    main()
