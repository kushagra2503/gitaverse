# Gitaverse - Bhagavad Gita Analysis Project

A comprehensive Python-based analysis tool for studying and visualizing the Bhagavad Gita, one of the most important spiritual texts in Hinduism.

## 📖 About the Project

This project provides tools and data structures for analyzing the Bhagavad Gita, including:
- Complete chapter information with Sanskrit names and verse counts
- Data processing utilities for spiritual text analysis
- Visualization capabilities for understanding the structure of the Gita

## 🎯 Features

- **Complete Chapter Data**: All 18 chapters with Sanskrit names and verse counts
- **Structured Data**: JSON format for easy processing and analysis
- **Python Integration**: Ready-to-use Python scripts and data structures
- **Extensible Architecture**: Easy to add new analysis features

## 📚 Bhagavad Gita Chapters

The project includes complete information for all 18 chapters:

| Chapter | Sanskrit Name | English Name | Verses |
|---------|---------------|--------------|--------|
| 1 | Arjuna Visada Yoga | The Yoga of Arjuna's Dejection | 47 |
| 2 | Sankhya Yoga | The Yoga of Knowledge | 72 |
| 3 | Karma Yoga | The Yoga of Action | 43 |
| 4 | Jnana Yoga | The Yoga of Knowledge | 42 |
| 5 | Karma Sanyasa Yoga | The Yoga of Renunciation of Action | 29 |
| 6 | Dhyana Yoga | The Yoga of Meditation | 47 |
| 7 | Jnana Vijnana Yoga | The Yoga of Knowledge and Realization | 30 |
| 8 | Aksara Brahma Yoga | The Yoga of the Imperishable Brahman | 28 |
| 9 | Raja Vidya Yoga | The Yoga of the Royal Knowledge | 34 |
| 10 | Vibhuti Yoga | The Yoga of Divine Glories | 42 |
| 11 | Visvarupa Darsana Yoga | The Yoga of the Vision of the Universal Form | 55 |
| 12 | Bhakti Yoga | The Yoga of Devotion | 20 |
| 13 | Ksetra Ksetrajna Vibhaga Yoga | The Yoga of the Distinction Between the Field and the Knower of the Field | 35 |
| 14 | Gunatraya Vibhaga Yoga | The Yoga of the Division of the Three Gunas | 27 |
| 15 | Purusottama Yoga | The Yoga of the Supreme Person | 20 |
| 16 | Daivasura Sampad Vibhaga Yoga | The Yoga of the Division Between the Divine and Demoniacal Natures | 24 |
| 17 | Sraddhatraya Vibhaga Yoga | The Yoga of the Division of Faith | 28 |
| 18 | Moksa Sanyasa Yoga | The Yoga of Liberation by Renunciation | 78 |

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kushagra2503/gitaverse.git
   cd gitaverse
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Dependencies

The project uses the following main dependencies:
- `pandas` - Data manipulation and analysis
- `requests` - HTTP library for API calls
- `boto3` - AWS SDK for Python
- `networkx` - Network analysis and visualization
- `numpy` - Numerical computing
- `matplotlib` - Plotting and visualization
- `seaborn` - Statistical data visualization

## 🛠️ Usage

### Basic Usage

```python
from src.graphGita_claude import CHAPTER_INFO

# Access chapter information
for chapter in CHAPTER_INFO["chapters"]:
    print(f"Chapter {chapter['number']}: {chapter['name']} ({chapter['total_shlokas']} verses)")
```

### Data Analysis

```python
import pandas as pd

# Convert chapter data to DataFrame
df = pd.DataFrame(CHAPTER_INFO["chapters"])
print(df.head())
```

## 📁 Project Structure

```
gitaverse/
├── src/
│   ├── graphGita_claude.py    # Main analysis script
│   └── graphGita_Data.ipynb   # Jupyter notebook for data analysis
├── data/
│   ├── bhagavad_gita_complete.json
│   ├── bhagavad_gita_meta_data.json
│   └── ashtavakra_gita_complete.json
├── images/                    # Generated visualizations
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## 🔗 Sources

The project uses data from the following sources:
- [Bhagavad Gita As It Is (1972 Edition)](https://archive.org/details/bhagavadgitaasitisoriginal1972edition)
- [Bhagavad Gita Original](https://archive.org/details/bhagavadgitaorig0000unse)
- [Gita Press - Shankarbhashya](https://gitapress.org/bookdetail/gita-shankarbhashya-hindi-10)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- The ancient wisdom of the Bhagavad Gita
- The spiritual teachers and commentators who have preserved this knowledge
- The open source community for providing the tools that make this project possible

## 📞 Contact

- **GitHub**: [@kushagra2503](https://github.com/kushagra2503)
- **Repository**: [gitaverse](https://github.com/kushagra2503/gitaverse)

---

*"योग: कर्मसु कौशलम्"* - "Yoga is skill in action" (Bhagavad Gita 2.50)
