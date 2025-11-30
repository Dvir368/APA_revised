# 🛣️ APA – Advanced Pavement Analytics

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

**APA (Advanced Pavement Analytics)** is a geospatial AI pipeline that uses **satellite imagery** to predict the **Pavement Condition Index (PCI)** of urban roads.

## 🎯 Key Features

- **🌍 Geospatial AI Pipeline**: Process satellite imagery for road condition assessment
- **🤖 Deep Learning Models**: U-Net and CNN architectures for pavement analysis
- **📊 PCI Prediction**: Accurate Pavement Condition Index estimation
- **🗺️ Multi-Source Data**: Support for various satellite imagery sources
- **⚙️ Configurable**: YAML-based configuration system
- **📈 Comprehensive Analytics**: Detailed metrics and visualization tools
- **🔧 CLI Interface**: Easy-to-use command-line tools

##  Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/apa-inc/apa.git
cd apa

# Create virtual environment
python -m venv venv_apa
source venv_apa/bin/activate  # On Windows: venv_apa\Scripts\activate

# Install APA
pip install -e .

# Or use the setup script
python setup.py
```

### Basic Usage

```bash
# Run APA with a configuration file
apa run --config configs/detroit.yaml

# Validate configuration
apa validate --config configs/detroit.yaml

# Create new configuration from template
apa create-config --template detroit --output my_config.yaml

# List available templates
apa list-templates
```

### Python API

```python
import apa
from apa.config.manager import ConfigManager
from apa.pipeline.runner import APAPipeline

# Load configuration
config_manager = ConfigManager()
config = config_manager.load_config('configs/detroit.yaml')

# Run pipeline
pipeline = APAPipeline(config['config'])
pipeline.run()

# Get results
results = pipeline.get_results()
```

## 🏗️ Architecture

APA follows a modular architecture with these main components:

```
apa/
├── src/apa/                    # Main package
│   ├── cli.py                 # Command-line interface
│   ├── config/                # Configuration management
│   ├── data/                  # Data import and preprocessing
│   ├── models/                # Machine learning models
│   ├── processing/            # Image processing
│   ├── pipeline/              # Main pipeline orchestration
│   └── utils/                 # Utilities and helpers
├── configs/                   # Configuration files
├── docs/                      # Documentation
├── examples/                  # Example notebooks
├── tests/                     # Test suite
└── scripts/                   # Utility scripts
```

## 🧠 Pipeline Overview

### 1. **Data Import**
- Import hyperspectral satellite imagery
- Load ground truth PCI data
- Support for multiple data sources (VENUS, Airbus, etc.)

### 2. **ROI Processing**
- Define regions of interest
- Crop imagery to relevant areas
- Coordinate system transformations

### 3. **Road Extraction**
- OpenStreetMap integration
- Road network segmentation
- Binary road masks

### 4. **PCI Segmentation**
- Ground truth PCI mapping
- Dijkstra's algorithm for road segmentation
- Pixel-level PCI assignment

### 5. **Data Preparation**
- Neural network input preparation
- Data augmentation
- Train/validation splits

### 6. **Model Training**
- U-Net and CNN architectures
- Multi-phase training
- Performance evaluation

## 📚 Documentation

- **[Installation Guide](docs/installation.md)** - Detailed setup instructions
- **[Quick Start Guide](docs/quickstart.md)** - Get up and running quickly
- **[Configuration Reference](docs/configuration.md)** - Configuration options
- **[API Documentation](docs/api/)** - Complete API reference
- **[Tutorials](docs/tutorials/)** - Step-by-step guides
- **[Examples](examples/)** - Example notebooks and scripts

## 🔧 Development

### Setting up Development Environment

```bash
# Install development dependencies
pip install -e .[dev]

# Set up pre-commit hooks
pre-commit install

# Run tests
pytest

# Run linting
black src/
isort src/
flake8 src/
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run the test suite (`pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📊 Supported Data Sources

- **VENUS (Israel)**: Kiryat Ata region
- **VENUS (Detroit)**: Detroit metropolitan area
- **Airbus (Detroit)**: Multispectral and panchromatic imagery
- **Custom Sources**: Extensible for other satellite data

## 🎯 Use Cases

- **Municipal Planning**: Road maintenance prioritization
- **Infrastructure Assessment**: Large-scale pavement evaluation
- **Research**: Academic studies on road conditions
- **Consulting**: Professional pavement analysis services

## 📈 Performance

- **Accuracy**: High correlation with ground truth PCI values
- **Speed**: Optimized for large-scale processing
- **Scalability**: Handles city-wide datasets efficiently
- **Reproducibility**: Consistent results across different environments

## 🤝 Support

- **Documentation**: [https://apa.readthedocs.io](https://apa.readthedocs.io)
- **Issues**: [GitHub Issues](https://github.com/apa-inc/apa/issues)
- **Discussions**: [GitHub Discussions](https://github.com/apa-inc/apa/discussions)
- **Email**: contact@apa.inc

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Satellite imagery providers
- OpenStreetMap contributors
- The open-source community
- Research collaborators

## 🔗 Related Projects

- [U-Net for Road Segmentation](src/ImagePreProcessModule/DeepLearningFilteringModule/U_Net_Satellite/)
- [Segment Anything Model](src/ImagePreProcessModule/DeepLearningFilteringModule/segment-anything/)
- [Aerial Image Road Segmentation](src/ImagePreProcessModule/DeepLearningFilteringModule/aerial-image-road-segmentation-xp/)

---

**Made with ❤️ by the APA team**
