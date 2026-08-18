# Netflix Movies and TV Shows — EDA & Power BI Dashboard

## Project Overview

This project analyzes the **Netflix Movies and TV Shows dataset** to understand Netflix's content distribution, countries, genres, ratings, and content added over the years.

The project includes **data cleaning, exploratory data analysis (EDA), and an interactive Power BI dashboard**.

## Objectives

* Clean and prepare the Netflix dataset
* Analyze Movies and TV Shows distribution
* Identify the countries with the most Netflix content
* Analyze popular genres
* Analyze content ratings
* Study Netflix content added by year
* Compare Movies and TV Shows added over time
* Create an interactive Power BI dashboard

## Dataset

The dataset contains information about Netflix Movies and TV Shows, including:

* Type
* Title
* Director
* Country
* Date Added
* Release Year
* Rating
* Duration
* Genre
* Year Added
* Month Added

## Data Cleaning

The following data-cleaning steps were performed:

* Checked dataset information and structure
* Checked missing values
* Handled missing categorical values using `Unknown`
* Removed unnecessary columns such as `show_id`, `cast`, and `description`
* Removed duplicate records
* Converted `date_added` into a proper datetime format
* Created `year_added` and `month_added` columns
* Removed records with invalid/missing date information
* Exported the cleaned dataset as `netflix_cleaned.csv`

## Exploratory Data Analysis

The following analyses were performed:

### 1. Movies vs TV Shows

Analyzed the distribution of Movies and TV Shows available on Netflix.

### 2. Content Added by Year

Analyzed the number of Netflix titles added each year.

### 3. Top Countries

Identified the countries producing the most Netflix content.

### 4. Top Genres

Analyzed the most common genres/categories on Netflix.

### 5. Content Ratings

Analyzed the distribution of Netflix content based on ratings.

### 6. Movies vs TV Shows Over Time

Compared the number of Movies and TV Shows added across different years.

## Tools & Technologies

* **Python**
* **Pandas**
* **Matplotlib**
* **Jupyter Notebook**
* **Power BI**
* **CSV Dataset**

## Project Files

```text
Netflix-Movies-TV-Shows-EDA/
│
├── Netflix.py
├── netflix_cleaned.csv
└── README.md
```

## Power BI Dashboard

The cleaned dataset was imported into Power BI to create an interactive dashboard for visualizing Netflix content insights.

The dashboard includes visualizations related to:

* Total Titles
* Movies vs TV Shows
* Content by Year
* Top Countries
* Top Genres
* Ratings
* Other Netflix content insights

## Key Insights

* Netflix contains both Movies and TV Shows across many countries.
* Content has been added to Netflix across multiple years.
* Movies and TV Shows show different patterns over time.
* Certain countries contribute significantly more content than others.
* Some genres and ratings are more common than others.

## Conclusion

This project demonstrates the complete workflow of a data analysis project, starting from **data cleaning and EDA in Python** and continuing with **interactive visualization in Power BI**.

It provides useful insights into Netflix's content library and demonstrates practical skills in **Python, Pandas, Data Analysis, Data Visualization, and Power BI**.

