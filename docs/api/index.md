# APA API Documentation

Welcome to the APA (Advanced Pavement Analytics) API documentation. This comprehensive guide covers all modules, classes, and functions available in the APA package.

## 📚 API Overview

APA is organized into several main modules, each handling specific aspects of the pavement analytics pipeline:

- **[Configuration Management](config/)** - Loading, validation, and management of configuration files
- **[Data Management](data/)** - Data import, preprocessing, and validation
- **[Pipeline Orchestration](pipeline/)** - Main pipeline execution and stage management
- **[Utilities](utils/)** - I/O operations, visualization, and metrics calculation
- **[Models](models/)** - Machine learning models and architectures
- **[Processing](processing/)** - Image processing and filtering operations

##  Quick Start

### Basic Usage

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

### CLI Usage

```bash
# Run the complete pipeline
apa run --config configs/detroit.yaml

# Validate configuration
apa validate --config configs/detroit.yaml

# Create new configuration
apa create-config --template detroit --output my_config.yaml
```

## 📖 Module Documentation

### Configuration Management (`apa.config`)

The configuration module provides tools for managing YAML configuration files with validation and template support.

**Key Classes:**
- `ConfigManager` - Main configuration manager
- `ConfigSchema` - Configuration validation schema

**Features:**
- YAML configuration loading and validation
- Template-based configuration creation
- Default value merging
- Schema validation

[→ Configuration API Documentation](config/)

### Data Management (`apa.data`)

The data module handles importing, preprocessing, and validating data from various sources.

**Key Classes:**
- `DataImporter` - Data import from various sources
- `DataPreprocessor` - Data preprocessing operations
- `DataValidator` - Data validation and quality checks

**Features:**
- Hyperspectral imagery import
- Ground truth PCI data loading
- Road network data from OpenStreetMap
- Data validation and quality assessment

[→ Data Management API Documentation](data/)

### Pipeline Orchestration (`apa.pipeline`)

The pipeline module orchestrates the execution of the complete APA workflow.

**Key Classes:**
- `APAPipeline` - Main pipeline orchestrator
- `PipelineStage` - Individual pipeline stages

**Features:**
- Stage-based pipeline execution
- Error handling and logging
- Progress tracking
- Result management

[→ Pipeline API Documentation](pipeline/)

### Utilities (`apa.utils`)

The utilities module provides helper functions for I/O operations, visualization, and metrics calculation.

**Key Classes:**
- `IOUtils` - File I/O operations
- `VisualizationUtils` - Plotting and visualization
- `MetricsCalculator` - Performance metrics

**Features:**
- Multi-format file I/O (YAML, JSON, HDF5, Pickle)
- Comprehensive plotting tools
- PCI-specific metrics calculation
- Model evaluation metrics

[→ Utilities API Documentation](utils/)

### Models (`apa.models`)

The models module contains machine learning architectures and model management tools.

**Key Classes:**
- `CNNModule` - CNN model implementations
- `UNetModule` - U-Net model implementations
- `ModelManager` - Model training and management

**Features:**
- U-Net architectures for segmentation
- CNN models for classification
- Multi-phase training support
- Model evaluation and metrics

[→ Models API Documentation](models/)

### Processing (`apa.processing`)

The processing module handles image processing, filtering, and geospatial operations.

**Key Classes:**
- `ImageProcessor` - Image processing operations
- `Georeferencer` - Geospatial data processing
- `RoadExtractor` - Road network extraction

**Features:**
- Hyperspectral image processing
- Georeferencing and coordinate transformations
- Road extraction from satellite imagery
- Image filtering and enhancement

[→ Processing API Documentation](processing/)

## 🔧 Common Patterns

### Configuration Loading

```python
from apa.config.manager import ConfigManager

# Initialize manager
config_manager = ConfigManager()

# Load configuration
config = config_manager.load_config('path/to/config.yaml')

# Validate configuration
config_manager.schema.validate(config)

# Create from template
config_manager.create_config_from_template('detroit', 'new_config.yaml')
```

### Data Import

```python
from apa.data.importers import DataImporter

# Initialize importer
importer = DataImporter(config)

# Import hyperspectral data
lon_mat, lat_mat, msp_image, rois = importer.import_hyperspectral_data(
    data_dirname, data_filename, metadata_filename
)

# Import ground truth
ground_truth = importer.import_ground_truth_data(excel_path)

# Validate imported data
is_valid = importer.validate_imported_data(data_dict)
```

### Pipeline Execution

```python
from apa.pipeline.runner import APAPipeline

# Initialize pipeline
pipeline = APAPipeline(config)

# Run complete pipeline
pipeline.run()

# Run specific stages
pipeline.run(['data_import', 'roi_processing'])

# Get results
results = pipeline.get_results()
```

### Visualization

```python
from apa.utils.visualization import VisualizationUtils

# Initialize visualization utils
viz_utils = VisualizationUtils()

# Create ROI overview
viz_utils.plot_roi_overview(roi_data, save_path='roi_overview.png')

# Plot training history
viz_utils.plot_training_history(history, save_path='training.png')

# Create results report
viz_utils.create_results_report(results, 'report.txt')
```

### Metrics Calculation

```python
from apa.utils.metrics import MetricsCalculator

# Initialize metrics calculator
metrics_calc = MetricsCalculator()

# Calculate PCI metrics
pci_metrics = metrics_calc.calculate_pci_metrics(true_pci, pred_pci)

# Calculate classification metrics
class_metrics = metrics_calc.calculate_classification_metrics(y_true, y_pred)

# Generate confusion matrix
cm = metrics_calc.calculate_confusion_matrix(y_true, y_pred)
```

## 🎯 Best Practices

### 1. Configuration Management
- Always validate configurations before use
- Use templates for consistent setups
- Keep sensitive data in separate files

### 2. Error Handling
- Use try-catch blocks for data import operations
- Validate data before processing
- Log errors with appropriate detail levels

### 3. Performance
- Use appropriate batch sizes for large datasets
- Cache intermediate results when possible
- Monitor memory usage during processing

### 4. Testing
- Test individual components before integration
- Use mock data for development
- Validate results against known benchmarks

## 🔗 Related Documentation

- [Installation Guide](../installation.md)
- [Quick Start Guide](../quickstart.md)
- [Configuration Reference](../configuration.md)
- [Tutorials](../tutorials/)
- [Examples](../../examples/)

## 📞 Support

For API-related questions:
- Check the specific module documentation
- Review the example notebooks
- Open an issue on GitHub
- Contact the development team
