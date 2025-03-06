import os
import sys
import json
import base64
import shutil
import sqlite3
import win32crypt
import html
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QProgressBar, QMessageBox, QTableWidget,
    QTableWidgetItem, QHeaderView, QDialog
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal

class ResultViewer(QDialog):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("Scan Results")
        self.setGeometry(200, 200, 1200, 600)
        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Browser", "Website", "URL", "Username", "Password"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        for row in data:
            self.add_table_row(row)
        
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.table.setSortingEnabled(True)

    def add_table_row(self, row):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        website_name = self.extract_website_name(row["url"])
        
        self.table.setItem(row_position, 0, QTableWidgetItem(row["browser"]))
        self.table.setItem(row_position, 1, QTableWidgetItem(website_name))
        self.table.setItem(row_position, 2, QTableWidgetItem(row["url"]))
        self.table.setItem(row_position, 3, QTableWidgetItem(row["username"]))
        self.table.setItem(row_position, 4, QTableWidgetItem(row["password"]))

    def extract_website_name(self, url):
        try:
            domain = url.split('//')[-1].split('/')[0]
            parts = domain.split('.')
            if len(parts) > 2 and parts[0] in ['www', 'mail', 'web']:
                return parts[1].capitalize()
            return parts[-2].capitalize()
        except:
            return "Unknown"

class DecryptionThread(QThread):
    update_progress = pyqtSignal(int, str)
    finished = pyqtSignal(list)
    error_occurred = pyqtSignal(str)

    def __init__(self, deep_scan=False):
        super().__init__()
        self.deep_scan = deep_scan
        self.all_data = []
        self.browser_paths = {
            "Google Chrome": "Local\\Google\\Chrome\\User Data",
            "Microsoft Edge": "Local\\Microsoft\\Edge\\User Data",
            "Brave": "Local\\BraveSoftware\\Brave-Browser\\User Data",
            "Opera": "Roaming\\Opera Software\\Opera Stable",
            "Vivaldi": "Local\\Vivaldi\\User Data",
            "Chromium": "Local\\Chromium\\User Data",
            "Firefox": "Roaming\\Mozilla\\Firefox\\Profiles"
        }

    def run(self):
        try:
            user_profile = os.environ["USERPROFILE"]
            self.update_progress.emit(5, "Initializing scanner...")
            
            # Process Chromium-based browsers
            self.process_chrome_browsers(user_profile)
            
            # Process Firefox
            self.process_firefox(user_profile)
            
            self.update_progress.emit(100, "Scan complete!")
            self.finished.emit(self.all_data)
        except Exception as e:
            self.error_occurred.emit(f"Critical error: {str(e)}")

    def process_chrome_browsers(self, user_profile):
        browsers = [b for b in self.browser_paths if b != "Firefox"]
        total = len(browsers)
        
        for idx, browser in enumerate(browsers):
            try:
                self.update_progress.emit(10 + int(60*(idx/total)), f"Scanning {browser}...")
                path = os.path.join(user_profile, "AppData", self.browser_paths[browser])
                
                if not os.path.exists(path):
                    continue
                
                profiles = self.get_chrome_profiles(path)
                key = self.get_chrome_key(path)
                
                for profile in profiles:
                    self.process_chrome_profile(browser, path, profile, key)
            except Exception as e:
                self.error_occurred.emit(f"{browser} error: {str(e)}")

    def get_chrome_profiles(self, path):
        profiles = ["Default"]
        if self.deep_scan:
            profiles += [d for d in os.listdir(path) 
                        if d.startswith("Profile") and os.path.isdir(os.path.join(path, d))]
        return profiles

    def get_chrome_key(self, path):
        local_state = os.path.join(path, "Local State")
        if not os.path.exists(local_state):
            raise FileNotFoundError("Chrome key file missing")
        
        with open(local_state, "r", encoding="utf-8") as f:
            encrypted_key = json.load(f)["os_crypt"]["encrypted_key"]
        
        encrypted_key = base64.b64decode(encrypted_key)[5:]
        return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

    def process_chrome_profile(self, browser, path, profile, key):
        login_db = os.path.join(path, profile, "Login Data")
        if not os.path.exists(login_db):
            return
        
        temp_dir = os.path.join(os.getcwd(), "Temp", browser.replace(" ", "_"))
        os.makedirs(temp_dir, exist_ok=True)
        
        try:
            temp_file = os.path.join(temp_dir, "temp_db")
            shutil.copy2(login_db, temp_file)
            
            conn = sqlite3.connect(temp_file)
            cursor = conn.cursor()
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
            
            for url, user, pwd in cursor.fetchall():
                try:
                    password = self.decrypt_chrome(pwd, key)
                    self.all_data.append({
                        "browser": browser,
                        "url": url,
                        "username": user,
                        "password": password
                    })
                except:
                    continue
        finally:
            conn.close()
            shutil.rmtree(temp_dir, ignore_errors=True)

    def decrypt_chrome(self, data, key):
        try:
            iv = data[3:15]
            encrypted = data[15:-16]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(encrypted).decode()
        except:
            return "Decryption Failed"

    def process_firefox(self, user_profile):
        try:
            self.update_progress.emit(80, "Scanning Firefox...")
            firefox_path = os.path.join(user_profile, "AppData", self.browser_paths["Firefox"])
            
            if not os.path.exists(firefox_path):
                return
            
            profiles = [d for d in os.listdir(firefox_path) 
                       if os.path.isdir(os.path.join(firefox_path, d))]
            
            for profile in profiles:
                self.process_firefox_profile(firefox_path, profile)
        except Exception as e:
            self.error_occurred.emit(f"Firefox error: {str(e)}")

    def process_firefox_profile(self, firefox_path, profile):
        profile_path = os.path.join(firefox_path, profile)
        key_db = os.path.join(profile_path, "key4.db")
        logins_json = os.path.join(profile_path, "logins.json")
        
        if not all(os.path.exists(f) for f in [key_db, logins_json]):
            return
        
        try:
            with open(logins_json, "r", encoding="utf-8") as f:
                logins = json.load(f).get("logins", [])
            
            key = self.get_firefox_key(profile_path)
            for login in logins:
                try:
                    user = self.decrypt_firefox(login["encryptedUsername"], key)
                    pwd = self.decrypt_firefox(login["encryptedPassword"], key)
                    
                    self.all_data.append({
                        "browser": "Firefox",
                        "url": login.get("hostname", ""),
                        "username": user,
                        "password": pwd
                    })
                except:
                    continue
        except:
            pass

    def get_firefox_key(self, profile_path):
        conn = sqlite3.connect(os.path.join(profile_path, "key4.db"))
        cursor = conn.cursor()
        cursor.execute("SELECT item1, item2 FROM metadata WHERE id = 'password';")
        row = cursor.fetchone()
        
        global_salt = base64.b64decode(row[0])
        item2 = base64.b64decode(row[1])
        entry_salt = item2[1:1 + item2[0]]
        ciphertext = item2[1 + item2[0]:]
        
        key = PBKDF2(
            password=global_salt,
            salt=entry_salt,
            dkLen=32,
            count=1,
            hmac_hash_module=None
        )
        return key

    def decrypt_firefox(self, data, key):
        encrypted = base64.b64decode(data)
        iv = encrypted[1:17]
        ciphertext = encrypted[17:]
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)
        return html.unescape(decrypted[:-decrypted[-1]].decode())

class PasswordExtractorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Browser Password Scanner")
        self.setGeometry(100, 100, 400, 200)
        self.init_ui()
        self.scanning = False

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Scan Buttons
        self.scan_btn = QPushButton("Quick Scan (Default Profiles)")
        self.scan_btn.clicked.connect(lambda: self.start_scan(False))
        
        self.deep_scan_btn = QPushButton("Deep Scan (All Profiles)")
        self.deep_scan_btn.clicked.connect(lambda: self.start_scan(True))
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.scan_btn)
        button_layout.addWidget(self.deep_scan_btn)
        layout.addLayout(button_layout)

        # Progress
        self.progress = QProgressBar()
        self.status = QLabel("Ready")
        layout.addWidget(self.progress)
        layout.addWidget(self.status)

    def start_scan(self, deep_scan):
        if self.scanning:
            return

        self.scanning = True
        self.thread = DecryptionThread(deep_scan)
        self.thread.update_progress.connect(self.update_progress)
        self.thread.finished.connect(self.show_results)
        self.thread.error_occurred.connect(self.show_error)
        self.thread.start()

        for btn in [self.scan_btn, self.deep_scan_btn]:
            btn.setEnabled(False)

    def update_progress(self, value, message):
        self.progress.setValue(value)
        self.status.setText(message)

    def show_results(self, data):
        self.scanning = False
        self.progress.setValue(0)
        self.status.setText("Scan completed")
        
        for btn in [self.scan_btn, self.deep_scan_btn]:
            btn.setEnabled(True)
        
        if not data:
            QMessageBox.information(self, "No Data", "No passwords found during scan.")
            return
        
        self.result_viewer = ResultViewer(data)
        self.result_viewer.exec()

    def show_error(self, message):
        self.scanning = False
        self.progress.setValue(0)
        self.status.setText("Error occurred")
        
        for btn in [self.scan_btn, self.deep_scan_btn]:
            btn.setEnabled(True)
        
        QMessageBox.critical(self, "Error", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordExtractorApp()
    window.show()
    sys.exit(app.exec())
