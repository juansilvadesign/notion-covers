from PIL import Image, ImageDraw, ImageFont
import json
import random
import os
from datetime import datetime, date
import textwrap

class ImageGenerator:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.fonts_dir = os.path.join(self.base_dir, 'fonts')
        self.data_dir = os.path.join(self.base_dir, 'data')
        self.output_dir = os.path.join(self.base_dir, 'output')
        self.templates_dir = os.path.join(self.base_dir, 'templates')
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Standard image dimensions for Notion covers
        self.width = 1500
        self.height = 600
        
    def get_font(self, font_name, size):
        """Get font with fallback to default if font file not found"""
        font_path = os.path.join(self.fonts_dir, font_name)
        try:
            return ImageFont.truetype(font_path, size)
        except:
            return ImageFont.load_default()
    
    def create_gradient_background(self, color1, color2):
        """Create a simple gradient background"""
        image = Image.new('RGB', (self.width, self.height), color1)
        draw = ImageDraw.Draw(image)
        
        # Simple vertical gradient
        for y in range(self.height):
            ratio = y / self.height
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            draw.line([(0, y), (self.width, y)], fill=(r, g, b))
        
        return image
    
    def create_solid_background(self, color):
        """Create a solid color background"""
        return Image.new('RGB', (self.width, self.height), color)
    
    def load_data(self, filename):
        """Load JSON data from the data directory"""
        filepath = os.path.join(self.data_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def generate_stoic_quote(self, theme='dark'):
        """Generate a stoic quote image"""
        quotes = self.load_data('stoic_quotes.json')
        quote = random.choice(quotes)
        
        # Choose colors based on theme
        if theme == 'dark':
            bg_color = (30, 30, 40)
            text_color = (255, 255, 255)
            accent_color = (180, 180, 180)
        else:
            bg_color = (245, 245, 250)
            text_color = (50, 50, 50)
            accent_color = (100, 100, 100)
        
        # Create background
        image = self.create_solid_background(bg_color)
        draw = ImageDraw.Draw(image)
        
        # Add quote text
        font_large = self.get_font('NewYork.ttf', 32)
        font_small = self.get_font('Helvetica-Neue-Pro-Light.ttf', 18)
        
        # Wrap text
        max_width = self.width - 200
        lines = textwrap.wrap(quote, width=60)
        
        # Calculate total text height
        line_height = 50
        total_height = len(lines) * line_height
        start_y = (self.height - total_height) // 2
        
        # Draw each line centered
        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font_large)
            text_width = bbox[2] - bbox[0]
            x = (self.width - text_width) // 2
            y = start_y + i * line_height
            draw.text((x, y), line, font=font_large, fill=text_color)
        
        # Add attribution
        attribution = "— Stoic Philosophy"
        bbox = draw.textbbox((0, 0), attribution, font=font_small)
        attr_width = bbox[2] - bbox[0]
        attr_x = (self.width - attr_width) // 2
        attr_y = start_y + total_height + 30
        draw.text((attr_x, attr_y), attribution, font=font_small, fill=accent_color)
        
        # Save image
        filename = f"stoic_quote_{theme}.png"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath)
        print(f"✓ Stoic quote image saved: {filepath}")
        return filepath
    
    def generate_anime_quote(self):
        """Generate an anime quote image"""
        quotes = self.load_data('anime_quotes.json')
        quote_data = random.choice(quotes)
        
        # Dark anime-style background
        bg_color1 = (20, 25, 40)
        bg_color2 = (40, 45, 70)
        image = self.create_gradient_background(bg_color1, bg_color2)
        draw = ImageDraw.Draw(image)
        
        # Fonts
        font_quote = self.get_font('Helvetica-Neue-Pro-Light.ttf', 28)
        font_char = self.get_font('NewYork.ttf', 20)
        font_anime = self.get_font('Helvetica-Neue-Pro-Light-Italic.ttf', 16)
        
        # Colors
        text_color = (255, 255, 255)
        char_color = (255, 200, 100)
        anime_color = (200, 200, 200)
        
        # Quote text
        lines = textwrap.wrap(quote_data['quote'], width=50)
        line_height = 45
        total_height = len(lines) * line_height
        start_y = (self.height - total_height - 100) // 2
        
        # Draw quote lines
        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font_quote)
            text_width = bbox[2] - bbox[0]
            x = (self.width - text_width) // 2
            y = start_y + i * line_height
            draw.text((x, y), line, font=font_quote, fill=text_color)
        
        # Character name
        char_text = f"— {quote_data['character']}"
        bbox = draw.textbbox((0, 0), char_text, font=font_char)
        char_width = bbox[2] - bbox[0]
        char_x = (self.width - char_width) // 2
        char_y = start_y + total_height + 20
        draw.text((char_x, char_y), char_text, font=font_char, fill=char_color)
        
        # Anime name
        anime_text = quote_data['anime']
        bbox = draw.textbbox((0, 0), anime_text, font=font_anime)
        anime_width = bbox[2] - bbox[0]
        anime_x = (self.width - anime_width) // 2
        anime_y = char_y + 35
        draw.text((anime_x, anime_y), anime_text, font=font_anime, fill=anime_color)
        
        # Save image
        filename = "anime_quote.png"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath)
        print(f"✓ Anime quote image saved: {filepath}")
        return filepath
    
    def generate_book_recommendation(self, theme='light'):
        """Generate a book recommendation image"""
        books = self.load_data('books.json')
        book = random.choice(books)
        
        # Choose colors based on theme
        if theme == 'dark':
            bg_color = (25, 25, 35)
            text_color = (255, 255, 255)
            accent_color = (200, 200, 200)
        else:
            bg_color = (250, 248, 240)
            text_color = (40, 40, 40)
            accent_color = (80, 80, 80)
        
        # Create background
        image = self.create_solid_background(bg_color)
        draw = ImageDraw.Draw(image)
        
        # Fonts
        font_title = self.get_font('NewYork.ttf', 48)
        font_author = self.get_font('Helvetica-Neue-Pro-Light.ttf', 24)
        font_year = self.get_font('Helvetica-Neue-Pro-Light-Italic.ttf', 18)
        font_label = self.get_font('Helvetica-Neue-Pro-Light.ttf', 20)
        
        # Draw label
        label = "Book Recommendation"
        bbox = draw.textbbox((0, 0), label, font=font_label)
        label_width = bbox[2] - bbox[0]
        label_x = (self.width - label_width) // 2
        draw.text((label_x, 150), label, font=font_label, fill=accent_color)
        
        # Draw title
        title_lines = textwrap.wrap(book['title'], width=30)
        line_height = 60
        start_y = 220
        
        for i, line in enumerate(title_lines):
            bbox = draw.textbbox((0, 0), line, font=font_title)
            text_width = bbox[2] - bbox[0]
            x = (self.width - text_width) // 2
            y = start_y + i * line_height
            draw.text((x, y), line, font=font_title, fill=text_color)
        
        # Draw author
        author_y = start_y + len(title_lines) * line_height + 30
        bbox = draw.textbbox((0, 0), f"by {book['author']}", font=font_author)
        author_width = bbox[2] - bbox[0]
        author_x = (self.width - author_width) // 2
        draw.text((author_x, author_y), f"by {book['author']}", font=font_author, fill=text_color)
        
        # Draw year
        year_y = author_y + 40
        bbox = draw.textbbox((0, 0), f"Published: {book['year']}", font=font_year)
        year_width = bbox[2] - bbox[0]
        year_x = (self.width - year_width) // 2
        draw.text((year_x, year_y), f"Published: {book['year']}", font=font_year, fill=accent_color)
        
        # Save image
        filename = f"book_recommendation_{theme}.png"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath)
        print(f"✓ Book recommendation image saved: {filepath}")
        return filepath
    
    def generate_year_progress(self, theme='light'):
        """Generate year progress image"""
        # Calculate progress
        now = datetime.now()
        start_of_year = datetime(now.year, 1, 1)
        days_passed = (now - start_of_year).days
        days_in_year = 366 if now.year % 4 == 0 else 365
        progress_percentage = int((days_passed / days_in_year) * 100)
        
        # Choose colors based on theme
        if theme == 'dark':
            bg_color = (20, 20, 30)
            text_color = (255, 255, 255)
            progress_color = (100, 200, 100)
            bar_bg_color = (60, 60, 70)
        else:
            bg_color = (248, 248, 252)
            text_color = (40, 40, 40)
            progress_color = (50, 150, 50)
            bar_bg_color = (200, 200, 210)
        
        # Create background
        image = self.create_solid_background(bg_color)
        draw = ImageDraw.Draw(image)
        
        # Fonts
        font_large = self.get_font('NewYork-Bold.ttf', 72)
        font_medium = self.get_font('Helvetica-Neue-Pro-Light.ttf', 24)
        
        # Main percentage
        percentage_text = f"{progress_percentage}%"
        bbox = draw.textbbox((0, 0), percentage_text, font=font_large)
        perc_width = bbox[2] - bbox[0]
        perc_x = (self.width - perc_width) // 2
        draw.text((perc_x, 200), percentage_text, font=font_large, fill=text_color)
        
        # Description
        desc_text = f"of year {now.year} completed"
        bbox = draw.textbbox((0, 0), desc_text, font=font_medium)
        desc_width = bbox[2] - bbox[0]
        desc_x = (self.width - desc_width) // 2
        draw.text((desc_x, 290), desc_text, font=font_medium, fill=text_color)
        
        # Progress bar
        bar_width = 600
        bar_height = 20
        bar_x = (self.width - bar_width) // 2
        bar_y = 350
        
        # Background bar
        draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], 
                      fill=bar_bg_color, outline=None)
        
        # Progress bar
        progress_width = int(bar_width * (progress_percentage / 100))
        draw.rectangle([bar_x, bar_y, bar_x + progress_width, bar_y + bar_height], 
                      fill=progress_color, outline=None)
        
        # Days info
        days_text = f"{days_passed} of {days_in_year} days"
        bbox = draw.textbbox((0, 0), days_text, font=font_medium)
        days_width = bbox[2] - bbox[0]
        days_x = (self.width - days_width) // 2
        draw.text((days_x, 400), days_text, font=font_medium, fill=text_color)
        
        # Save image
        filename = f"year_progress_{theme}.png"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath)
        print(f"✓ Year progress image saved: {filepath}")
        return filepath
    
    def generate_life_progress(self, birth_year, life_expectancy, theme='light'):
        """Generate life progress image"""
        current_year = datetime.now().year
        current_age = current_year - birth_year
        progress_percentage = int((current_age / life_expectancy) * 100)
        
        # Choose colors based on theme
        if theme == 'dark':
            bg_color = (25, 25, 35)
            text_color = (255, 255, 255)
            progress_color = (150, 100, 200)
            bar_bg_color = (60, 60, 70)
        else:
            bg_color = (252, 248, 248)
            text_color = (40, 40, 40)
            progress_color = (120, 80, 160)
            bar_bg_color = (210, 200, 200)
        
        # Create background
        image = self.create_solid_background(bg_color)
        draw = ImageDraw.Draw(image)
        
        # Fonts
        font_large = self.get_font('NewYork.ttf', 60)
        font_medium = self.get_font('Helvetica-Neue-Pro-Light.ttf', 22)
        font_small = self.get_font('Helvetica-Neue-Pro-Light-Italic.ttf', 18)

        # Title
        title = "Life Progress"
        bbox = draw.textbbox((0, 0), title, font=font_medium)
        title_width = bbox[2] - bbox[0]
        title_x = (self.width - title_width) // 2
        draw.text((title_x, 150), title, font=font_medium, fill=text_color)
        
        # Main percentage
        percentage_text = f"{progress_percentage}%"
        bbox = draw.textbbox((0, 0), percentage_text, font=font_large)
        perc_width = bbox[2] - bbox[0]
        perc_x = (self.width - perc_width) // 2
        draw.text((perc_x, 200), percentage_text, font=font_large, fill=text_color)
        
        # Description
        desc_text = f"Age {current_age} of {life_expectancy} years"
        bbox = draw.textbbox((0, 0), desc_text, font=font_medium)
        desc_width = bbox[2] - bbox[0]
        desc_x = (self.width - desc_width) // 2
        draw.text((desc_x, 280), desc_text, font=font_medium, fill=text_color)
        
        # Progress bar
        bar_width = 600
        bar_height = 25
        bar_x = (self.width - bar_width) // 2
        bar_y = 330
        
        # Background bar
        draw.rectangle([bar_x, bar_y, bar_x + bar_width, bar_y + bar_height], 
                      fill=bar_bg_color, outline=None)
        
        # Progress bar
        progress_width = int(bar_width * (progress_percentage / 100))
        draw.rectangle([bar_x, bar_y, bar_x + progress_width, bar_y + bar_height], 
                      fill=progress_color, outline=None)
        
        # Additional info
        years_left = life_expectancy - current_age
        info_text = f"{years_left} years remaining (estimated)"
        bbox = draw.textbbox((0, 0), info_text, font=font_small)
        info_width = bbox[2] - bbox[0]
        info_x = (self.width - info_width) // 2
        draw.text((info_x, 380), info_text, font=font_small, fill=text_color)
        
        # Save image
        filename = f"life_progress_{theme}.png"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath)
        print(f"✓ Life progress image saved: {filepath}")
        return filepath
    
    def generate_motivational_text(self, text, theme='light'):
        """Generate a custom motivational text image"""
        # Choose colors based on theme
        if theme == 'dark':
            bg_color1 = (30, 35, 50)
            bg_color2 = (50, 55, 70)
            text_color = (255, 255, 255)
        else:
            bg_color1 = (240, 245, 250)
            bg_color2 = (250, 250, 255)
            text_color = (50, 50, 50)
        
        # Create gradient background
        image = self.create_gradient_background(bg_color1, bg_color2)
        draw = ImageDraw.Draw(image)
        
        # Font
        font = self.get_font('NewYork.ttf', 36)
        
        # Wrap text
        lines = textwrap.wrap(text, width=40)
        line_height = 55
        total_height = len(lines) * line_height
        start_y = (self.height - total_height) // 2
        
        # Draw each line centered
        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]
            x = (self.width - text_width) // 2
            y = start_y + i * line_height
            draw.text((x, y), line, font=font, fill=text_color)
        
        # Save image
        filename = f"motivational_text_{theme}.png"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath)
        print(f"✓ Motivational text image saved: {filepath}")
        return filepath