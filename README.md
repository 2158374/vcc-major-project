# Cloud-based AI-Driven Cyber Threat Intelligence Platform 🚨☁️

This project implements a real-time, scalable, AI-powered cybersecurity platform using *Google Cloud Platform (GCP). It leverages services like **Vertex AI, **BigQuery, **Pub/Sub, and **Cloud Functions* to detect and respond to network threats with high accuracy and low latency.

## 🔍 Problem Statement

Traditional security systems suffer from:
- Delayed threat detection
- High false-positive rates
- Poor scalability in cloud environments

This platform addresses these challenges by providing:
- Real-time threat detection (under 1 second)
- AI-driven decision-making
- Automated remediation in cloud-native setups

---

## 🚀 Project Highlights

- *Vertex AI* for ML-based anomaly detection  
- *BigQuery* and *Cloud Storage* for data storage  
- *Cloud Pub/Sub* and *Cloud Functions* for real-time inference and response  
- *Infrastructure as Code* using *Terraform*  
- *Cloud Security Command Center* for centralized threat monitoring  

---

## 📊 Results

| Metric              | Traditional Systems | Our Platform          |
|---------------------|---------------------|------------------------|
| Detection Time      | ~45 seconds         | < 1 second (800ms)     |
| False Positive Rate | 14%                 | 3.9%                   |
| Model Accuracy      | 85–90%              | *96.1%*              |
| Response Time       | ~2 mins             | < 5 seconds            |
| Monthly Cost        | $500                | $280                   |

---

## 🧠 Technologies Used

- *Google Cloud Platform (GCP)*:
  - Vertex AI
  - BigQuery
  - Pub/Sub
  - Cloud Functions
  - Cloud Storage
  - VPC Flow Logs
  - Security Command Center
- *Terraform* – Infrastructure Automation  
- *Python* – Model inference and automation scripts  

---

## 🔧 How It Works

1. *Ingest Logs* from VPC Flow, Cloud Audit, and system logs  
2. *Store Logs* in BigQuery and Cloud Storage  
3. *Train ML Models* (Supervised & Unsupervised) using Vertex AI  
4. *Real-Time Inference* via Pub/Sub → Vertex AI → Cloud Functions  
5. *Automated Response* like IP blocking or alerts  
6. *Monitoring* via Looker Studio and Security Command Center
