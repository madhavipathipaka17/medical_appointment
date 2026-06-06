# 🏥 Medical Appointment Analytics System

## No-Show Prediction & Demand Forecasting for Healthcare Optimization

---

## 📖 Project Overview

This project is a machine learning-based healthcare analytics system designed to solve two major hospital operational challenges:

### 1️⃣ Patient No-Show Prediction

Predict whether a patient will attend or miss an appointment.

### 2️⃣ Appointment Demand Forecasting

Predict daily hospital appointment demand for better staffing and resource planning.

---

## 🎯 Objectives

* Reduce patient no-shows
* Improve hospital scheduling efficiency
* Optimize staff allocation
* Forecast appointment demand accurately
* Build a deployable Streamlit application

---

## 📊 Dataset Information

### No-Show Dataset

* ~110,000+ appointment records
* Binary target: `no_show`

### Demand Forecasting Dataset

* 498 unique appointment dates (~1.36 years)

**Target:** Daily appointment count

---

## 🧹 Data Preprocessing

### Missing Value Handling

**Age Missing Rate:** ~21%

**Strategy**

* Median imputation
* Added `age_missing` indicator

### Feature Cleaning Decisions

* Removed inconsistent age-group flags
* Fixed encoding mismatches
* Standardized categorical variables

---

## ⚙️ Feature Engineering

### Patient Features

* Age
* Gender
* Disability encoding:

  * intellectual → 0
  * motor → 1
  * unknown → 2
* Hypertension
* Diabetes

### Appointment Features

* Appointment time
* SMS received
* Day of week

### Location Features

* Encoded hospital place

### Specialty Encoding

| Specialty            | Code |
| -------------------- | ---- |
| assist               | 0    |
| enf                  | 1    |
| occupational therapy | 2    |
| pedagogo             | 3    |
| physiotherapy        | 4    |
| psychotherapy        | 5    |
| sem especialidade    | 6    |
| speech therapy       | 7    |
| unknown              | 8    |
