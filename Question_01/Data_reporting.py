# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sr0F3HBpozmoI7Yq_NuuW-Z55qJWPrn2
"""

import os
import requests
import psutil
from datetime import datetime
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Function to get network metrics
def get_network_metrics():
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }

# Function to get Disk I/O metrics
def get_disk_io_metrics():
    disk_io = psutil.disk_io_counters()
    return {
        'read_bytes': disk_io.read_bytes,
        'write_bytes': disk_io.write_bytes,
        'read_count': disk_io.read_count,
        'write_count': disk_io.write_count
    }

def get_application_metrics():

    app_response_time = 150  # Simulated response time in milliseconds
    active_sessions = 42
    return {
        'response_time': app_response_time,
        'active_sessions': active_sessions
    }

def check_external_service_status():

    external_service_url = "https://api.example.com/health"
    try:
        response = requests.get(external_service_url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


# Function to generate the report
def generate_report():
    network_metrics = get_network_metrics()
    disk_io_metrics = get_disk_io_metrics()
    application_metrics = get_application_metrics()
    external_service_status = check_external_service_status()

    report = f"Weekly Performance Report - {datetime.now().strftime('%Y-%m-%d')}\n\n"

    # Network Metrics
    report += "Network Metrics:\n"
    report += f"Bytes Sent: {network_metrics['bytes_sent']}\n"
    report += f"Bytes Received: {network_metrics['bytes_recv']}\n"
    report += f"Packets Sent: {network_metrics['packets_sent']}\n"
    report += f"Packets Received: {network_metrics['packets_recv']}\n\n"

    # Disk I/O Metrics
    report += "Disk I/O Metrics:\n"
    report += f"Read Bytes: {disk_io_metrics['read_bytes']}\n"
    report += f"Write Bytes: {disk_io_metrics['write_bytes']}\n"
    report += f"Read Count: {disk_io_metrics['read_count']}\n"
    report += f"Write Count: {disk_io_metrics['write_count']}\n\n"

    # Application Metrics
    report += "Application Metrics:\n"
    report += f"Response Time: {application_metrics['response_time']} ms\n"
    report += f"Active Sessions: {application_metrics['active_sessions']}\n\n"

    # External Service Dependency Status
    report += "External Service Dependency Status:\n"
    report += f"External Service is {'UP' if external_service_status else 'DOWN'}\n\n"


    return report

# Function to save the report to Google Drive
def save_report_to_drive(report):
    file_name = f"/content/drive/My Drive/performance_report-{datetime.now().strftime('%Y-%m-%d')}.txt"
    with open(file_name, 'w') as file:
        file.write(report)
    print(f"Report saved to {file_name}")

# Main execution
if __name__ == "__main__":
    report = generate_report()
    save_report_to_drive(report)