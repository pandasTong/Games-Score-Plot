<h1 align = 'center'>
    NBA Final Games - Scores Visualization
    </h1>

## About

## Prerequisite
Download [Chrome WebDriver](https://chromedriver.chromium.org/downloads)
</br>Target [Website](https://www.basketball-reference.com/)
```python
from selenium import webdriver
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration
from matplotlib.patches import Ellipse, Circle, Rectangle
%config InlineBackend.figure_format = 'retina'
```
## Usage
Collecting Scores from 1969-2021 [Scraper](https://github.com/pandasTong/Matplotlib-Practice/blob/main/Score_Scrap.py) <br/>
Detailed Plot [Notebook](https://github.com/pandasTong/Matplotlib-Practice/blob/main/MatPlotLib_Practice.ipynb)

## Sample
![NBA Final Scores](https://user-images.githubusercontent.com/7564386/133545100-50224181-5647-4b76-8fc8-12e9a15ecee0.png)
