# Contributing to Notion Covers Generator

Thank you for your interest in contributing to the Notion Covers Generator! We welcome contributions from the community to help make this project better.

## 🤝 How to Contribute

Feel free to contribute in any of the following ways:

### 📝 Content Contributions
- **Add more quotes**: Expand the collection in the JSON files located in the `data/` folder
  - `stoic_quotes.json` - Add philosophical quotes from Stoic philosophy
  - `anime_quotes.json` - Add inspirational quotes from anime characters
- **Add more book recommendations**: Expand the `books.json` file with classic and popular books

### 🎨 Design Improvements
- **Improve the image designs**: Enhance the visual aesthetics of generated images
- **Add new themes**: Create additional color schemes and visual styles
- **Enhance typography**: Improve font selection and text layout

### ✨ Feature Enhancements
- **Add new image generation features**: Create new types of Notion cover images
- **Improve existing generators**: Enhance the functionality of current image types
- **Add customization options**: Provide more user control over image appearance

## 📁 File Structure

When contributing, please be aware of the project structure:

```
notion-covers/
├── data/                  # JSON files containing quotes and book data
├── fonts/                 # Font files used for text rendering
├── templates/             # (Empty) Reserved for future background templates
├── output/                # Generated images (auto-created)
├── main.py               # Main terminal interface
├── image_generator.py    # Core image generation logic
└── requirements.txt      # Python dependencies
```

## 🛠️ Development Guidelines

### Code Style
- Follow Python PEP 8 style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and modular

### Data Format
When adding to JSON files:
- **Quotes**: Ensure proper attribution and accuracy
- **Books**: Include title, author, and publication year
- **Anime Quotes**: Include quote, character name, and anime title

### Testing
- Test your changes locally before submitting
- Ensure all image types generate correctly
- Verify the terminal interface works as expected

## 📋 Submission Process

1. **Fork the repository**
2. **Create a feature branch** for your changes
3. **Make your changes** following the guidelines above
4. **Test thoroughly** to ensure everything works
5. **Submit a pull request** with a clear description of your changes

## 💡 Ideas for Contributions

Here are some ideas if you're looking for ways to contribute:

- Add quotes from other philosophical traditions
- Include quotes from movies, books, or historical figures
- Create seasonal or holiday-themed generators
- Add support for different image dimensions
- Implement more sophisticated gradient patterns
- Add text shadow or outline effects
- Create template-based background systems

## 🐛 Bug Reports

If you find bugs or issues:
1. Check if the issue already exists in the project's issues
2. Create a detailed bug report with steps to reproduce
3. Include your Python version and operating system
4. Provide screenshots if applicable

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

Thank you for helping make Notion Covers Generator better! 🎨