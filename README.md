<h1 align = 'center'>
    NBA Final Games - Scores Visualization
    </h1>

## About

## Prepare
+ Collecting Data
  + Download [Chrome WebDriver](https://chromedriver.chromium.org/downloads)
  + Target [Website](https://www.basketball-reference.com/)
  ```python
  from selenium import webdriver
  wd = webdriver.Chrome('chromedriver.exe')
  ```
+ Ploting
  + Basic Plot
  ```python
  import matplotlib.pyplot as plt
  import seaborn as sns
  ```
  + Personalize
  ```python
  from matplotlib.patches import Ellipse, Circle, Rectangle
  %config InlineBackend.figure_format = 'retina'
  ```
  
## Process
+ Scraping
    #### [Py](sss)
+ Cleaning

#### [Dictionary](https://github.com/pandasTong/NBA-Teams-Chinese/blob/5d7f067614cc6b98174364711987ece117dafd00/name-dict.py)

![NBA Final Scores](https://user-images.githubusercontent.com/7564386/133545100-50224181-5647-4b76-8fc8-12e9a15ecee0.png)
