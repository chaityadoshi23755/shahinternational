document.addEventListener('DOMContentLoaded', () => {
    
    const mapConfig = { width: 4378, height: 2434 };
    
    const indiaHQ = { id: 'india-hq', name: 'Shah International', type: 'Exclusive Regional Partner', country: 'India', x: 3020, y: 1180 };
    
    const suppliers = [
        { id: 'schattdecor', name: 'Schattdecor', country: 'Germany', relationship: 'Official Partner', x: 2120, y: 420 },
        { id: 'hueck', name: 'Hueck Rheinische', country: 'Germany', relationship: 'Exclusive Principal', x: 2080, y: 380 },
        { id: 'deurowood', name: 'Deurowood', country: 'Austria', relationship: 'Official Partner', x: 2150, y: 450 },
        { id: 'arcolor', name: 'Arcolor', country: 'Switzerland', relationship: 'Official Partner', x: 2050, y: 470 },
        { id: 'kingdecor', name: 'Kingdecor', country: 'China', relationship: 'Exclusive Principal', x: 3580, y: 840 },
        { id: 'mitsubishi', name: 'Mitsubishi Chemical', country: 'Japan', relationship: 'Official Partner', x: 3800, y: 740 },
        { id: 'coveright', name: 'Coveright', country: 'Brazil', relationship: 'Official Partner', x: 1300, y: 1600 }
    ];

    const markersLayer = document.getElementById('map-markers-layer');
    const routesGroup = document.getElementById('trade-routes-group');
    const particlesGroup = document.getElementById('trade-particles-group');

    if (!markersLayer || !routesGroup || !particlesGroup) return;

    // Helper: calculate orthogonal control point for Bezier curve
    function getBezierControlPoint(x1, y1, x2, y2, bendFactor = 0.2) {
        const mx = (x1 + x2) / 2;
        const my = (y1 + y2) / 2;
        const dx = x2 - x1;
        const dy = y2 - y1;
        const dist = Math.hypot(dx, dy);
        
        let nx = -dy / dist;
        let ny = dx / dist;
        
        if (ny > 0) {
            nx = -nx;
            ny = -ny;
        }

        return {
            cx: mx + nx * dist * bendFactor,
            cy: my + ny * dist * bendFactor
        };
    }

    // 1. Render India HQ
    const hqEl = document.createElement('div');
    hqEl.className = 'map-marker hq-marker';
    hqEl.style.left = `${(indiaHQ.x / mapConfig.width) * 100}%`;
    hqEl.style.top = `${(indiaHQ.y / mapConfig.height) * 100}%`;
    hqEl.innerHTML = `
        <div class="hq-pulse"></div>
        <div class="hq-pulse delay"></div>
        <div class="hq-dot"></div>
        <div class="hq-badge">${indiaHQ.type}</div>
    `;
    markersLayer.appendChild(hqEl);

    // 2. Render Suppliers and Routes
    suppliers.forEach((sup, index) => {
        // --- HTML Marker ---
        const supEl = document.createElement('div');
        supEl.className = 'map-marker supplier-marker hidden-anim';
        supEl.style.left = `${(sup.x / mapConfig.width) * 100}%`;
        supEl.style.top = `${(sup.y / mapConfig.height) * 100}%`;
        supEl.style.transitionDelay = `${index * 0.15}s`;
        
        supEl.innerHTML = `
            <div class="sup-dot"></div>
            <div class="sup-tooltip">
                <div class="sup-name">${sup.name}</div>
                <div class="sup-country">${sup.country}</div>
                <div class="sup-meta">${sup.relationship}</div>
            </div>
        `;
        
        supEl.addEventListener('mouseenter', () => activateRoute(sup.id));
        supEl.addEventListener('mouseleave', deactivateRoutes);
        
        markersLayer.appendChild(supEl);

        // --- SVG Route (Bezier) ---
        const bend = 0.15 + (index % 4) * 0.08; 
        const cp = getBezierControlPoint(sup.x, sup.y, indiaHQ.x, indiaHQ.y, bend);
        
        const pathData = `M ${sup.x} ${sup.y} Q ${cp.cx} ${cp.cy} ${indiaHQ.x} ${indiaHQ.y}`;
        
        const pathNode = document.createElementNS("http://www.w3.org/2000/svg", "path");
        pathNode.setAttribute("d", pathData);
        pathNode.setAttribute("class", `trade-route route-${sup.id}`);
        routesGroup.appendChild(pathNode);
        
        // Wait a tick for the path to render so we can get its length
        requestAnimationFrame(() => {
            const length = pathNode.getTotalLength();
            pathNode.style.setProperty('--path-length', length);
            pathNode.style.strokeDasharray = length;
            pathNode.style.strokeDashoffset = length;
        });

        const motionPath = document.createElementNS("http://www.w3.org/2000/svg", "path");
        motionPath.setAttribute("d", pathData);
        motionPath.setAttribute("id", `motion-${sup.id}`);
        motionPath.setAttribute("fill", "none");
        motionPath.setAttribute("stroke", "none");
        routesGroup.appendChild(motionPath);

        // --- SVG Particles ---
        for(let i=0; i<2; i++) {
            const particleGroup = document.createElementNS("http://www.w3.org/2000/svg", "g");
            particleGroup.setAttribute("class", `trade-particle particle-${sup.id}`);
            
            const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
            circle.setAttribute("r", "4");
            circle.setAttribute("fill", "#E23137");
            circle.setAttribute("filter", "drop-shadow(0 0 6px rgba(226,49,55,0.7))");
            
            const animateMotion = document.createElementNS("http://www.w3.org/2000/svg", "animateMotion");
            animateMotion.setAttribute("dur", `${5.5 + index*0.4}s`);
            animateMotion.setAttribute("repeatCount", "indefinite");
            animateMotion.setAttribute("begin", `${i * 1.75}s`);
            
            const mpath = document.createElementNS("http://www.w3.org/2000/svg", "mpath");
            mpath.setAttributeNS("http://www.w3.org/1999/xlink", "href", `#motion-${sup.id}`);
            
            animateMotion.appendChild(mpath);
            particleGroup.appendChild(circle);
            particleGroup.appendChild(animateMotion);
            particlesGroup.appendChild(particleGroup);
        }
    });

    function activateRoute(supplierId) {
        document.querySelectorAll('.trade-route').forEach(r => {
            if (r.classList.contains(`route-${supplierId}`)) {
                r.classList.add('active');
            } else {
                r.classList.add('dimmed');
            }
        });
        document.querySelectorAll('.trade-particle').forEach(p => {
            if (!p.classList.contains(`particle-${supplierId}`)) {
                p.classList.add('dimmed');
            } else {
                p.classList.add('active');
            }
        });
        hqEl.classList.add('highlighted');
    }

    function deactivateRoutes() {
        document.querySelectorAll('.trade-route').forEach(r => {
            r.classList.remove('active', 'dimmed');
        });
        document.querySelectorAll('.trade-particle').forEach(p => {
            p.classList.remove('dimmed', 'active');
        });
        hqEl.classList.remove('highlighted');
    }

    const mapContainer = document.querySelector('.interactive-world-map-container');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                mapContainer.classList.add('animated');
                
                document.querySelectorAll('.supplier-marker').forEach(m => {
                    m.classList.remove('hidden-anim');
                });

                document.querySelectorAll('.trade-route').forEach((r, i) => {
                    setTimeout(() => {
                        r.classList.add('draw');
                    }, 800 + i * 200);
                });
                
                setTimeout(() => {
                    particlesGroup.classList.add('visible');
                }, 2500);
                
                observer.unobserve(mapContainer);
            }
        });
    }, { threshold: 0.3 });
    
    if(mapContainer) {
        observer.observe(mapContainer);
    }
});
