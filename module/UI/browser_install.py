import os
import requests
import platform
import subprocess

def download_browser(url, save_path):
    print(f"Downloading from {url}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Download complete: {save_path}")
    except Exception as e:
        print(f"Error downloading: {e}")

def install_browser(file_path):
    print(f"Starting installation for {file_path}...")
    try:
        if platform.system() == "Windows":
            subprocess.run(file_path, shell=True)
        elif platform.system() == "Linux":
            subprocess.run(["chmod", "+x", file_path])
            subprocess.run(["sudo", file_path])
        elif platform.system() == "Darwin":
            subprocess.run(["open", file_path])
        print("Installation completed!")
    except Exception as e:
        print(f"Error during installation: {e}")

def main():
    browsers = {
        "1": {"name": "Google Chrome", "url": "https://dl.google.com/chrome/install/chrome_installer.exe"},
        "2": {"name": "Mozilla Firefox", "url": "https://download.mozilla.org/?product=firefox-latest&os=win64&lang=en-US"},
        "3": {"name": "Microsoft Edge", "url": "https://go.microsoft.com/fwlink/?linkid=2123438"},
    }

    print("Available browsers for download and installation:")
    for key, browser in browsers.items():
        print(f"{key}. {browser['name']}")

    choice = input("Enter the number of the browser you want to download and install: ")
    if choice in browsers:
        browser_name = browsers[choice]["name"]
        download_url = browsers[choice]["url"]
        save_path = f"{browser_name.replace(' ', '_')}_installer.exe"

        print(f"You selected {browser_name}.")
        download_browser(download_url, save_path)
        install_browser(save_path)
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()
