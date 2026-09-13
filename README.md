# 🌐 Exact Site Snapshot & Local Host

> A Python-based utility that uses **Playwright** to capture a rendered website, save its HTML snapshot and a full-page screenshot, and serve the captured page locally for testing and visual verification.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge\&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green?style=for-the-badge)
![Localhost](https://img.shields.io/badge/Server-Localhost-orange?style=for-the-badge)

---

## ✨ Features

* 🚀 Automated Chromium browser rendering
* 🌐 Accepts `HTTP` and `HTTPS` target URLs
* 📄 Captures the final rendered HTML
* 📸 Generates a full-page screenshot for verification
* 🔄 Scrolls the page to trigger lazy-loaded content
* 📁 Automatically creates the output directory
* 🖥️ Starts a local HTTP server on port `8080`
* ⚡ Uses asynchronous Playwright APIs
* 🔍 Useful for local UI testing and authorized website archiving

---

## 🧰 Requirements

Make sure you have:

* **Python 3.10+**
* Internet access for Playwright to load the target website
* A website that you are authorized to snapshot

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Install dependencies

```bash
pip install playwright
```

### 3. Install Playwright Chromium

```bash
playwright install chromium
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

You will be prompted to enter a URL:

```text
=== 100% VISUAL ACCURACY SITE COPIER & LOCAL HOST ===

Enter the full website URL to clone:
```

Example:

```text
https://example.com
```

The tool will then:

1. Launch Chromium in headless mode.
2. Navigate to the supplied website.
3. Wait for network activity to settle.
4. Scroll through the page to trigger lazy-loaded elements.
5. Capture the rendered HTML.
6. Save a full-page screenshot.
7. Start a local web server.

---

## 📁 Output

After execution, the following directory is created:

```text
cloned_exact_site/
├── index.html
└── screenshot.png
```

### `index.html`

Contains the rendered HTML snapshot captured by Playwright.

### `screenshot.png`

A full-page screenshot of the rendered target page that can be used for visual comparison.

---

## 🖥️ Local Hosting

Once the snapshot has been created, the built-in HTTP server starts automatically.

Open:

```text
http://localhost:8080
```

You should see the generated `index.html` served from the local directory.

Stop the server with:

```text
Ctrl+C
```

---

## 🔧 Configuration

The default server port is:

```python
port=8080
```

You can change it in:

```python
start_local_host(port=8080)
```

For example:

```python
start_local_host(port=3000)
```

Then access:

```text
http://localhost:3000
```

---

## 🧠 How It Works

```text
        Target Website
              │
              ▼
       Playwright / Chromium
              │
              ▼
      Render webpage completely
              │
              ▼
       Trigger lazy loading
              │
        ┌─────┴─────┐
        ▼           ▼
    index.html   screenshot.png
        │
        └─────┬─────┘
              ▼
       Local HTTP Server
              │
              ▼
    http://localhost:8080
```

---

## ⚠️ Important Limitations

This project captures the **rendered HTML**, but it is not necessarily a completely self-contained offline copy of a website.

For example, the captured HTML may still reference:

* External CSS
* JavaScript files
* Images
* Fonts
* API endpoints
* CDN resources

Therefore, some websites may not look or behave exactly the same when opened offline or through localhost.

Dynamic functionality that depends on the original server may also stop working.

---

## 🛡️ Responsible Use

Use this tool only on websites and systems that you own or have explicit permission to test, archive, or reproduce.

Do **not** use website snapshots to impersonate legitimate services, collect credentials, deceive users, or conduct unauthorized phishing or credential-harvesting activities.

For security research, use intentionally vulnerable applications or your own test environment.

Recommended targets include:

```text
http://localhost
http://127.0.0.1
Authorized development/staging environments
CTF/lab applications
Your own websites
```

---

## 🧪 Example Test

For a simple local test server:

```bash
python -m http.server 9000
```

Then run this project and provide:

```text
http://localhost:9000
```

The generated snapshot will be placed inside:

```text
cloned_exact_site/
```

---

## 🐛 Troubleshooting

### Playwright is not installed

Run:

```bash
pip install playwright
```

Then:

```bash
playwright install chromium
```

### Port 8080 is already in use

Change:

```python
start_local_host(port=8080)
```

to another port:

```python
start_local_host(port=8081)
```

### Website fails to load

Check that:

* The URL starts with `http://` or `https://`
* Your internet connection is working
* The target website is accessible
* The website does not require authentication
* The page does not depend heavily on server-side functionality

### Some assets are missing

The current implementation saves the HTML snapshot but does not download every external resource locally. Consequently, externally hosted assets may remain dependent on their original URLs.

---

## 📜 License

Use an appropriate open-source license for your repository, such as MIT, if you intend to distribute the project publicly.

---

## ⭐ Project Purpose

This project is intended for:

* 🔬 Web development testing
* 🎨 UI/visual comparison
* 🧪 Authorized security labs
* 📚 Web automation learning
* 🗃️ Authorized website archiving
* 🖥️ Local rendering experiments

**Built for learning, testing, and authorized research.**
