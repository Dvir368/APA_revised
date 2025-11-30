# APA - Advanced Pavement Analytics

Welcome to the APA documentation! APA is a geospatial AI pipeline that uses satellite imagery to predict the Pavement Condition Index (PCI) of urban roads.

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

# Or install with development dependencies
pip install -e .[dev]
```

### Basic Usage

```bash
# Run APA with a configuration file
apa run --config configs/detroit.yaml

# Validate a configuration file
apa validate --config configs/detroit.yaml

# Create a new configuration from template
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

## 📚 Documentation

- [Installation Guide](installation.md) - Detailed installation instructions
- [Quick Start Guide](quickstart.md) - Get up and running quickly
- [Configuration Reference](configuration.md) - Configuration file format and options
- [API Reference](api/) - Complete API documentation
- [Tutorials](tutorials/) - Step-by-step tutorials and guides
- [Examples](examples/) - Example notebooks and scripts

### 🎓 For University Students
- [APA Pipeline: A University Student's Guide](tutorials/apa_pipeline_intro.md) - Learn professional software development practices

## 🏗️ Architecture

APA follows a modular architecture with the following main components:

- **Configuration Management**: Handles loading and validation of configuration files
- **Data Import**: Imports hyperspectral imagery and ground truth data
- **Image Processing**: Preprocesses and filters satellite imagery
- **Road Extraction**: Identifies and segments road networks
- **PCI Prediction**: Uses machine learning to predict pavement conditions
- **Visualization**: Creates plots and reports of results

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
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run the test suite
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

- **Documentation**: [https://apa.readthedocs.io](https://apa.readthedocs.io)
- **Issues**: [GitHub Issues](https://github.com/apa-inc/apa/issues)
- **Discussions**: [GitHub Discussions](https://github.com/apa-inc/apa/discussions)

## 🙏 Acknowledgments

- Satellite imagery providers
- OpenStreetMap contributors
- The open-source community
