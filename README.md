# 🎨 Notion Covers Generator

A simplified, offline version of the Dynamic Notion Covers generator. This terminal-based application creates beautiful cover images for your Notion pages without requiring any external APIs or internet connection.

![Project's Cover](https://i.ibb.co/GvDP7R11/book-recommendation-dark-1.webp)

## 🚀 Features

- **100% Offline** - No internet connection required
- **Terminal-based Interface** - Simple command-line interaction
- **Multiple Image Types**:
  - 📜 Stoic Philosophy Quotes (Dark & Light themes)
  - 🎌 Anime Quotes
  - 📚 Book Recommendations (Dark & Light themes)
  - 📅 Year Progress Trackers (Dark & Light themes)
  - ⏳ Life Progress Trackers (Dark & Light themes)
  - ✨ Custom Motivational Text (Dark & Light themes)
- **Standard Notion Dimensions** - All images are 1500x600px, perfect for Notion covers

## 📋 Requirements

- Python 3.6 or higher
- Pillow (PIL) library

## 🛠️ Installation

1. **Navigate to the project folder:**
   ```bash
   cd notion-covers
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

1. **Run the main program:**
   ```bash
   python main.py
   ```

2. **Follow the interactive menu:**
   - Choose from 11 different image generation options
   - Provide any required input (like birth year for life progress)
   - Images will be automatically saved to the `output` folder

3. **Open your generated images:**
   - Use option 12 to automatically open the output folder
   - Or manually navigate to the `output` folder

## 🛠 Creating Your Custom Run Script (Windows)

### 📝 Setting Up run.bat

For Windows users, you can create a personalized batch file to quickly launch the application without typing commands each time.

#### ✨ Quick Setup

1. **📋 Copy the Template**
   - Locate the `template.bat` file in the project folder
   - Copy its contents to create your own `run.bat`

2. **✏️ Customize the Path**
   ```batch
   @echo off
   echo Starting notion-covers...
   REM Replace with your actual project path
   "C:\Your\Actual\Path\notion-covers\.env\Scripts\python.exe" main.py
   pause
   ```

3. **🎯 Example Configuration**
   ```batch
   @echo off
   echo Starting notion-covers...
   "C:\Users\YourName\Documents\notion-covers\.env\Scripts\python.exe" main.py
   pause
   ```

#### 🚀 Usage
Once configured, simply double-click your `run.bat` file to launch the application instantly!

> **💡 Pro Tip**: Keep your `run.bat` file local and don't commit it to Git since it contains your specific folder paths.

## 📁 Project Structure

```
notion-covers/
├── main.py                 # Main terminal interface
├── image_generator.py      # Core image generation functions
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── data/                  # Local data files (no APIs needed)
│   ├── stoic_quotes.json  # Collection of stoic philosophy quotes
│   ├── anime_quotes.json  # Collection of anime quotes
│   └── books.json         # Collection of book recommendations
├── fonts/                 # Font files for text rendering
│   ├── NewYork.ttf
│   ├── Helvetica-Neue-Pro-Light.ttf
│   └── Helvetica-Neue-Pro-Light-Italic.ttf
└── output/                # Generated images will be saved here
```

## 🎨 Image Types

### 1. Stoic Quotes
Random philosophical quotes from Stoic philosophy with elegant typography.

### 2. Anime Quotes
Inspirational quotes from popular anime characters with dark, atmospheric backgrounds.

### 3. Book Recommendations
Randomly selected classic and popular books with author information.

### 4. Year Progress
Visual progress bar showing how much of the current year has passed.

### 5. Life Progress
Personalized progress bar showing life progression based on your birth year and estimated life expectancy.

### 6. Custom Motivational Text
Create custom motivational images with your own text input.

## ⚡ Key Differences from Original

This simplified version:
- ❌ **Removed**: Instagram profile integration (required Instagram API)
- ❌ **Removed**: Reddit hot posts (required Reddit API)
- ❌ **Removed**: Weather information (required weather API)
- ❌ **Removed**: Crypto fear & greed index (required external API)
- ❌ **Removed**: Live horoscope data (required astrology API)
- ❌ **Removed**: Moon phase information (required astronomy API)
- ❌ **Removed**: Wall Street Bets sentiment (required Reddit API)
- ❌ **Removed**: Flask web server functionality
- ✅ **Added**: Terminal-based user interface
- ✅ **Added**: Offline quote databases
- ✅ **Added**: Local book recommendations
- ✅ **Simplified**: Image generation using solid colors and gradients instead of complex downloaded backgrounds

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on how to contribute to this project.

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Credits

Based on the original [Dynamic Notion Covers project](https://github.com/juansilvadesign/dynamic-notion-covers), simplified for offline use and ease of deployment.

---

<div align="center">

### 🎉 Thank You for Using Notion Covers Generator!

*Made with 💜 by **Juan Silva***

**⭐ If you found this project helpful, please consider giving it a star!**

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=juansilvadesign.notion-covers)

</div>