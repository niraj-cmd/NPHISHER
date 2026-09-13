# 🌐 NPHISHER — Web Snapshot & Local Testing Tool

<p align="center">

**Automated Website Rendering • HTML Snapshot • Screenshot Verification • Localhost Hosting**

</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge\&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-Chromium-green?style=for-the-badge)
![Localhost](https://img.shields.io/badge/Server-Localhost-orange?style=for-the-badge)

</p>

---

## 📌 About

**NPHISHER** is a Python-based web snapshot utility built with **Playwright**.

It launches a headless Chromium browser, loads an authorized target website, renders the page, triggers lazy-loaded content, saves the resulting HTML, creates a full-page screenshot, and finally hosts the generated snapshot locally.

The main implementation is:

👉 [NPHISHER.py](https://github.com/niraj-cmd/site-cloner/blob/main/NPHISHER.py)

> **Important:** Despite the filename, this project should only be used for authorized website testing, development, UI research, CTF/lab environments, and archiving. Do not use it to impersonate services or collect credentials.

---

## ✨ Features

* 🚀 Automated Chromium rendering
* 🌐 Supports HTTP and HTTPS URLs
* 📄 Saves the rendered HTML snapshot
* 📸 Creates a full-page screenshot
* 🔄 Scrolls the page to trigger lazy-loaded content
* 📁 Automatically creates the output directory
* 🖥️ Built-in localhost HTTP server
* ⚡ Asynchronous Playwright automation
* 🔍 Useful for UI testing and visual verification

---

## 📂 Project Structure

```text
site-cloner/
│
├── NPHISHER.py
├── requirements.txt
├── README.md
│
└── cloned_exact_site/
    ├── index.html
    └── screenshot.png
```

The `cloned_exact_site` directory is created automatically when the script runs.

---

## 🧰 Requirements

* Python **3.10+**
* Playwright
* Chromium browser installed through Playwright

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/niraj-cmd/site-cloner.git
cd site-cloner
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Chromium

```bash
playwright install chromium
```

---

## ▶️ Running NPHISHER

Start the script:

```bash
python NPHISHER.py
```

You will be prompted for a URL:

```text
=== 100% VISUAL ACCURACY SITE COPIER & LOCAL HOST ===

Enter the full website URL to clone:
```

Enter an authorized URL, for example:

```text
https://example.com
```

The program then:

```text
Target URL
    │
    ▼
Playwright / Chromium
    │
    ▼
Render webpage
    │
    ▼
Trigger lazy-loaded content
    │
    ├───────────────┐
    ▼               ▼
index.html     screenshot.png
    │               │
    └───────┬───────┘
            ▼
      Local HTTP Server
            │
            ▼
   http://localhost:8080
```

---

## 📁 Generated Files

After the script finishes:

```text
cloned_exact_site/
├── index.html
└── screenshot.png
```

### `index.html`

Contains the HTML generated from the rendered page.

### `screenshot.png`

Contains a full-page screenshot captured by Playwright for visual verification.

---

## 🖥️ Localhost

NPHISHER automatically starts a local HTTP server on port `8080`.

Open:

```text
http://localhost:8080
```

The terminal will display:

```text
[Server] Active! Open your browser and go to:
http://localhost:8080
```

Stop the server with:

```text
Ctrl + C
```

---

## ⚙️ Configuration

The default port is:

```python
start_local_host(port=8080)
```

To use another port:

```python
start_local_host(port=3000)
```

Then visit:

```text
http://localhost:3000
```

---

## 🔍 How the Script Works

### 1. URL Validation

The program checks that the supplied URL starts with:

```text
http://
```

or:

```text
https://
```

### 2. Chromium Launch

Playwright starts Chromium in headless mode.

### 3. Page Rendering

The target page is loaded using:

```python
wait_until="networkidle"
```

with a 60-second timeout.

### 4. Lazy-Load Trigger

The script scrolls to the bottom of the page and waits briefly before returning to the top.

This can cause lazy-loaded page elements to render.

### 5. HTML Capture

The final rendered DOM is retrieved using Playwright and written to:

```text
cloned_exact_site/index.html
```

### 6. Screenshot

A full-page screenshot is generated:

```text
cloned_exact_site/screenshot.png
```

### 7. Local Hosting

Python's built-in HTTP server serves the generated directory.

---

## ⚠️ Important Limitations

This project captures the **rendered HTML**, not necessarily a completely self-contained offline copy.

External resources may still be referenced from their original locations, including:

* CSS
* JavaScript
* Images
* Fonts
* APIs
* CDN resources

Therefore, some websites may not function correctly when hosted locally.

Server-side functionality is also not copied by this script.

---

## 🧪 Safe Testing

For testing, use:

* Your own website
* Local development applications
* Authorized staging environments
* CTF/lab applications
* Intentionally vulnerable training applications

For example:

```text
http://localhost:9000
```

You can create a simple local test server with:

```bash
python -m http.server 9000
```

Then run:

```bash
python NPHISHER.py
```

and enter:

```text
http://localhost:9000
```

---

## 🛡️ Responsible Use

This tool is intended for **authorized security research, development, testing, education, and website archiving**.

Do not use it to:

* Impersonate legitimate services
* Deploy phishing pages
* Collect usernames or passwords
* Harvest authentication information
* Deceive users
* Bypass authentication
* Reproduce websites without authorization

Only snapshot websites that you own or have explicit permission to test.

---

## 🐛 Troubleshooting

### `ModuleNotFoundError: No module named 'playwright'`

Run:

```bash
pip install -r requirements.txt
```

### Chromium is missing

Run:

```bash
playwright install chromium
```

### Port 8080 is already in use

Change:

```python
start_local_host(port=8080)
```

to:

```python
start_local_host(port=8081)
```

### Website does not load

Check:

* URL is valid
* Internet connection is available
* Website is reachable
* Target permits access
* Page does not require unavailable authentication/session state

### Some assets are missing

The current implementation saves the rendered HTML but does not download every external resource into the output directory. External assets may therefore continue to depend on the original website.

---

## 📜 License

If you distribute this project publicly, consider adding an appropriate open-source license such as MIT.

---

## 👨‍💻 Author

**Niraj Ashtaputre**

GitHub:

https://github.com/niraj-cmd

Repository:

https://github.com/niraj-cmd/site-cloner

---

## ⭐ Project Purpose

NPHISHER is designed as a learning and research project for:

```text
Web Automation
       │
       ├── Playwright
       ├── Chromium
       ├── HTML Rendering
       ├── Screenshot Testing
       └── Local Web Hosting
```

**Built for authorized testing, learning, and security research.**

---
