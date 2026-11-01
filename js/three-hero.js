/**
 * ZETICUZ AI PLUS GEN — 3D WebGL Hero Motion System
 * Developed with raw Three.js for Sam Pangilinan (ZETICUZ / TECHNOLOHIYA)
 * Provides 60fps cinematic 3D neural core, orbital token rings, and pointer parallax.
 */

(function initThreeHero() {
	const canvas = document.getElementById("three-hero-canvas");
	if (!canvas) return;

	// Check prefers-reduced-motion
	const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

	// Scene & Camera
	const scene = new THREE.Scene();
	const camera = new THREE.PerspectiveCamera(
		45,
		canvas.clientWidth / canvas.clientHeight,
		0.1,
		1000
	);
	camera.position.z = 28;

	// Renderer with optimal performance settings
	const renderer = new THREE.WebGLRenderer({
		canvas: canvas,
		alpha: true,
		antialias: true,
		powerPreference: "high-performance",
	});
	renderer.setSize(canvas.clientWidth, canvas.clientHeight, false);
	renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

	// Group to hold all 3D scene elements
	const rootGroup = new THREE.Group();
	scene.add(rootGroup);

	// 1. Core Geometric AI Crystal (Icosahedron Wireframe & Point Nodes)
	const coreGeo = new THREE.IcosahedronGeometry(6.5, 1);
	const coreMat = new THREE.MeshBasicMaterial({
		color: 0x0284c7, // Sky 600
		wireframe: true,
		transparent: true,
		opacity: 0.35,
	});
	const coreMesh = new THREE.Mesh(coreGeo, coreMat);
	rootGroup.add(coreMesh);

	// Inner solid faceted core with glowing edges
	const innerGeo = new THREE.OctahedronGeometry(4, 0);
	const innerMat = new THREE.MeshStandardMaterial({
		color: 0x090d16,
		roughness: 0.2,
		metalness: 0.8,
		emissive: 0x0284c7,
		emissiveIntensity: 0.25,
		wireframe: false,
	});
	const innerMesh = new THREE.Mesh(innerGeo, innerMat);
	rootGroup.add(innerMesh);

	// 2. Orbital AI Token Ring (Instanced / Particle Points)
	const ringParticleCount = 180;
	const ringPositions = new Float32Array(ringParticleCount * 3);
	const ringRadius = 11.5;

	for (let i = 0; i < ringParticleCount; i++) {
		const theta = (i / ringParticleCount) * Math.PI * 2;
		const r = ringRadius + (Math.random() - 0.5) * 1.2;
		ringPositions[i * 3] = Math.cos(theta) * r;
		ringPositions[i * 3 + 1] = Math.sin(theta * 3) * 0.8 + (Math.random() - 0.5) * 0.6;
		ringPositions[i * 3 + 2] = Math.sin(theta) * r;
	}

	const ringGeo = new THREE.BufferGeometry();
	ringGeo.setAttribute("position", new THREE.BufferAttribute(ringPositions, 3));

	const ringMat = new THREE.PointsMaterial({
		color: 0x38bdf8, // Sky 400
		size: 0.32,
		transparent: true,
		opacity: 0.85,
		blending: THREE.AdditiveBlending,
	});
	const ringMesh = new THREE.Points(ringGeo, ringMat);
	ringMesh.rotation.x = Math.PI * 0.25;
	rootGroup.add(ringMesh);

	// Second Counter-Rotating Orbital Ring
	const ring2Geo = ringGeo.clone();
	const ring2Mat = new THREE.PointsMaterial({
		color: 0x34d399, // Emerald 400
		size: 0.25,
		transparent: true,
		opacity: 0.65,
		blending: THREE.AdditiveBlending,
	});
	const ring2Mesh = new THREE.Points(ring2Geo, ring2Mat);
	ring2Mesh.rotation.x = -Math.PI * 0.3;
	ring2Mesh.rotation.z = Math.PI * 0.15;
	rootGroup.add(ring2Mesh);

	// 3. Floating Background Ambient Dust
	const dustCount = 120;
	const dustPositions = new Float32Array(dustCount * 3);
	for (let i = 0; i < dustCount; i++) {
		dustPositions[i * 3] = (Math.random() - 0.5) * 60;
		dustPositions[i * 3 + 1] = (Math.random() - 0.5) * 40;
		dustPositions[i * 3 + 2] = (Math.random() - 0.5) * 40;
	}
	const dustGeo = new THREE.BufferGeometry();
	dustGeo.setAttribute("position", new THREE.BufferAttribute(dustPositions, 3));
	const dustMat = new THREE.PointsMaterial({
		color: 0x94a3b8,
		size: 0.18,
		transparent: true,
		opacity: 0.4,
	});
	const dustMesh = new THREE.Points(dustGeo, dustMat);
	scene.add(dustMesh);

	// Lighting
	const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
	scene.add(ambientLight);

	const pointLightCyan = new THREE.PointLight(0x38bdf8, 2, 50);
	pointLightCyan.position.set(12, 12, 14);
	scene.add(pointLightCyan);

	const pointLightCobalt = new THREE.PointLight(0x0284c7, 1.8, 50);
	pointLightCobalt.position.set(-14, -10, 10);
	scene.add(pointLightCobalt);

	// Mouse Interaction & Damped Parallax
	let mouseX = 0;
	let mouseY = 0;
	let targetX = 0;
	let targetY = 0;

	function onPointerMove(e) {
		const clientX = e.touches ? e.touches[0].clientX : e.clientX;
		const clientY = e.touches ? e.touches[0].clientY : e.clientY;
		const rect = canvas.getBoundingClientRect();
		mouseX = ((clientX - rect.left) / rect.width) * 2 - 1;
		mouseY = -(((clientY - rect.top) / rect.height) * 2 - 1);
	}

	window.addEventListener("mousemove", onPointerMove, { passive: true });
	window.addEventListener("touchmove", onPointerMove, { passive: true });

	// Responsive Canvas Sizing
	function resize() {
		const width = canvas.parentElement.clientWidth;
		const height = canvas.parentElement.clientHeight;
		if (canvas.width !== width || canvas.height !== height) {
			camera.aspect = width / height;
			camera.updateProjectionMatrix();
			renderer.setSize(width, height, false);
		}
	}
	window.addEventListener("resize", resize, { passive: true });
	resize();

	// Viewport Visibility Check (pause when scrolled out)
	let isVisible = true;
	const observer = new IntersectionObserver(
		(entries) => {
			isVisible = entries[0].isIntersecting;
		},
		{ threshold: 0.05 }
	);
	observer.observe(canvas);

	// Animation Loop
	let clock = new THREE.Clock();

	function animate() {
		requestAnimationFrame(animate);

		if (!isVisible) return;

		const delta = clock.getDelta();
		const time = clock.getElapsedTime();

		if (!prefersReducedMotion) {
			// Continuous subtle rotation
			coreMesh.rotation.y += 0.25 * delta;
			coreMesh.rotation.x += 0.12 * delta;

			innerMesh.rotation.y -= 0.35 * delta;
			innerMesh.rotation.z += 0.18 * delta;

			ringMesh.rotation.z += 0.3 * delta;
			ring2Mesh.rotation.z -= 0.22 * delta;

			// Floating vertical bobbing
			rootGroup.position.y = Math.sin(time * 1.4) * 0.45;

			// Smooth Damped Parallax
			targetX += (mouseX * 0.45 - targetX) * 0.05;
			targetY += (mouseY * 0.35 - targetY) * 0.05;

			rootGroup.rotation.y = targetX * 1.2;
			rootGroup.rotation.x = -targetY * 0.9;
		}

		renderer.render(scene, camera);
	}

	animate();
})();
