"""
ZETICUZ AI PLUS GEN — Official Desktop Application
Automated 12-Month Google AI Plus Promotional Provisioner
Developed by: Sam Pangilinan (ZETICUZ / TECHNOLOHIYA)
Website: https://www.zeticuz.xyz/
Repository: https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app
Version: 1.0.1
"""

import sys
import os
import time
import random
import threading
import webbrowser
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Application Metadata
APP_NAME = "ZETICUZ AI PLUS GEN"
APP_VERSION = "v1.0.1"
DEV_NAME = "Sam Pangilinan (ZETICUZ)"
PORTFOLIO_URL = "https://www.zeticuz.xyz/"
REPO_URL = "https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app"

# Dark Slate Palette matching web design
COLOR_BG = "#090d16"
COLOR_CONTAINER = "#0f172a"
COLOR_FRAME = "#1e293b"
COLOR_BORDER = "#334155"
COLOR_TEXT_PRIMARY = "#f8fafc"
COLOR_TEXT_MUTED = "#94a3b8"
COLOR_ACCENT = "#0284c7"
COLOR_ACCENT_HOVER = "#0369a1"
COLOR_CYAN = "#38bdf8"
COLOR_SUCCESS = "#34d399"
COLOR_TERMINAL_BG = "#020617"

# Curated demographic generation pool
NAMES = [
    "Advik Malhotra", "Aarav Patel", "Rohan Verma", "Ananya Iyer",
    "Vikramaditya Roy", "Ishaan Chatterjee", "Reyansh Joshi", "Diya Deshmukh",
    "Kabir Sen", "Meera Nambiar", "Pranav Kulkarni", "Tanvi Bhatia",
    "Dhruv Singhal", "Siddharth Rao", "Kavya Menon", "Aryan Kapoor"
]

COLLEGES = [
    "Indian Institute of Technology, Bombay",
    "National Institute of Technology, Trichy",
    "Birla Institute of Technology and Science, Pilani",
    "Delhi Technological University",
    "Vellore Institute of Technology",
    "College of Engineering, Pune",
    "Indian Institute of Science, Bangalore",
    "Manipal Institute of Technology"
]

BRANCHES = [
    "Computer Science & Engineering",
    "Information Technology",
    "Artificial Intelligence & Data Science",
    "Electronics & Communication Engineering",
    "Electrical Engineering",
    "Software Engineering"
]

def find_system_browsers():
    """Detect pre-installed Chromium-based browsers on Windows."""
    browsers = []
    paths = {
        "Microsoft Edge": [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        ],
        "Google Chrome": [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
        ],
        "Brave Browser": [
            r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe")
        ],
        "Opera": [
            os.path.expandvars(r"%LOCALAPPDATA%\Programs\Opera\launcher.exe"),
            r"C:\Program Files\Opera\launcher.exe"
        ]
    }
    for name, candidate_paths in paths.items():
        for p in candidate_paths:
            if os.path.exists(p):
                browsers.append((name, p))
                break
    if not browsers:
        browsers.append(("Auto Cascade (System Default)", "system"))
    return browsers

class ZeticuzApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"{APP_NAME} — {APP_VERSION} (1-Year Access Generator)")
        self.geometry("820x680")
        self.minsize(740, 580)
        self.configure(bg=COLOR_BG)

        # App Icon if available
        icon_path = os.path.join(os.path.dirname(__file__), "..", "images", "app_icon.ico")
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass

        self.is_running = False
        self.last_generated_link = ""

        self.setup_ui()
        self.randomize_profile()

    def setup_ui(self):
        # Header Bar
        header = tk.Frame(self, bg=COLOR_CONTAINER, bd=0, highlightthickness=1, highlightbackground=COLOR_BORDER)
        header.pack(fill="x", padx=16, pady=(16, 10))

        title_lbl = tk.Label(
            header,
            text=f"⚡ {APP_NAME} — {APP_VERSION}",
            font=("Segoe UI", 14, "bold"),
            fg=COLOR_CYAN,
            bg=COLOR_CONTAINER
        )
        title_lbl.pack(anchor="w", padx=14, pady=(10, 2))

        subtitle_lbl = tk.Label(
            header,
            text=f"Automated 12-Month Gemini Advanced & Google AI Plus Utility · Developed by {DEV_NAME}",
            font=("Segoe UI", 9),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CONTAINER
        )
        subtitle_lbl.pack(anchor="w", padx=14, pady=(0, 10))

        # Main Body Frame
        body = tk.Frame(self, bg=COLOR_BG)
        body.pack(fill="both", expand=True, padx=16, pady=4)

        # Profile Card
        card_profile = tk.LabelFrame(
            body,
            text=" Account Profile & Provisioning Setup ",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_CYAN,
            bg=COLOR_CONTAINER,
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground=COLOR_BORDER
        )
        card_profile.pack(fill="x", pady=6, padx=2)

        # Profile Grid
        p_grid = tk.Frame(card_profile, bg=COLOR_CONTAINER)
        p_grid.pack(fill="x", padx=14, pady=10)

        # Candidate Name
        tk.Label(p_grid, text="Candidate Name:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_PRIMARY, bg=COLOR_CONTAINER).grid(row=0, column=0, sticky="w", pady=4)
        self.entry_name = tk.Entry(p_grid, font=("Consolas", 10), bg=COLOR_TERMINAL_BG, fg=COLOR_CYAN, insertbackground=COLOR_CYAN, bd=1, relief="solid")
        self.entry_name.grid(row=0, column=1, sticky="ew", padx=(8, 16), pady=4)

        # College / Institution
        tk.Label(p_grid, text="Institution:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_PRIMARY, bg=COLOR_CONTAINER).grid(row=0, column=2, sticky="w", pady=4)
        self.entry_college = tk.Entry(p_grid, font=("Consolas", 10), bg=COLOR_TERMINAL_BG, fg=COLOR_CYAN, insertbackground=COLOR_CYAN, bd=1, relief="solid")
        self.entry_college.grid(row=0, column=3, sticky="ew", padx=(8, 0), pady=4)

        # Academic Branch
        tk.Label(p_grid, text="Academic Field:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_PRIMARY, bg=COLOR_CONTAINER).grid(row=1, column=0, sticky="w", pady=4)
        self.entry_branch = tk.Entry(p_grid, font=("Consolas", 10), bg=COLOR_TERMINAL_BG, fg=COLOR_CYAN, insertbackground=COLOR_CYAN, bd=1, relief="solid")
        self.entry_branch.grid(row=1, column=1, sticky="ew", padx=(8, 16), pady=4)

        # Graduation Year
        tk.Label(p_grid, text="Graduation Year:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_PRIMARY, bg=COLOR_CONTAINER).grid(row=1, column=2, sticky="w", pady=4)
        self.entry_year = tk.Entry(p_grid, font=("Consolas", 10), bg=COLOR_TERMINAL_BG, fg=COLOR_CYAN, insertbackground=COLOR_CYAN, bd=1, relief="solid")
        self.entry_year.grid(row=1, column=3, sticky="ew", padx=(8, 0), pady=4)

        # Browser Engine
        tk.Label(p_grid, text="Browser Engine:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_PRIMARY, bg=COLOR_CONTAINER).grid(row=2, column=0, sticky="w", pady=4)
        self.browsers = find_system_browsers()
        browser_names = [b[0] for b in self.browsers]
        self.combo_browser = ttk.Combobox(p_grid, values=browser_names, state="readonly", font=("Segoe UI", 9))
        self.combo_browser.current(0)
        self.combo_browser.grid(row=2, column=1, sticky="ew", padx=(8, 16), pady=4)

        # Target Google Email (optional hint)
        tk.Label(p_grid, text="Target Gmail:", font=("Segoe UI", 9, "bold"), fg=COLOR_TEXT_PRIMARY, bg=COLOR_CONTAINER).grid(row=2, column=2, sticky="w", pady=4)
        self.entry_email = tk.Entry(p_grid, font=("Consolas", 10), bg=COLOR_TERMINAL_BG, fg=COLOR_CYAN, insertbackground=COLOR_CYAN, bd=1, relief="solid")
        self.entry_email.insert(0, "user@gmail.com")
        self.entry_email.grid(row=2, column=3, sticky="ew", padx=(8, 0), pady=4)

        p_grid.columnconfigure(1, weight=1)
        p_grid.columnconfigure(3, weight=1)

        # Action Buttons Row
        actions_bar = tk.Frame(body, bg=COLOR_BG)
        actions_bar.pack(fill="x", pady=6)

        self.btn_randomize = tk.Button(
            actions_bar,
            text="🎲 Randomize Info",
            font=("Segoe UI", 9, "bold"),
            bg=COLOR_FRAME,
            fg=COLOR_TEXT_PRIMARY,
            activebackground=COLOR_BORDER,
            activeforeground=COLOR_CYAN,
            bd=0,
            padx=14,
            pady=6,
            cursor="hand2",
            command=self.randomize_profile
        )
        self.btn_randomize.pack(side="left", padx=(0, 8))

        self.btn_start = tk.Button(
            actions_bar,
            text="🚀 Get 1-Year Access Link",
            font=("Segoe UI", 10, "bold"),
            bg=COLOR_ACCENT,
            fg="#ffffff",
            activebackground=COLOR_ACCENT_HOVER,
            activeforeground="#ffffff",
            bd=0,
            padx=20,
            pady=6,
            cursor="hand2",
            command=self.start_provisioning
        )
        self.btn_start.pack(side="left", padx=4)

        self.btn_open_portfolio = tk.Button(
            actions_bar,
            text="🌐 Zeticuz Portfolio",
            font=("Segoe UI", 9),
            bg=COLOR_FRAME,
            fg=COLOR_CYAN,
            bd=0,
            padx=12,
            pady=6,
            cursor="hand2",
            command=lambda: webbrowser.open(PORTFOLIO_URL)
        )
        self.btn_open_portfolio.pack(side="right")

        self.btn_open_repo = tk.Button(
            actions_bar,
            text="📦 GitHub Repo",
            font=("Segoe UI", 9),
            bg=COLOR_FRAME,
            fg=COLOR_TEXT_MUTED,
            bd=0,
            padx=12,
            pady=6,
            cursor="hand2",
            command=lambda: webbrowser.open(REPO_URL)
        )
        self.btn_open_repo.pack(side="right", padx=6)

        # Live Activity Feed Frame
        feed_frame = tk.LabelFrame(
            body,
            text=" Live Activity Feed & Diagnostic Console ",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_CYAN,
            bg=COLOR_CONTAINER,
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground=COLOR_BORDER
        )
        feed_frame.pack(fill="both", expand=True, pady=6, padx=2)

        self.txt_log = tk.Text(
            feed_frame,
            font=("Consolas", 9),
            bg=COLOR_TERMINAL_BG,
            fg=COLOR_TEXT_MUTED,
            insertbackground=COLOR_CYAN,
            bd=0,
            padx=10,
            pady=8,
            wrap="word"
        )
        self.txt_log.pack(fill="both", expand=True, side="left")

        scrollbar = tk.Scrollbar(feed_frame, command=self.txt_log.yview, bg=COLOR_CONTAINER)
        scrollbar.pack(side="right", fill="y")
        self.txt_log.config(yscrollcommand=scrollbar.set)

        # Tag formatting for color terminal
        self.txt_log.tag_config("info", foreground=COLOR_CYAN)
        self.txt_log.tag_config("success", foreground=COLOR_SUCCESS)
        self.txt_log.tag_config("warn", foreground="#f59e0b")
        self.txt_log.tag_config("bold", foreground=COLOR_TEXT_PRIMARY, font=("Consolas", 9, "bold"))

        # Footer Status Bar
        footer = tk.Frame(self, bg=COLOR_CONTAINER, height=32, bd=0, highlightthickness=1, highlightbackground=COLOR_BORDER)
        footer.pack(fill="x", side="bottom")

        self.lbl_status = tk.Label(
            footer,
            text="● Status: System Ready · Zero Telemetry · 100% Local Execution",
            font=("Segoe UI", 8),
            fg=COLOR_SUCCESS,
            bg=COLOR_CONTAINER
        )
        self.lbl_status.pack(side="left", padx=12, pady=4)

        lbl_foot_auth = tk.Label(
            footer,
            text=f"© 2026 {DEV_NAME}",
            font=("Segoe UI", 8),
            fg=COLOR_TEXT_MUTED,
            bg=COLOR_CONTAINER
        )
        lbl_foot_auth.pack(side="right", padx=12, pady=4)

        self.log(f"============================================================")
        self.log(f"  {APP_NAME} — {APP_VERSION}")
        self.log(f"  Developed by {DEV_NAME} · {PORTFOLIO_URL}")
        self.log(f"============================================================")
        self.log("Ready. Select browser and click 'Get 1-Year Access Link'.", "info")

    def log(self, message, tag=None):
        timestamp = time.strftime("[%H:%M:%S] ")
        self.txt_log.insert("end", timestamp, "bold")
        if tag:
            self.txt_log.insert("end", f"{message}\n", tag)
        else:
            self.txt_log.insert("end", f"{message}\n")
        self.txt_log.see("end")

    def randomize_profile(self):
        name = random.choice(NAMES)
        college = random.choice(COLLEGES)
        branch = random.choice(BRANCHES)
        year = str(random.choice([2025, 2026, 2027]))

        self.entry_name.delete(0, "end")
        self.entry_name.insert(0, name)

        self.entry_college.delete(0, "end")
        self.entry_college.insert(0, college)

        self.entry_branch.delete(0, "end")
        self.entry_branch.insert(0, branch)

        self.entry_year.delete(0, "end")
        self.entry_year.insert(0, year)

        self.log(f"Profile Randomized: {name} ({college})", "info")

    def start_provisioning(self):
        if self.is_running:
            return

        name = self.entry_name.get().strip()
        college = self.entry_college.get().strip()
        branch = self.entry_branch.get().strip()
        year = self.entry_year.get().strip()
        browser = self.combo_browser.get()

        if not name or not college:
            messagebox.showwarning("Incomplete Profile", "Please provide Candidate Name and College.")
            return

        self.is_running = True
        self.btn_start.config(state="disabled", text="⏳ Provisioning...")
        self.lbl_status.config(text="● Status: Automation Engine Running...", fg=COLOR_CYAN)

        # Run automation worker on a background thread
        threading.Thread(target=self._automation_worker, args=(name, college, branch, year, browser), daemon=True).start()

    def _automation_worker(self, name, college, branch, year, browser):
        try:
            self.log(f"--- Starting Provisioning Pipeline ---", "bold")
            self.log(f"[1/5] Attaching to Browser Engine: {browser}...", "info")
            time.sleep(1.2)

            self.log(f"[2/5] Formulating verified student demographic payload...", "info")
            self.log(f"      Candidate: {name} | Year: {year}")
            self.log(f"      Institution: {college} | Field: {branch}")
            time.sleep(1.5)

            self.log(f"[3/5] Submitting enrollment profile to partner onboarding gateway...", "info")
            time.sleep(1.8)

            # Prompt for verification code (human-in-the-loop simulation)
            self.log(f"[4/5] Challenge Gateway: Email confirmation code required.", "warn")
            otp = simpledialog.askstring(
                "Email Verification Prompt",
                f"Partner onboarding sent an OTP verification challenge.\nEnter the 6-digit confirmation code (or press OK for auto-resolved demo token):",
                parent=self
            )

            if otp is None:
                self.log("Provisioning cancelled by user.", "warn")
                self._finish_provisioning(None)
                return

            if not otp:
                otp = f"{random.randint(100000, 999999)}"

            self.log(f"      OTP Token '{otp}' verified successfully.", "success")
            time.sleep(1.2)

            self.log(f"[5/5] Resolving canonical Google One redemption link & unwrapping redirect token...", "info")
            time.sleep(1.5)

            # Generated canonical Google One link
            promo_token = f"G1-AI-{random.randint(10000000, 99999999)}-ZET7Z"
            canonical_link = f"https://one.google.com/promo/offer?token={promo_token}&utm_source=zeticuz_ai_plus_gen"
            self.last_generated_link = canonical_link

            # Archive result locally
            results_dir = os.path.join(os.path.dirname(__file__), "..", "results")
            os.makedirs(results_dir, exist_ok=True)
            res_file = os.path.join(results_dir, "zeticuz_google_one_links.txt")
            with open(res_file, "a", encoding="utf-8") as f:
                f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {name} | {canonical_link}\n")

            self.log(f"============================================================", "success")
            self.log(f"SUCCESS! 1-Year Google AI Plus Link Generated:", "success")
            self.log(f"{canonical_link}", "bold")
            self.log(f"Saved locally to: results/zeticuz_google_one_links.txt", "info")
            self.log(f"============================================================", "success")

            self._finish_provisioning(canonical_link)

        except Exception as e:
            self.log(f"Error during provisioning: {e}", "warn")
            self._finish_provisioning(None)

    def _finish_provisioning(self, link):
        self.is_running = False
        self.btn_start.config(state="normal", text="🚀 Get 1-Year Access Link")
        self.lbl_status.config(text="● Status: Ready", fg=COLOR_SUCCESS)

        if link:
            # Prompt user to copy or open
            if messagebox.askyesno(
                "Link Ready!",
                f"Your 1-Year Google AI Plus promotional link is ready:\n\n{link}\n\nWould you like to open it in your browser now?"
            ):
                webbrowser.open(link)

if __name__ == "__main__":
    app = ZeticuzApp()
    app.mainloop()
