#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================
    KPU DATA EXTRACTOR - INSTALLATION SCRIPT
    Complete Project Setup with Dependencies
================================================================
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

class ProjectSetup:
    def __init__(self):
        self.project_name = "KPUDataExtractor"
        self.version = "5.0.0"
        self.author = "System Admin"
        self.base_dir = Path(__file__).parent
        self.requirements = [
            'requests>=2.31.0',
            'colorama>=0.4.6',
            'tqdm>=4.66.1',
            'pandas>=2.0.3',
            'openpyxl>=3.1.2',
            'python-dotenv>=1.0.0',
            'PyInquirer>=1.0.3',
            'tabulate>=0.9.0'
        ]
        
    def print_banner(self):
        """Print installation banner"""
        banner = f"""
╔══════════════════════════════════════════════════════════════╗
║                    KPU DATA EXTRACTOR v{self.version}                    ║
║                Complete Installation Setup                   ║
╚══════════════════════════════════════════════════════════════╝
"""
        print(banner)
    
    def check_python_version(self):
        """Check Python version"""
        print("[1/6] Checking Python version...")
        if sys.version_info < (3, 7):
            print("❌ Python 3.7 or higher is required!")
            sys.exit(1)
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    def create_project_structure(self):
        """Create complete project structure"""
        print("\n[2/6] Creating project structure...")
        
        directories = [
            'src',
            'src/core',
            'src/api',
            'src/database',
            'src/utils',
            'src/export',
            'src/reports',
            'data',
            'data/raw',
            'data/processed',
            'data/exports',
            'logs',
            'config',
            'docs',
            'tests',
            'bin',
            'tmp'
        ]
        
        files = [
            'src/__init__.py',
            'src/core/__init__.py',
            'src/api/__init__.py',
            'src/database/__init__.py',
            'src/utils/__init__.py',
            'src/export/__init__.py',
            'src/reports/__init__.py',
            'config/settings.json',
            'config/api_config.json',
            '.env.example',
            'requirements.txt',
            'README.md',
            'CHANGELOG.md',
            'LICENSE',
            'run.py',
            'cleanup.py'
        ]
        
        # Create directories
        for directory in directories:
            dir_path = self.base_dir / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"  📁 Created: {directory}")
        
        # Create files
        for file in files:
            file_path = self.base_dir / file
            if not file_path.exists():
                file_path.touch()
                print(f"  📄 Created: {file}")
        
        # Create .gitignore
        gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Project
data/exports/*
!data/exports/.gitkeep
logs/*
!logs/.gitkeep
tmp/*
!tmp/.gitkeep

# Environment
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
"""
        
        gitignore_path = self.base_dir / '.gitignore'
        gitignore_path.write_text(gitignore_content)
        print("  📄 Created: .gitignore")
        
        print("✅ Project structure created successfully!")
    
    def create_config_files(self):
        """Create configuration files"""
        print("\n[3/6] Creating configuration files...")
        
        # settings.json
        settings = {
            "app": {
                "name": "KPU Data Extractor",
                "version": self.version,
                "author": self.author,
                "description": "Complete KPU/KOMINFO Data Extraction Tool"
            },
            "database": {
                "path": "data/kpu_database.db",
                "backup_interval": 3600,
                "max_connections": 10
            },
            "api": {
                "timeout": 30,
                "retry_attempts": 3,
                "rate_limit": 10,
                "user_agent": "KPU-Data-Extractor/5.0"
            },
            "export": {
                "default_format": "csv",
                "encoding": "utf-8",
                "include_timestamp": True
            },
            "logging": {
                "level": "INFO",
                "max_size_mb": 10,
                "backup_count": 5
            }
        }
        
        settings_path = self.base_dir / 'config' / 'settings.json'
        settings_path.write_text(json.dumps(settings, indent=2))
        print("  📄 Created: config/settings.json")
        
        # api_config.json
        api_config = {
            "endpoints": {
                "dpt_check": "https://cekdptonline.kpu.go.id",
                "pemilu_data": "https://sirekap-obj.kpu.go.id",
                "wilayah": "https://wilayah-kpu.go.id",
                "pilkada": "https://pilkada2024.kpu.go.id"
            },
            "headers": {
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
        }
        
        api_config_path = self.base_dir / 'config' / 'api_config.json'
        api_config_path.write_text(json.dumps(api_config, indent=2))
        print("  📄 Created: config/api_config.json")
        
        # .env.example
        env_example = """# Database Configuration
DB_PATH=data/kpu_database.db
DB_BACKUP_ENABLED=true

# API Configuration
API_TIMEOUT=30
API_RETRY_COUNT=3
API_RATE_LIMIT=10

# Export Configuration
EXPORT_FORMAT=csv
EXPORT_ENCODING=utf-8

# Logging Configuration
LOG_LEVEL=INFO
LOG_MAX_SIZE=10485760
LOG_BACKUP_COUNT=5

# Application Configuration
APP_NAME=KPU Data Extractor
APP_VERSION=5.0.0
"""
        
        env_path = self.base_dir / '.env.example'
        env_path.write_text(env_example)
        print("  📄 Created: .env.example")
        
        print("✅ Configuration files created!")
    
    def install_dependencies(self):
        """Install Python dependencies"""
        print("\n[4/6] Installing dependencies...")
        
        # Create requirements.txt
        req_content = "\n".join(self.requirements)
        req_path = self.base_dir / 'requirements.txt'
        req_path.write_text(req_content)
        
        try:
            # Install using pip
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Dependencies installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install dependencies: {e}")
            print("Please install manually: pip install -r requirements.txt")
    
    def create_main_files(self):
        """Create main application files"""
        print("\n[5/6] Creating main application files...")
        
        # run.py - Main entry point
        run_py = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
        run_py += f'''
"""
===============================================================
    KPU DATA EXTRACTOR - MAIN ENTRY POINT
    Version: {self.version}
===============================================================
"""

import sys
import os
from pathlib import Path

# Add src to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / 'src'))

from src.app.main import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\\n⚠️  Application interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\\n❌ Fatal error: {{e}}")
        sys.exit(1)
'''
        
        run_path = self.base_dir / 'run.py'
        run_path.write_text(run_py)
        print("  📄 Created: run.py")
        
        # cleanup.py
        cleanup_py = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
        cleanup_py += f'''
"""
Cleanup script for KPU Data Extractor
"""

import os
import shutil
from pathlib import Path

def cleanup():
    """Clean temporary files and cache"""
    project_root = Path(__file__).parent
    
    # Directories to clean
    temp_dirs = [
        project_root / '__pycache__',
        project_root / 'tmp',
        project_root / 'logs'  # Keep logs, just clear contents
    ]
    
    # Files to remove
    temp_files = [
        project_root / '.DS_Store',
        project_root / 'thumbs.db'
    ]
    
    print("🧹 Cleaning project...")
    
    # Clean directories
    for dir_path in temp_dirs:
        if dir_path.exists():
            if dir_path.name == 'logs':
                # Clear log files but keep directory
                for file in dir_path.glob('*.log'):
                    file.unlink()
                print(f"  ✅ Cleared: {dir_path.name}/")
            else:
                shutil.rmtree(dir_path)
                print(f"  ✅ Removed: {dir_path.name}/")
    
    # Remove temp files
    for file_path in temp_files:
        if file_path.exists():
            file_path.unlink()
            print(f"  ✅ Removed: {file_path.name}")
    
    print("✅ Cleanup completed!")

if __name__ == "__main__":
    cleanup()
'''
        
        cleanup_path = self.base_dir / 'cleanup.py'
        cleanup_path.write_text(cleanup_py)
        print("  📄 Created: cleanup.py")
        
        print("✅ Main files created!")
    
    def create_documentation(self):
        """Create documentation files"""
        print("\n[6/6] Creating documentation...")
        
        # README.md
        readme_content = f"""# KPU Data Extractor v{self.version}

Complete data extraction tool for KPU/KOMINFO public APIs.

## 🚀 Features

- ✅ Data DPT lookup by NIK
- ✅ TPS results checking
- ✅ Wilayah data extraction
- ✅ Batch NIK processing
- ✅ Multiple export formats (CSV, Excel, JSON)
- ✅ Database storage with SQLite
- ✅ Comprehensive logging
- ✅ Clean and structured code

## 📁 Project Structure
