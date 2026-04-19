# ⚙️ Feature Engineering on Restaurant Dataset

## 📌 Overview
This project focuses on transforming raw restaurant data into meaningful features that can be used for further analysis or machine learning models. Feature engineering helps improve model performance by creating useful inputs from existing data.

## 🎯 Objective
- Create new meaningful features from existing columns  
- Convert categorical data into numerical format  
- Prepare dataset for machine learning tasks  

## 🛠️ Tools & Technologies
- Python  
- Pandas  

## 📂 Dataset Details
The dataset includes:
- Restaurant Name  
- Address  
- Has Table Booking  
- Has Online Delivery  
- Aggregate Rating  
- Price Range  

## 🔍 Methodology

### 1. Name Length Feature
- Created a new column:
  - **Name Length** = length of restaurant name  
- Helps analyze patterns like branding vs rating  

### 2. Address Length Feature
- Created:
  - **Address Length** = length of address  
- Can indicate location detail or complexity  

### 3. Encoding Table Booking
- Converted:
  - Yes → 1  
  - No → 0  
- New column: `Table Booking (Encoded)`  

### 4. Encoding Online Delivery
- Converted:
  - Yes → 1  
  - No → 0  
- New column: `Online Delivery (Encoded)`  

### 5. Dataset Transformation
- Original dataset expanded with new features  
- Previewed updated dataset  

### 6. Saving Processed Data
- Final dataset saved as:
```
processed_dataset.csv
```

## 📊 Output

<img width="1484" height="806" alt="Image" src="https://github.com/user-attachments/assets/08d03d09-42df-4fe9-af05-fd4d57f10446" />

## 🚀 How to Run

1. Install dependencies:
```bash
pip install pandas
```

2. Run the script:
```bash
python "Task 6.py"
```

## 📁 Project Structure

```
Feature-Engineering/
│
├── Task 6.py
├── Dataset.csv
├── processed_dataset.csv
└── README.md
```

## 🚀 Key Insights

- Feature engineering helps convert raw data into useful signals  
- Encoding categorical variables is essential for machine learning  
- New features like name length and address length can reveal hidden patterns  
- Processed dataset is now ready for:
  - Machine Learning  
  - Advanced Analysis  

## 🎯 Conclusion

This task demonstrates how raw data can be transformed into a structured and model-ready format. Feature engineering plays a crucial role in improving data quality and enabling better insights and predictions.

---

