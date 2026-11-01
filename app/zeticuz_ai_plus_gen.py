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
import math
import random
import webbrowser
import tkinter as tk
from PIL import Image

# Explicit imports to ensure PyInstaller bundles all required backend engines
import greenlet
import playwright
import playwright.sync_api
from playwright.sync_api import sync_playwright
import PIL
import PIL.Image
import PIL.ImageTk
import customtkinter as ctk

# Ensure app/engine is in python path (both local dev and PyInstaller frozen bundle)
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    CURRENT_DIR = sys._MEIPASS
    ENGINE_DIR = os.path.join(sys._MEIPASS, 'engine')
    IMAGES_DIR = os.path.join(sys._MEIPASS, 'images')
else:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    ENGINE_DIR = os.path.join(CURRENT_DIR, 'engine')
    IMAGES_DIR = os.path.join(os.path.dirname(CURRENT_DIR), 'images')

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
DEV_BRAND = "TECHNOLOHIYA"
PORTFOLIO_URL = "https://www.zeticuz.xyz/"
REPO_URL = "https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app"

ZETICUZ_BANNER = """================================================================================
  ZETICUZ AI PLUS GEN — 12-MONTH PROMOTIONAL PROVISIONER (v1.0.1)
================================================================================
  Engineered by: Sam Pangilinan (ZETICUZ / TECHNOLOHIYA)
  Developer Portfolio: https://www.zeticuz.xyz/
  Repository: https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app
  Engine Status: Ready · 100% Client-Side Automation
  
  Quick Execution Guide:
  1. Review or customize your account credentials in the control panel.
  2. Click "Get 1-Year Access Link" to initiate automated gateway verification.
  3. Enter the 6-digit confirmation OTP dispatched to your Gmail.
  4. Your 12-Month Google AI Plus activation link will be delivered directly!
================================================================================
"""

class ZeticuzAIPlusApp(gui.GeminiClaimerApp):
    """
    Bespoke, high-performance UI implementation for ZETICUZ AI PLUS GEN.
    Overhauls the default UI with a modern 3D glossy SaaS design system,
    pulsing status indicators, real-time telemetry HUD, and sleek card layouts.
    """
    def __init__(self):
        # Animation state variables before super().__init__ triggers _build_ui
        self._pulse_tick = 0
        self._is_pulsing = True
        self._status_color = "#38bdf8"
        self._last_step = 1

        super().__init__()

        # 1. Update Window Properties & Icons
        self.title(f"{APP_NAME} — {APP_VERSION} (1-Year Access Portal)")
        self.geometry("960x840")
        self.minsize(880, 720)
        self.configure(fg_color="#070b14")

        # Set taskbar and window icon
        self._apply_branding_icons()

        # 2. Pre-populate user test email
        if hasattr(self, "entry_email"):
            current = self.entry_email.get().strip()
            if not current or current == "example@gmail.com":
                self.entry_email.delete(0, "end")
                self.entry_email.insert(0, "samxerz73@gmail.com")

        # 3. Start Smooth Pulsing Animation Loop
        self._start_pulse_animation()

    def _apply_branding_icons(self):
        """Applies the 3rd image squircle icon to the window taskbar and titlebar."""
        candidates = [
            os.path.join(IMAGES_DIR, "app_icon.ico"),
            os.path.join(CURRENT_DIR, "images", "app_icon.ico"),
            os.path.join(CURRENT_DIR, "..", "images", "app_icon.ico"),
        ]
        for c in candidates:
            if os.path.exists(c):
                try:
                    self.iconbitmap(c)
                    break
                except Exception:
                    pass

        png_candidates = [
            os.path.join(IMAGES_DIR, "zeticuz_app_icon.png"),
            os.path.join(IMAGES_DIR, "app_icon.png"),
            os.path.join(CURRENT_DIR, "images", "zeticuz_app_icon.png"),
            os.path.join(CURRENT_DIR, "..", "images", "zeticuz_app_icon.png"),
        ]
        for pc in png_candidates:
            if os.path.exists(pc):
                try:
                    pimg = Image.open(pc)
                    photo = ctk.CTkImage(light_image=pimg, dark_image=pimg, size=(32, 32))
                    # Tk photoimage for window icon
                    from PIL import ImageTk
                    tk_icon = ImageTk.PhotoImage(pimg.resize((32, 32), Image.Resampling.LANCZOS))
                    self.iconphoto(True, tk_icon)
                    break
                except Exception:
                    pass

    def _build_ui(self):
        """
        Bespoke, high-end 3D glossy UI overhaul.
        Creates all required widget attributes to maintain 100% functional parity.
        """
        # =========================================================================
        # 1. TOP HEADER (Dark glassmorphism navbar with official header logo)
        # =========================================================================
        header_frame = ctk.CTkFrame(
            self,
            fg_color="#0b1120",
            corner_radius=0,
            border_width=1,
            border_color="#1e293b",
            height=76
        )
        header_frame.pack(fill="x", side="top")
        header_frame.pack_propagate(False)

        # Inner container for header content
        header_inner = ctk.CTkFrame(header_frame, fg_color="transparent")
        header_inner.pack(fill="both", expand=True, padx=20, pady=8)

        # Left: Branded Header Logo (2nd uploaded image: 3D red ZE + ZETICUZ)
        logo_loaded = False
        header_logo_paths = [
            os.path.join(IMAGES_DIR, "zeticuz_header_logo.png"),
            os.path.join(CURRENT_DIR, "images", "zeticuz_header_logo.png"),
            os.path.join(CURRENT_DIR, "..", "images", "zeticuz_header_logo.png"),
        ]
        for lp in header_logo_paths:
            if os.path.exists(lp):
                try:
                    pil_logo = Image.open(lp)
                    # 728x200 aspect ratio: render at 200x55
                    self.ctk_header_logo = ctk.CTkImage(
                        light_image=pil_logo,
                        dark_image=pil_logo,
                        size=(200, 55)
                    )
                    logo_lbl = ctk.CTkLabel(header_inner, image=self.ctk_header_logo, text="")
                    logo_lbl.pack(side="left", padx=(0, 14))
                    logo_loaded = True
                    break
                except Exception:
                    pass

        if not logo_loaded:
            # Clean fallback typography badge
            fallback_title = ctk.CTkLabel(
                header_inner,
                text="ZETICUZ",
                font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
                text_color="#f8fafc"
            )
            fallback_title.pack(side="left", padx=(0, 8))

        # Vertical Divider Line
        sep = ctk.CTkFrame(header_inner, width=1, height=36, fg_color="#1e293b")
        sep.pack(side="left", padx=12)

        # Header Titles
        title_box = ctk.CTkFrame(header_inner, fg_color="transparent")
        title_box.pack(side="left", fill="y", pady=4)

        h_tag = ctk.CTkLabel(
            title_box,
            text="⚡ AI PLUS GEN — 12-MONTH ACCESS PROVISIONER",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            text_color="#38bdf8",
            anchor="w"
        )
        h_tag.pack(anchor="w")

        h_sub = ctk.CTkLabel(
            title_box,
            text=f"Automated Client-Side Engine · By {DEV_NAME} ({DEV_HANDLE}) · © 2026",
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color="#64748b",
            anchor="w"
        )
        h_sub.pack(anchor="w")

        # Right Side: Status Beacon Pill & Action Buttons
        right_box = ctk.CTkFrame(header_inner, fg_color="transparent")
        right_box.pack(side="right", fill="y")

        # Pulsing Status Pill
        self.status_pill = ctk.CTkFrame(
            right_box,
            fg_color="#0f172a",
            corner_radius=20,
            border_width=1,
            border_color="#1e293b"
        )
        self.status_pill.pack(side="left", padx=8, pady=4)

        self.beacon_dot = ctk.CTkLabel(
            self.status_pill,
            text="●",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#38bdf8"
        )
        self.beacon_dot.pack(side="left", padx=(10, 4), pady=4)

        self.lbl_status = ctk.CTkLabel(
            self.status_pill,
            text="System Ready · Local Execution",
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            text_color="#38bdf8"
        )
        self.lbl_status.pack(side="left", padx=(0, 12), pady=4)

        # Header Support Dev Button
        self.btn_header_support = ctk.CTkButton(
            right_box,
            text="Support Dev ↗",
            width=110,
            height=32,
            corner_radius=8,
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            fg_color="#1e293b",
            hover_color="#0284c7",
            text_color="#f8fafc",
            command=self._show_support_modal
        )
        self.btn_header_support.pack(side="left", padx=4)

        # Header About Button
        self.btn_header_about = ctk.CTkButton(
            right_box,
            text="About ℹ",
            width=70,
            height=32,
            corner_radius=8,
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            fg_color="#1e293b",
            hover_color="#334155",
            text_color="#94a3b8",
            command=self._show_about_modal
        )
        self.btn_header_about.pack(side="left", padx=(4, 0))

        # =========================================================================
        # 2. SCROLLABLE WORKSPACE
        # =========================================================================
        self.scroll_body = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            scrollbar_button_color="#1e293b",
            scrollbar_button_hover_color="#334155"
        )
        self.scroll_body.pack(fill="both", expand=True, padx=20, pady=16)

        # =========================================================================
        # 3. PIPELINE STEPPER CARD (Progress Tracker)
        # =========================================================================
        self.pipeline_card = ctk.CTkFrame(
            self.scroll_body,
            fg_color="#0c1322",
            corner_radius=12,
            border_width=1,
            border_color="#1e293b"
        )
        self.pipeline_card.pack(fill="x", pady=(0, 14), padx=2)

        pipe_inner = ctk.CTkFrame(self.pipeline_card, fg_color="transparent")
        pipe_inner.pack(fill="x", padx=16, pady=12)

        self.step1_lbl = ctk.CTkLabel(
            pipe_inner,
            text="① Gateway Connection",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#38bdf8"
        )
        self.step1_lbl.pack(side="left")

        self.step1_sep = ctk.CTkLabel(
            pipe_inner,
            text="───────",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#334155"
        )
        self.step1_sep.pack(side="left", expand=True)

        self.step2_lbl = ctk.CTkLabel(
            pipe_inner,
            text="② Email OTP Verification",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#64748b"
        )
        self.step2_lbl.pack(side="left")

        self.step2_sep = ctk.CTkLabel(
            pipe_inner,
            text="───────",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#334155"
        )
        self.step2_sep.pack(side="left", expand=True)

        self.step3_lbl = ctk.CTkLabel(
            pipe_inner,
            text="③ 1-Year Access Dispatched",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#64748b"
        )
        self.step3_lbl.pack(side="left")

        # =========================================================================
        # 4. RESULTS & ACTIVATION CARD (Shown on success)
        # =========================================================================
        self.result_card = ctk.CTkFrame(
            self.scroll_body,
            fg_color="#042f2e",
            corner_radius=14,
            border_width=1,
            border_color="#059669"
        )
        # Pack forget initially; displayed by engine on completion
        self.result_card.pack(fill="x", pady=(0, 14), padx=2)
        self.result_card.pack_forget()

        res_inner = ctk.CTkFrame(self.result_card, fg_color="transparent")
        res_inner.pack(fill="both", expand=True, padx=20, pady=18)

        self.result_title = ctk.CTkLabel(
            res_inner,
            text="🎉 Account Completed! Activation link sent to your email",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color="#34d399",
            anchor="w"
        )
        self.result_title.pack(fill="x", pady=(0, 12))

        # Highlight box for the redemption status / email target
        self.url_frame = ctk.CTkFrame(
            res_inner,
            fg_color="#022c22",
            corner_radius=10,
            border_width=1,
            border_color="#10b981"
        )
        self.url_frame.pack(fill="x", pady=(0, 14))

        self.lbl_result_url = ctk.CTkLabel(
            self.url_frame,
            text="✉ Check your inbox at: your registered email",
            font=ctk.CTkFont(family="Consolas", size=12, weight="bold"),
            text_color="#6ee7b7",
            anchor="w"
        )
        self.lbl_result_url.pack(fill="x", padx=16, pady=12)

        # Action Buttons in Results Card
        res_btns_frame = ctk.CTkFrame(res_inner, fg_color="transparent")
        res_btns_frame.pack(fill="x", pady=(0, 14))

        self.btn_copy_link = ctk.CTkButton(
            res_btns_frame,
            text="📋 Copy Credentials",
            height=36,
            corner_radius=8,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            fg_color="#059669",
            hover_color="#047857",
            text_color="#ffffff",
            command=self._copy_link_to_clipboard
        )
        self.btn_copy_link.pack(side="left", padx=(0, 8))

        self.btn_open_browser = ctk.CTkButton(
            res_btns_frame,
            text="✉ Open Email Inbox",
            height=36,
            corner_radius=8,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            fg_color="#0284c7",
            hover_color="#0369a1",
            text_color="#ffffff",
            command=self._open_in_browser
        )
        self.btn_open_browser.pack(side="left", padx=8)

        self.btn_open_results = ctk.CTkButton(
            res_btns_frame,
            text="📁 Open Results Folder",
            height=36,
            corner_radius=8,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            fg_color="#1e293b",
            hover_color="#334155",
            text_color="#cbd5e1",
            command=self._open_results_folder
        )
        self.btn_open_results.pack(side="left", padx=8)

        self.btn_res_support = ctk.CTkButton(
            res_btns_frame,
            text="☕ Support Dev",
            height=36,
            corner_radius=8,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            fg_color="#f59e0b",
            hover_color="#d97706",
            text_color="#0f172a",
            command=self._show_support_modal
        )
        self.btn_res_support.pack(side="left", padx=8)

        # Guidance Notice Box inside Results Card
        self.notice_box = ctk.CTkFrame(
            res_inner,
            fg_color="#064e3b",
            corner_radius=10,
            border_width=1,
            border_color="#047857"
        )
        self.notice_box.pack(fill="x")

        guide_inner = ctk.CTkFrame(self.notice_box, fg_color="transparent")
        guide_inner.pack(fill="x", padx=14, pady=12)

        lbl_how = ctk.CTkLabel(
            guide_inner,
            text="How to activate your 12-Month Google AI Plus access:",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#a7f3d0",
            anchor="w"
        )
        lbl_how.pack(fill="x", pady=(0, 4))

        self.lbl_activate_desc = ctk.CTkLabel(
            guide_inner,
            text="1. Check your email inbox (and Spam/Promotions folder).\n2. Look for the confirmation email: 'Claim your free access'.\n3. Click the activation button inside to activate your 1-Year Google AI Plus access directly.",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#d1fae5",
            justify="left",
            anchor="w"
        )
        self.lbl_activate_desc.pack(fill="x", pady=(0, 6))

        lbl_imp = ctk.CTkLabel(
            guide_inner,
            text="Important Notice:",
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            text_color="#fbbf24",
            anchor="w"
        )
        lbl_imp.pack(fill="x", pady=(4, 2))

        self.lbl_notice_desc = ctk.CTkLabel(
            guide_inner,
            text="Please verify your email inbox and follow the on-screen steps. Using the link in your email activates your promotional tier instantly.",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#fef3c7",
            justify="left",
            anchor="w"
        )
        self.lbl_notice_desc.pack(fill="x")

        # =========================================================================
        # 5. ACCOUNT PROFILE & SETUP CARD (Control Panel)
        # =========================================================================
        self.config_card = ctk.CTkFrame(
            self.scroll_body,
            fg_color="#0c1322",
            corner_radius=14,
            border_width=1,
            border_color="#1e293b"
        )
        self.config_card.pack(fill="x", pady=(0, 14), padx=2)

        config_inner = ctk.CTkFrame(self.config_card, fg_color="transparent")
        config_inner.pack(fill="both", expand=True, padx=20, pady=18)

        # Card Title Header
        title_row = ctk.CTkFrame(config_inner, fg_color="transparent")
        title_row.pack(fill="x", pady=(0, 14))

        self.card_title = ctk.CTkLabel(
            title_row,
            text="⚡ Account Profile & Automation Setup",
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"),
            text_color="#38bdf8",
            anchor="w"
        )
        self.card_title.pack(side="left")

        self.btn_randomize = ctk.CTkButton(
            title_row,
            text="🎲 Randomize Info",
            width=135,
            height=32,
            corner_radius=8,
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            fg_color="#1e293b",
            hover_color="#334155",
            text_color="#e2e8f0",
            command=self._randomize_credentials
        )
        self.btn_randomize.pack(side="right")

        # Form Grid (2 Columns, sleek input styling)
        form_grid = ctk.CTkFrame(config_inner, fg_color="transparent")
        form_grid.pack(fill="x", pady=(0, 16))
        form_grid.grid_columnconfigure(0, weight=1, uniform="col")
        form_grid.grid_columnconfigure(1, weight=1, uniform="col")

        # Row 0: First Name & Last Name
        # First Name
        fn_box = ctk.CTkFrame(form_grid, fg_color="transparent")
        fn_box.grid(row=0, column=0, sticky="ew", padx=(0, 10), pady=6)
        self.lbl_fname = ctk.CTkLabel(
            fn_box,
            text="First Name:",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#94a3b8",
            anchor="w"
        )
        self.lbl_fname.pack(fill="x", pady=(0, 4))
        self.entry_fname = ctk.CTkEntry(
            fn_box,
            height=38,
            corner_radius=8,
            fg_color="#070b14",
            border_color="#1e293b",
            border_width=1,
            text_color="#f8fafc",
            placeholder_text="First name"
        )
        self.entry_fname.pack(fill="x")
        self.entry_fname.insert(0, random.choice(gui.FIRST_NAMES))

        # Last Name
        ln_box = ctk.CTkFrame(form_grid, fg_color="transparent")
        ln_box.grid(row=0, column=1, sticky="ew", padx=(10, 0), pady=6)
        self.lbl_lname = ctk.CTkLabel(
            ln_box,
            text="Last Name:",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#94a3b8",
            anchor="w"
        )
        self.lbl_lname.pack(fill="x", pady=(0, 4))
        self.entry_lname = ctk.CTkEntry(
            ln_box,
            height=38,
            corner_radius=8,
            fg_color="#070b14",
            border_color="#1e293b",
            border_width=1,
            text_color="#f8fafc",
            placeholder_text="Last name"
        )
        self.entry_lname.pack(fill="x")
        self.entry_lname.insert(0, random.choice(gui.LAST_NAMES))

        # Row 1: Gmail Address & Password
        # Gmail Address
        em_box = ctk.CTkFrame(form_grid, fg_color="transparent")
        em_box.grid(row=1, column=0, sticky="ew", padx=(0, 10), pady=6)
        lbl_em = ctk.CTkLabel(
            em_box,
            text="Gmail Address (@gmail.com):",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#94a3b8",
            anchor="w"
        )
        lbl_em.pack(fill="x", pady=(0, 4))
        self.entry_email = ctk.CTkEntry(
            em_box,
            height=38,
            corner_radius=8,
            fg_color="#070b14",
            border_color="#1e293b",
            border_width=1,
            text_color="#38bdf8",
            placeholder_text="your_email@gmail.com"
        )
        self.entry_email.pack(fill="x")

        # Password
        pw_box = ctk.CTkFrame(form_grid, fg_color="transparent")
        pw_box.grid(row=1, column=1, sticky="ew", padx=(10, 0), pady=6)
        lbl_pw = ctk.CTkLabel(
            pw_box,
            text="Secure Password (Min 6 chars):",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#94a3b8",
            anchor="w"
        )
        lbl_pw.pack(fill="x", pady=(0, 4))
        self.entry_password = ctk.CTkEntry(
            pw_box,
            height=38,
            corner_radius=8,
            fg_color="#070b14",
            border_color="#1e293b",
            border_width=1,
            text_color="#f8fafc",
            placeholder_text="Password"
        )
        self.entry_password.pack(fill="x")
        self.entry_password.insert(0, gui.generate_secure_password())

        # Row 2: Contact Number & Visual Browser Checkbox
        # Contact Number
        ph_box = ctk.CTkFrame(form_grid, fg_color="transparent")
        ph_box.grid(row=2, column=0, sticky="ew", padx=(0, 10), pady=6)
        self.lbl_phone = ctk.CTkLabel(
            ph_box,
            text="Contact (+91):",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#94a3b8",
            anchor="w"
        )
        self.lbl_phone.pack(fill="x", pady=(0, 4))
        self.entry_phone = ctk.CTkEntry(
            ph_box,
            height=38,
            corner_radius=8,
            fg_color="#070b14",
            border_color="#1e293b",
            border_width=1,
            text_color="#f8fafc",
            placeholder_text="10 digit Indian number"
        )
        self.entry_phone.pack(fill="x")
        self.entry_phone.insert(0, gui.generate_random_indian_phone())

        # Checkbox: Visual Browser Option
        chk_box = ctk.CTkFrame(form_grid, fg_color="transparent")
        chk_box.grid(row=2, column=1, sticky="ew", padx=(10, 0), pady=(24, 0))
        self.chk_browser = ctk.CTkCheckBox(
            chk_box,
            text="Show visual automation browser (Recommended)",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#cbd5e1",
            fg_color="#0284c7",
            hover_color="#0369a1",
            corner_radius=6
        )
        self.chk_browser.pack(fill="x")
        self.chk_browser.select()

        # Action Buttons Row (3D glossy appearance)
        btn_bar = ctk.CTkFrame(config_inner, fg_color="transparent")
        btn_bar.pack(fill="x", pady=(10, 4))

        # Start Process Button (3D Glossy Cobalt/Sky)
        self.btn_start = ctk.CTkButton(
            btn_bar,
            text="⚡ Get 1-Year Access Link",
            width=240,
            height=44,
            corner_radius=10,
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            fg_color="#0284c7",
            hover_color="#0369a1",
            text_color="#ffffff",
            command=self._start_process
        )
        self.btn_start.pack(side="left", padx=(0, 10))

        # Stop Process Button
        self.btn_stop = ctk.CTkButton(
            btn_bar,
            text="⏹ Stop Process",
            width=130,
            height=44,
            corner_radius=10,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            fg_color="#334155",
            hover_color="#475569",
            text_color="#cbd5e1",
            command=self._stop_process
        )
        self.btn_stop.pack(side="left", padx=6)

        # Support Dev Button
        self.btn_support = ctk.CTkButton(
            btn_bar,
            text="Support Dev ↗",
            width=140,
            height=44,
            corner_radius=10,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            fg_color="#f59e0b",
            hover_color="#d97706",
            text_color="#0f172a",
            command=self._show_support_modal
        )
        self.btn_support.pack(side="right")

        # =========================================================================
        # 6. LIVE ACTIVITY CONSOLE HUD (Real-Time Terminal Output)
        # =========================================================================
        log_card = ctk.CTkFrame(
            self.scroll_body,
            fg_color="#080d1a",
            corner_radius=12,
            border_width=1,
            border_color="#1e293b"
        )
        log_card.pack(fill="both", expand=True, padx=2, pady=(0, 10))

        log_head = ctk.CTkFrame(log_card, fg_color="#050814", corner_radius=0, height=36)
        log_head.pack(fill="x")
        log_head.pack_propagate(False)

        # Mock macOS window control dots
        dots_box = ctk.CTkFrame(log_head, fg_color="transparent")
        dots_box.pack(side="left", padx=12)

        for col in ["#ef4444", "#f59e0b", "#10b981"]:
            d = ctk.CTkLabel(dots_box, text="●", font=ctk.CTkFont(size=12), text_color=col)
            d.pack(side="left", padx=2)

        log_title = ctk.CTkLabel(
            log_head,
            text="⚡ PIPELINE ACTIVITY & TELEMETRY STREAM",
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            text_color="#94a3b8"
        )
        log_title.pack(side="left", padx=8)

        # Clear Logs Button
        btn_clear = ctk.CTkButton(
            log_head,
            text="Clear",
            width=54,
            height=22,
            corner_radius=4,
            font=ctk.CTkFont(family="Segoe UI", size=10),
            fg_color="#1e293b",
            hover_color="#334155",
            text_color="#94a3b8",
            command=self._clear_logs
        )
        btn_clear.pack(side="right", padx=(4, 12))

        # Copy Logs Button
        btn_copy_logs = ctk.CTkButton(
            log_head,
            text="Copy All",
            width=64,
            height=22,
            corner_radius=4,
            font=ctk.CTkFont(family="Segoe UI", size=10),
            fg_color="#1e293b",
            hover_color="#334155",
            text_color="#94a3b8",
            command=self._copy_all_logs
        )
        btn_copy_logs.pack(side="right", padx=4)

        # Text Console
        self.txt_logs = ctk.CTkTextbox(
            log_card,
            font=ctk.CTkFont(family="Consolas", size=11),
            fg_color="#040711",
            text_color="#38bdf8",
            corner_radius=0,
            border_width=0,
            wrap="word",
            height=180
        )
        self.txt_logs.pack(fill="both", expand=True, padx=6, pady=6)
        self.txt_logs.insert("1.0", ZETICUZ_BANNER)
        self.txt_logs.configure(state="disabled")

        # =========================================================================
        # 7. FOOTER BAR
        # =========================================================================
        footer = ctk.CTkFrame(self, fg_color="#070b14", height=32, corner_radius=0)
        footer.pack(fill="x", side="bottom")

        lbl_foot = ctk.CTkLabel(
            footer,
            text=f"ZETICUZ AI PLUS GEN · Developed by {DEV_NAME} · © 2026",
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color="#475569"
        )
        lbl_foot.pack(side="left", padx=20)

        lbl_port = ctk.CTkLabel(
            footer,
            text="Visit Portfolio ↗",
            font=ctk.CTkFont(family="Segoe UI", size=10, underline=True),
            text_color="#0284c7",
            cursor="hand2"
        )
        lbl_port.pack(side="right", padx=20)
        lbl_port.bind("<Button-1>", lambda e: webbrowser.open(PORTFOLIO_URL))

    def _clear_logs(self):
        """Clears the activity feed."""
        try:
            self.txt_logs.configure(state="normal")
            self.txt_logs.delete("1.0", "end")
            self.txt_logs.configure(state="disabled")
        except Exception:
            pass

    def _copy_all_logs(self):
        """Copies the entire terminal text to clipboard."""
        try:
            content = self.txt_logs.get("1.0", "end")
            self.clipboard_clear()
            self.clipboard_append(content)
            self.update()
            self._set_status("Logs Copied to Clipboard!", "#10b981")
            self.after(2000, lambda: self._set_status("System Ready · Local Execution", "#38bdf8"))
        except Exception:
            pass

    def _start_pulse_animation(self):
        """Oscillates the beacon dot color smoothly to create an organic breathing glow."""
        if not self._is_pulsing:
            return

        self._pulse_tick += 1
        # Sine wave breathing between 0.3 and 1.0
        val = 0.5 + 0.5 * math.sin(self._pulse_tick * 0.12)
        
        # If currently active/running, pulse between cyan and cobalt
        if getattr(self, "active_claimer", None) is not None:
            # Running mode: Fast electric blue pulse
            r = int(2 + (56 - 2) * val)
            g = int(132 + (189 - 132) * val)
            b = int(199 + (248 - 199) * val)
            col = f"#{r:02x}{g:02x}{b:02x}"
            if hasattr(self, "beacon_dot"):
                self.beacon_dot.configure(text_color=col)
        else:
            # Idle ready mode: Soft breathing cyan
            r = int(14 + (56 - 14) * val)
            g = int(165 + (189 - 165) * val)
            b = int(233 + (248 - 233) * val)
            col = f"#{r:02x}{g:02x}{b:02x}"
            if hasattr(self, "beacon_dot"):
                self.beacon_dot.configure(text_color=col)

        self.after(70, self._start_pulse_animation)

    def _show_about_modal(self, event=None):
        """Displays our branded, clean About Modal dialog with zero original author traces."""
        modal = ctk.CTkToplevel(self)
        modal.title(f"About {APP_NAME}")
        modal.geometry("520x460")
        modal.resizable(False, False)
        modal.configure(fg_color="#0b1120")
        modal.transient(self)
        modal.grab_set()

        # Center modal over parent
        try:
            x = self.winfo_x() + (self.winfo_width() // 2) - 260
            y = self.winfo_y() + (self.winfo_height() // 2) - 230
            modal.geometry(f"520x460+{x}+{y}")
        except Exception:
            pass

        card = ctk.CTkFrame(modal, fg_color="#0f172a", corner_radius=14, border_width=1, border_color="#1e293b")
        card.pack(fill="both", expand=True, padx=20, pady=20)

        # Header Badge
        h_lbl = ctk.CTkLabel(
            card,
            text=f"⚡ {APP_NAME}",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#38bdf8"
        )
        h_lbl.pack(pady=(20, 2))

        v_lbl = ctk.CTkLabel(
            card,
            text=f"Version {APP_VERSION} · 12-Month Access Provisioner",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#94a3b8"
        )
        v_lbl.pack(pady=(0, 16))

        # Description
        desc_txt = (
            "ZETICUZ AI PLUS GEN is a specialized client-side automation utility designed "
            "to streamline partner promotional registration and provision official 12-Month "
            "Google AI Plus & Gemini Advanced access links.\n\n"
            "Key Principles:\n"
            "• 100% Local & Client-Side: Runs securely on your machine with clean browser contexts.\n"
            "• Direct Redemption: Activation tokens are dispatched directly to your Gmail inbox.\n"
            "• Zero Telemetry: Credentials are never collected or transmitted externally."
        )
        desc_lbl = ctk.CTkLabel(
            card,
            text=desc_txt,
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#cbd5e1",
            justify="left",
            wraplength=440
        )
        desc_lbl.pack(padx=20, pady=(0, 20))

        # Developer Signature Frame
        dev_frame = ctk.CTkFrame(card, fg_color="#070b14", corner_radius=8, border_width=1, border_color="#1e293b")
        dev_frame.pack(fill="x", padx=20, pady=(0, 16))

        dev_lbl = ctk.CTkLabel(
            dev_frame,
            text=f"Engineered by: {DEV_NAME} ({DEV_HANDLE} / {DEV_BRAND})\nDeveloper Portfolio: {PORTFOLIO_URL}",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#38bdf8",
            justify="center"
        )
        dev_lbl.pack(pady=10)

        # Buttons
        b_box = ctk.CTkFrame(card, fg_color="transparent")
        b_box.pack(fill="x", padx=20)

        btn_port = ctk.CTkButton(
            b_box,
            text="Visit Portfolio ↗",
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            fg_color="#0284c7",
            hover_color="#0369a1",
            command=lambda: webbrowser.open(PORTFOLIO_URL)
        )
        btn_port.pack(side="left", expand=True, padx=4)

        btn_close = ctk.CTkButton(
            b_box,
            text="Close",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            fg_color="#1e293b",
            hover_color="#334155",
            command=modal.destroy
        )
        btn_close.pack(side="right", expand=True, padx=4)

    def _show_support_modal(self):
        """Displays our branded Support Dev Modal pointing to Sam Pangilinan's portfolio."""
        modal = ctk.CTkToplevel(self)
        modal.title(f"Support Dev — {DEV_NAME}")
        modal.geometry("480x380")
        modal.resizable(False, False)
        modal.configure(fg_color="#0b1120")
        modal.transient(self)
        modal.grab_set()

        try:
            x = self.winfo_x() + (self.winfo_width() // 2) - 240
            y = self.winfo_y() + (self.winfo_height() // 2) - 190
            modal.geometry(f"480x380+{x}+{y}")
        except Exception:
            pass

        card = ctk.CTkFrame(modal, fg_color="#0f172a", corner_radius=14, border_width=1, border_color="#1e293b")
        card.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            card,
            text="☕ Support the Developer",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#f59e0b"
        ).pack(pady=(20, 4))

        ctk.CTkLabel(
            card,
            text=f"Engineered with care by {DEV_NAME} ({DEV_HANDLE})",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#94a3b8"
        ).pack(pady=(0, 16))

        info_txt = (
            "Saved you time and unlocked 12 months of Gemini Advanced?\n\n"
            "If you found this software valuable, you can support further development, "
            "security audits, and future updates by visiting my official developer hub."
        )
        ctk.CTkLabel(
            card,
            text=info_txt,
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#cbd5e1",
            justify="center",
            wraplength=400
        ).pack(padx=20, pady=(0, 20))

        btn_open = ctk.CTkButton(
            card,
            text=f"Open {PORTFOLIO_URL} ↗",
            height=40,
            corner_radius=8,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            fg_color="#f59e0b",
            hover_color="#d97706",
            text_color="#0f172a",
            command=lambda: webbrowser.open(PORTFOLIO_URL)
        )
        btn_open.pack(fill="x", padx=30, pady=(0, 10))

        btn_dismiss = ctk.CTkButton(
            card,
            text="Dismiss",
            height=34,
            corner_radius=8,
            font=ctk.CTkFont(family="Segoe UI", size=11),
            fg_color="#1e293b",
            hover_color="#334155",
            text_color="#94a3b8",
            command=modal.destroy
        )
        btn_dismiss.pack(fill="x", padx=30)

if __name__ == "__main__":
    app = ZeticuzAIPlusApp()
    app.mainloop()
