# APA Tutorials

Welcome to the APA tutorials! These step-by-step guides will help you understand and use the APA (Advanced Pavement Analytics) pipeline effectively.

## 📚 Available Tutorials

### 1. [APA Pipeline: A University Student's Guide](apa_pipeline_intro.md)
**Perfect for:** University students, beginners, anyone new to professional software development

**What you'll learn:**
- Why we use APIs and Managers instead of simple functions
- How professional software projects are structured
- The building blocks of the APA pipeline
- How modularity makes software maintainable and scalable
- Real-world examples of each module

**Prerequisites:** Basic Python knowledge

---

## 🎯 Tutorial Roadmap

### For Beginners
1. **Start here:** [APA Pipeline: A University Student's Guide](apa_pipeline_intro.md)
2. **Next:** Try the [Basic Usage Example](../../examples/basic_usage.ipynb)
3. **Then:** Explore the [API Documentation](../api/index.md)

### For Intermediate Users
1. **Configuration Management:** [Configuration API](../api/config/index.md)
2. **Data Processing:** [Data Management API](../api/data/index.md)
3. **Pipeline Execution:** [Pipeline API](../api/pipeline/index.md)

### For Advanced Users
1. **Custom Models:** [Models API](../api/models/index.md)
2. **Image Processing:** [Processing API](../api/processing/index.md)
3. **Utilities:** [Utilities API](../api/utils/index.md)

---

##  Quick Start

### 1. Installation
```bash
# Clone the repository
git clone https://github.com/apa-inc/apa.git
cd apa

# Install APA
pip install -e .

# Activate virtual environment
source venv_apa/bin/activate
```

### 2. Run Your First Pipeline
```python
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
print(f"Processed {len(results['processed_rois'])} ROIs")
```

### 3. Explore Individual Components
```python
# Explore data import
from apa.data.importers import DataImporter
importer = DataImporter(config['config'])

# Explore visualization
from apa.utils.visualization import VisualizationUtils
viz = VisualizationUtils()

# Explore metrics
from apa.utils.metrics import MetricsCalculator
metrics = MetricsCalculator()
```

---

## 📖 Additional Resources

- **[Installation Guide](../installation.md)** - Detailed setup instructions
- **[API Documentation](../api/index.md)** - Complete API reference
- **[Configuration Reference](../configuration.md)** - Configuration options
- **[Examples](../../examples/)** - Example notebooks and scripts

---

## 🤝 Getting Help

- **Documentation**: Check the specific tutorial or API documentation
- **Examples**: Look at the example notebooks
- **Issues**: Open an issue on GitHub
- **Discussions**: Join the GitHub discussions

---

**Happy Learning!** 🎓

*These tutorials are designed to help you understand professional software development practices through the lens of the APA project. Use them as a stepping stone to building your own professional software projects.*


