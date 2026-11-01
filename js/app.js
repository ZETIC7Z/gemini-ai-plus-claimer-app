/**
 * ZETICUZ AI PLUS GEN — Interactive Web Portal Script
 * Single Source of Truth for release configuration, DOM synchronization,
 * mobile drawer navigation, interactive 3D UI simulation, and accessibility.
 * Developed by: Sam Pangilinan (ZETICUZ / TECHNOLOHIYA)
 * Portfolio: https://www.zeticuz.xyz/
 */

// Centralized Release Configuration
const CONFIG = {
	APP_NAME: "ZETICUZ AI PLUS GEN",
	VERSION: "v1.0.1",
	REPO_URL: "https://github.com/ZETIC7Z/gemini-ai-plus-claimer-app",
	DEV_NAME: "Sam Pangilinan",
	DEV_HANDLE: "ZETICUZ",
	PORTFOLIO_URL: "https://www.zeticuz.xyz/",
	get DIRECT_DOWNLOAD_URL() {
		return `${this.REPO_URL}/releases/tag/${this.VERSION}`;
	},
	get RELEASES_URL() {
		return `${this.REPO_URL}/releases`;
	},
	get LATEST_RELEASE_URL() {
		return `${this.REPO_URL}/releases/latest`;
	},
};

// Wire all direct release download buttons
document.querySelectorAll(".direct-download-link").forEach((link) => {
	if (CONFIG.DIRECT_DOWNLOAD_URL) {
		link.href = CONFIG.DIRECT_DOWNLOAD_URL;
	}
});

// Wire releases hub links
document.querySelectorAll(".releases-link").forEach((link) => {
	if (CONFIG.RELEASES_URL) {
		link.href = CONFIG.RELEASES_URL;
	}
});

// Synchronize all version text elements across the page
document.querySelectorAll(".app-version-text").forEach((element) => {
	element.textContent = CONFIG.VERSION;
});

// Synchronize developer links
document.querySelectorAll(".dev-portfolio-link").forEach((link) => {
	link.href = CONFIG.PORTFOLIO_URL;
});

// Update Schema.org JSON-LD Structured Data if present
const schemaScript = document.getElementById("app-schema");
if (schemaScript) {
	try {
		const schema = JSON.parse(schemaScript.textContent);
		const appNode = schema["@graph"]?.find((item) => item["@type"] === "SoftwareApplication");
		if (appNode) {
			appNode.name = CONFIG.APP_NAME;
			appNode.softwareVersion = CONFIG.VERSION.replace(/^v/, "");
			appNode.downloadUrl = CONFIG.DIRECT_DOWNLOAD_URL;
			if (appNode.author) {
				appNode.author.name = "Sam Pangilinan (ZETICUZ)";
				appNode.author.url = CONFIG.PORTFOLIO_URL;
			}
			schemaScript.textContent = JSON.stringify(schema, null, "\t");
		}
	} catch (e) {
		// Graceful fallback
	}
}

// Mobile Drawer Navigation
const mobileMenuBtn = document.getElementById("mobile-menu-btn");
const mobileMenu = document.getElementById("mobile-menu");
const menuIconBars = document.getElementById("menu-icon-bars");
const menuIconClose = document.getElementById("menu-icon-close");

if (mobileMenuBtn && mobileMenu) {
	mobileMenuBtn.setAttribute("aria-controls", "mobile-menu");

	mobileMenuBtn.addEventListener("click", () => {
		const isOpen = !mobileMenu.classList.contains("hidden");
		if (isOpen) {
			mobileMenu.classList.add("hidden");
			mobileMenuBtn.setAttribute("aria-expanded", "false");
			if (menuIconBars) menuIconBars.classList.remove("hidden");
			if (menuIconClose) menuIconClose.classList.add("hidden");
		} else {
			mobileMenu.classList.remove("hidden");
			mobileMenuBtn.setAttribute("aria-expanded", "true");
			if (menuIconBars) menuIconBars.classList.add("hidden");
			if (menuIconClose) menuIconClose.classList.remove("hidden");
		}
	});

	// Close drawer on link click
	document.querySelectorAll(".mobile-nav-link").forEach((link) => {
		link.addEventListener("click", () => {
			mobileMenu.classList.add("hidden");
			mobileMenuBtn.setAttribute("aria-expanded", "false");
			if (menuIconBars) menuIconBars.classList.remove("hidden");
			if (menuIconClose) menuIconClose.classList.add("hidden");
		});
	});

	// Close on Escape key press (keyboard accessibility)
	document.addEventListener("keydown", (e) => {
		if (e.key === "Escape" && !mobileMenu.classList.contains("hidden")) {
			mobileMenu.classList.add("hidden");
			mobileMenuBtn.setAttribute("aria-expanded", "false");
			if (menuIconBars) menuIconBars.classList.remove("hidden");
			if (menuIconClose) menuIconClose.classList.add("hidden");
			mobileMenuBtn.focus();
		}
	});
}

// Universal Environment Link Adapter (Production Root vs Local File System)
if (window.location.protocol === "http:" || window.location.protocol === "https:") {
	document.querySelectorAll('a[href^="index.html#"]').forEach((link) => {
		const hash = link.getAttribute("href").replace("index.html#", "#");
		if (window.location.pathname === "/" || window.location.pathname === "/index.html") {
			link.setAttribute("href", hash);
		} else {
			link.setAttribute("href", "/" + hash);
		}
	});
}

// Interactive Desktop Mockup Simulator (Browser-Level Live Demonstration)
(function initMockupSimulator() {
	const CANDIDATES = [
		{ name: "Advik Malhotra", inst: "IIT Bombay", field: "Computer Science", year: "2026" },
		{ name: "Aarav Patel", inst: "BITS Pilani", field: "Artificial Intelligence", year: "2026" },
		{ name: "Rohan Verma", inst: "NIT Trichy", field: "Information Technology", year: "2025" },
		{
			name: "Ananya Iyer",
			inst: "Delhi Tech University",
			field: "Software Engineering",
			year: "2027",
		},
		{ name: "Diya Deshmukh", inst: "COEP Pune", field: "Data Science", year: "2026" },
		{ name: "Kabir Sen", inst: "IISc Bangalore", field: "Computer Engineering", year: "2025" },
	];

	const elName = document.getElementById("mock-name");
	const elInst = document.getElementById("mock-inst");
	const elField = document.getElementById("mock-field");
	const elYear = document.getElementById("mock-year");
	const elBtnRandom = document.getElementById("mock-btn-randomize");
	const elBtnStart = document.getElementById("mock-btn-start");
	const elTerminal = document.getElementById("mock-terminal-log");
	const elStep1 = document.getElementById("mock-step-1");
	const elStep2 = document.getElementById("mock-step-2");
	const elStep3 = document.getElementById("mock-step-3");
	const elStatusText = document.getElementById("mock-status-text");

	if (!elBtnRandom || !elTerminal) return;

	let isSimulating = false;

	function logTerminal(text, type = "normal") {
		const line = document.createElement("div");
		const time = new Date().toTimeString().split(" ")[0];
		if (type === "info") {
			line.className = "text-sky-300";
		} else if (type === "success") {
			line.className = "text-emerald-400 font-bold";
		} else if (type === "warn") {
			line.className = "text-amber-300";
		} else {
			line.className = "text-slate-400";
		}
		line.innerHTML = `<span class="text-slate-500 font-mono">[${time}]</span> ${text}`;
		elTerminal.appendChild(line);
		elTerminal.scrollTop = elTerminal.scrollHeight;
	}

	elBtnRandom.addEventListener("click", () => {
		const pick = CANDIDATES[Math.floor(Math.random() * CANDIDATES.length)];
		if (elName) elName.textContent = pick.name;
		if (elInst) elInst.textContent = pick.inst;
		if (elField) elField.textContent = pick.field;
		if (elYear) elYear.textContent = pick.year;

		// Flash effect
		[elName, elInst, elField, elYear].forEach((el) => {
			if (el) {
				el.classList.add("text-sky-300");
				setTimeout(() => el.classList.remove("text-sky-300"), 400);
			}
		});

		logTerminal(`Profile randomized: ${pick.name} (${pick.inst})`, "info");
	});

	if (elBtnStart) {
		elBtnStart.addEventListener("click", () => {
			if (isSimulating) return;
			isSimulating = true;
			elBtnStart.textContent = "⏳ Simulating...";
			elBtnStart.classList.add("opacity-75");

			if (elStatusText) elStatusText.textContent = "Engine Running";

			logTerminal("--------------------------------------------------", "normal");
			logTerminal("Initializing ZETICUZ AI PLUS GEN automation session...", "info");

			// Stepper updates
			setTimeout(() => {
				logTerminal("[1/5] Attaching to pre-installed Chromium engine...", "info");
				if (elStep1)
					elStep1.className = "text-sky-400 font-bold flex items-center gap-1.5 shrink-0";
			}, 900);

			setTimeout(() => {
				const candidateName = elName ? elName.textContent : "Advik Malhotra";
				logTerminal(`[2/5] Submitting candidate profile: ${candidateName}...`, "info");
			}, 2100);

			setTimeout(() => {
				logTerminal("[3/5] Challenge Gateway: OTP confirmation token requested.", "warn");
				if (elStep2)
					elStep2.className = "text-sky-400 font-bold flex items-center gap-1.5 shrink-0";
			}, 3300);

			setTimeout(() => {
				const randomOtp = Math.floor(100000 + Math.random() * 900000);
				logTerminal(`[4/5] Verification challenge token '${randomOtp}' confirmed.`, "success");
			}, 4400);

			setTimeout(() => {
				const promoCode = "G1-AI-" + Math.floor(10000000 + Math.random() * 90000000) + "-ZET7Z";
				const link = `https://one.google.com/promo/offer?token=${promoCode}&utm_source=zeticuz_ai_plus_gen`;
				logTerminal("[5/5] Canonical token link unwrapped & verified!", "success");
				logTerminal(
					`ACCESS LINK: <a href="${link}" target="_blank" rel="noopener noreferrer" class="text-sky-300 underline font-mono break-all">${link}</a>`,
					"success"
				);
				logTerminal("Archived link locally to results/zeticuz_google_one_links.txt", "info");

				if (elStep3)
					elStep3.className = "text-emerald-400 font-bold flex items-center gap-1.5 shrink-0";
				if (elStatusText) elStatusText.textContent = "Link Ready";

				elBtnStart.textContent = "✨ Link Generated!";
				setTimeout(() => {
					elBtnStart.textContent = "🚀 Get 1-Year Access Link";
					elBtnStart.classList.remove("opacity-75");
					isSimulating = false;
				}, 3000);
			}, 5600);
		});
	}
})();
