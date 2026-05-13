# Silent Burnout AI

Silent Burnout AI is a machine learning-based early warning system designed to detect academic disengagement and potential silent burnout risk among students using Learning Management System (LMS) behavioral data and academic performance indicators.

The system predicts whether a student belongs to a **Low Risk**, **Moderate Risk**, or **High Risk / Potential Withdrawal** category and displays the result through an interactive Streamlit dashboard.

---

## Live Demo

The Silent Burnout AI web application is deployed using Streamlit Community Cloud.

**Live App:** https://silent-burnout.streamlit.app/

---

## Application Screenshot

The screenshot below shows the Silent Burnout AI Streamlit application, including the input form, prediction result, confidence score, risk probability distribution, and engagement profile visualization.

![Silent Burnout AI Application Screenshot]((images/app_screenshot.pdf))

---

## Project Overview

Academic disengagement is often detected only after a student’s performance has already declined. Traditional monitoring systems mainly depend on grades, attendance, or final assessment outcomes. However, early signs of disengagement can appear through behavioral changes such as reduced LMS activity, fewer resource interactions, irregular participation, and inconsistent academic submissions.

Silent Burnout AI uses behavioral and academic features to identify these early warning signs and classify students into different risk levels.

---

## Problem Statement

Student disengagement is usually a gradual process. Students may continue to remain enrolled while slowly reducing their learning activity, interaction frequency, and academic consistency. This hidden disengagement is referred to as **silent burnout**.

The objective of this project is to build a machine learning system that can detect early signs of academic disengagement using LMS interaction data and academic performance features.

---

## Objectives

- Detect early signs of student disengagement using behavioral and academic data
- Analyze LMS activity patterns such as clicks, active days, and resource access
- Engineer meaningful features from student interaction and assessment data
- Train and compare machine learning models
- Select the best-performing model for risk prediction
- Build an interactive Streamlit dashboard for real-time prediction
- Display risk probability and engagement profile visualizations
- Support educators with early warning insights for possible intervention

---

## Dataset

This project uses the **Open University Learning Analytics Dataset (OULAD)**, which contains student demographic, assessment, and LMS interaction data.

The dataset includes:

- Student information
- LMS activity logs
- Assessment scores
- Resource interaction records

Large dataset files are not uploaded directly to this repository due to GitHub file size limits.

### Required Dataset Files

- `studentInfo.csv`
- `studentVle.csv`
- `studentAssessment.csv`

### Dataset Download

Download the required dataset files from the external link below:

```text
https://drive.google.com/drive/folders/1dS52H3CIp6VWURuL07V7qS2BxxPi3oQ9?usp=sharing
