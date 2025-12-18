# Open-Source Telecom Service Assurance Platform

## Overview
This project is a basic open-source telecom service assurance platform built to monitor network services and support SLA compliance using SNMP.

## Problem Statement
Telecom service providers need continuous monitoring of network performance to ensure service reliability and SLA compliance. Commercial tools are expensive and complex, so this project demonstrates a simple open-source alternative.

## What This Project Does
- Collects SNMP metrics from network devices
- Stores metrics in a local database
- Displays metrics using a web dashboard
- Visualizes data using tables and graphs
- Represents the service assurance flow visually

## Architecture / Workflow
1. SNMP agent runs on the device
2. Python script polls SNMP metrics
3. Data is stored in SQLite database
4. Flask backend serves the data
5. Web UI displays charts and tables

## Technologies Used
- Ubuntu (VirtualBox)
- SNMP
- Python
- Flask
- SQLite
- HTML, CSS, JavaScript
- Chart.js
- Git and GitHub

## How to Run the Project
1. Clone the repository
2. Create and activate Python virtual environment
3. Install required libraries
4. Start SNMP service
5. Run SNMP collector
6. Run Flask application
7. Open browser and view dashboard

## Future Enhancements
- RESTCONF-based service monitoring
- AI-based QoS prediction
- SLA breach detection and alerts
- Support for multiple devices

## Author
Thanish Seemakurthi
