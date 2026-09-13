import os
import asyncio
from playwright.async_api import async_playwright
from http.server import SimpleHTTPRequestHandler
import socketserver

# Custom handler to serve files from a specific directory
class ClonedSiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Explicitly serve files out of the cloned directory
        super().__init__(*args, directory="cloned_exact_site", **kwargs)

def start_local_host(port=8080):
    """Starts a standard synchronous local HTTP server on the specified port"""
    print(f"\n[Server] Initializing local host on port {port}...")
    
    # Allows the socket to reuse the address immediately after shutdown
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        with socketserver.TCPServer(("", port), ClonedSiteHandler) as httpd:
            print(f"[Server] Active! Open your browser and go to: http://localhost:{port}")
            print("[Server] Press Ctrl+C in the terminal to stop hosting.")
            httpd.serve_forever()
    except Exception as e:
        print(f"[Server] Failed to start server: {e}")

async def clone_exact_site():
    print("=== 100% VISUAL ACCURACY SITE COPIER & LOCAL HOST ===")
    target_url = input("Enter the full website URL to clone (e.g., https://example.com): ").strip()

    if not target_url.startswith(("http://", "https://")):
        print("Error: URL must start with http:// or https://")
        return

    output_folder = "cloned_exact_site"
    os.makedirs(output_folder, exist_ok=True)

    print("\nLaunching automated Chrome browser...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        print(f"Loading {target_url} and waiting for all assets...")
        try:
            await page.goto(target_url, wait_until="networkidle", timeout=60000)
            
            # Scroll down to trigger lazy-loaded assets
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(2000) 
            await page.evaluate("window.scrollTo(0, 0)")
        except Exception as e:
            print(f"Warning during page generation: {e}")

        # Capture the snapshot
        complete_html = await page.content()
        output_path = os.path.join(output_folder, "index.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(complete_html)

        # Capture screenshot verification
        screenshot_path = os.path.join(output_folder, "screenshot.png")
        await page.screenshot(path=screenshot_path, full_page=True)

        await browser.close()
        
    print(f"\n Layout snapshot saved successfully.")
    
    # Hand over execution to the local hosting server
    start_local_host(port=8080)

if __name__ == "__main__":
    asyncio.run(clone_exact_site())
