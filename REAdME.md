# 🌐 Python Networking Projects

A collection of 5 beginner-friendly Python networking projects designed to help developers understand networking fundamentals, socket programming, DNS resolution, API integration, and network diagnostics.

## 🚀 Projects Included

### 1️⃣ Internet Connection Checker
Checks whether the system has an active internet connection by attempting to establish a socket connection to a public DNS server.

**Concepts Covered**
- Socket Programming
- Network Connectivity Testing
- Exception Handling

---

### 2️⃣ Public IP Address Finder
Fetches the user's public IP address using an external API.

**Concepts Covered**
- REST APIs
- HTTP Requests
- JSON Parsing

---

### 3️⃣ DNS Lookup Tool
Resolves a domain name to its corresponding IP address.

**Concepts Covered**
- DNS Resolution
- Socket Module
- Domain Name Systems

---

### 4️⃣ Website Response Time Checker
Measures the response time of a website and returns its HTTP status code.

**Concepts Covered**
- Performance Monitoring
- HTTP Requests
- Time Measurement

---

### 5️⃣ Internet Speed Test
Tests internet download speed, upload speed, and ping.

**Concepts Covered**
- Network Diagnostics
- Speed Testing
- Third-Party Python Libraries

---

## 📂 Project Structure

```text
python-networking-projects/
│
├── internet_checker/
│   └── main.py
│
├── public_ip_finder/
│   └── main.py
│
├── dns_lookup/
│   └── main.py
│
├── response_time_checker/
│   └── main.py
│
├── speed_test/
│   └── main.py
│
└── README.md
```

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/python-networking-projects.git
```

Navigate to the project:

```bash
cd python-networking-projects
```

Install dependencies:

```bash
pip install requests speedtest-cli
```

---

## ▶️ Running Projects

### Internet Connection Checker

```bash
cd internet_checker
python main.py
```

### Public IP Address Finder

```bash
cd public_ip_finder
python main.py
```

### DNS Lookup Tool

```bash
cd dns_lookup
python main.py
```

### Website Response Time Checker

```bash
cd response_time_checker
python main.py
```

### Internet Speed Test

```bash
cd speed_test
python main.py
```

---

## 📸 Sample Outputs

### Internet Connection Checker

```text
✅ Internet connection is active.
```

### Public IP Finder

```text
Public IP: 103.xxx.xxx.xxx
```

### DNS Lookup

```text
{
  'domain': 'google.com',
  'ip': '142.250.183.14'
}
```

### Website Response Time Checker

```text
{
  'status_code': 200,
  'response_time_ms': 120.5
}
```

### Internet Speed Test

```text
{
  'download_mbps': 89.12,
  'upload_mbps': 42.11,
  'ping_ms': 14.9
}
```

---

## 🎯 Learning Outcomes

By building these projects, you will gain hands-on experience with:

- Python Programming
- Socket Programming
- DNS Resolution
- HTTP Requests
- REST APIs
- Network Diagnostics
- Performance Monitoring
- Exception Handling
- CLI Development
- Internet Protocol Fundamentals

---

## 🔮 Future Improvements

- Build a unified Network Toolkit CLI
- Add GUI using Tkinter or PyQt
- Export results to CSV/JSON
- Add Network Scanner
- Add Port Scanner
- Add Traceroute Utility
- Add WHOIS Lookup Tool

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Happy Coding! 🚀