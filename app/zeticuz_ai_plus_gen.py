"""
ZETICUZ AI PLUS GEN — Official Desktop Application
Automated 12-Month Google AI Plus Promotional Provisioner
Engineered by: Sam Pangilinan (ZETICUZ / TECHNOLOHIYA)
Website: https://www.zeticuz.xyz/
Repository: https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app
Version: 1.0.1
"""

import os
import sys
import webbrowser
import customtkinter as ctk

# Ensure app/engine is in python path (both local dev and PyInstaller frozen bundle)
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    CURRENT_DIR = sys._MEIPASS
    ENGINE_DIR = os.path.join(sys._MEIPASS, 'engine')
else:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    ENGINE_DIR = os.path.join(CURRENT_DIR, 'engine')

if ENGINE_DIR not in sys.path:
    sys.path.insert(0, ENGINE_DIR)

import gui
import claimer

# Set CustomTkinter appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APP_NAME = "ZETICUZ AI PLUS GEN"
APP_VERSION = "v1.0.1"
DEV_NAME = "Sam Pangilinan"
DEV_HANDLE = "ZETICUZ"
PORTFOLIO_URL = "https://www.zeticuz.xyz/"
REPO_URL = "https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app"

ZETICUZ_BANNER = """================================================================================
  ZETICUZ AI PLUS GEN — 1-YEAR ACCESS PROVISIONER (v1.0.1)
================================================================================
  Engineered by Sam Pangilinan (ZETICUZ / TECHNOLOHIYA)
  Developer Portfolio: https://www.zeticuz.xyz/
  Repository: https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app
  Status: System Ready · 100% Local Execution

  Quick Guide:
  1. Review or customize your account profile above.
  2. Click "Get 1-Year Access Link" to start provisioning.
  3. Enter the 6-digit verification code sent to your email when prompted.
  4. Your 1-Year Google AI Plus redemption link will be ready to claim!
================================================================================
"""

class ZeticuzAIPlusApp(gui.GeminiClaimerApp):
    def __init__(self):
        super().__init__()
        
        # 1. Update Title and Window properties
        self.title(f"{APP_NAME} — {APP_VERSION} (1-Year Access Portal)")
        
        # App Icon
        icon_path = os.path.join(CURRENT_DIR, "..", "images", "app_icon.ico")
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass

        # 2. Rebrand Header Labels
        # Traverse top frame widgets to customize branding
        try:
            for child in self.winfo_children():
                # Check top header frame
                if isinstance(child, ctk.CTkFrame):
                    for sub in child.winfo_children():
                        if isinstance(sub, ctk.CTkLabel):
                            txt = sub.cget("text")
                            if "Google AI Plus" in txt and "Portal" in txt:
                                sub.configure(text=f"⚡ {APP_NAME} — 1-Year Access Portal", text_color="#38bdf8")
                            elif "Gemini Advanced" in txt:
                                sub.configure(text=f"Automated 12-Month Gemini Advanced & Google AI Plus Utility · By {DEV_NAME} ({DEV_HANDLE})")
        except Exception:
            pass

        # 3. Update Activity Feed Header
        try:
            self.txt_logs.configure(state="normal")
            self.txt_logs.delete("1.0", "end")
            self.txt_logs.insert("1.0", ZETICUZ_BANNER)
            self.txt_logs.configure(state="disabled")
        except Exception:
            pass

        # 4. Wire Support Dev Button to Sam Pangilinan's Portfolio
        if hasattr(self, "btn_support"):
            self.btn_support.configure(
                text="Support Dev ↗",
                command=lambda: webbrowser.open(PORTFOLIO_URL)
            )

        # 5. Populate user test email by default for instant live testing
        if hasattr(self, "entry_email"):
            current_email = self.entry_email.get().strip()
            if not current_email or current_email == "example@gmail.com":
                self.entry_email.delete(0, "end")
                self.entry_email.insert(0, "samxerz73@gmail.com")

    def _show_support_modal(self):
        webbrowser.open(PORTFOLIO_URL)

    def _show_about_modal(self, event=None):
        webbrowser.open(REPO_URL)

if __name__ == "__main__":
    app = ZeticuzAIPlusApp()
    app.mainloop()
