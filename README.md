# Skincare Web Scraper: Building a Dynamic Product-Ingredient Dataset
Technologies: Python, BeautifulSoup, Requests, Web Scraping, JSON

This project scrapes skincare product data, including product names, brands, and ingredients, from INCIDecoder, a popular, user-updated database for skincare formulations. The scraper outputs a clean JSON file mapping products to their ingredient lists:

[
  {
    "Name": "Example Product",
    "Ingredients": ["Water", "Niacinamide", "Glycerin", ...]
  },
  ...
]

# Motivation & Use Case
While working on a personal project to detect harmful or incompatible ingredient combinations in skincare routines, I hit a major **roadblock**:
  The ack of accessible, up-to-date skincare product APIs or databases. Many were outdated, shut down, or undocumented.

**To solve this, I:**

  1. Built a scalable web scraper targeting live product listings on INCIDecoder.
  
  2. Designed the scraper to reflect new product additions, since the site allows user submissions.
  
  3. Open-sourced it to help others working on skincare-related projects or research.

# What I Learned
- Developed fluency in BeautifulSoup and HTML parsing.

- Deepened my understanding of website structures and dynamic search pagination.

- Researched and considered the legal and ethical implications of web scraping, practicing responsible use.

