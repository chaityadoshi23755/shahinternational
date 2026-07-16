const fs = require('fs');
const cssPath = 'C:/Users/chait/OneDrive/Desktop/shahinternational/full_site/shahinternational.in/style.css';
let css = fs.readFileSync(cssPath, 'utf8');

css = css.replace(/--space-lg: 4rem;/, '--space-lg: 5rem;');
css = css.replace(/--space-xl: 6rem;/, '--space-xl: 8rem;');
css = css.replace(/--color-bg-alt: #f8f9fa;/, '--color-bg-alt: #F9F9F7;');
css = css.replace(/--transition-normal: 0.3s ease;/, '--transition-normal: 0.4s cubic-bezier(0.25, 1, 0.5, 1);');
css = css.replace(/--transition-slow: 0.5s ease;/, '--transition-slow: 0.7s cubic-bezier(0.25, 1, 0.5, 1);');

css = css.replace(/h1, h2, h3, h4, h5, h6 \{\s*font-family: var\(--font-heading\);\s*font-weight: 600;/g, 'h1, h2, h3, h4, h5, h6 {\\n  font-family: var(--font-heading);\\n  font-weight: 400;\\n  letter-spacing: 0.01em;');
css = css.replace(/line-height: 1.8;/, 'line-height: 2.0;');
css = css.replace(/--color-text-light: #6b7280;/, '--color-text-light: #525252;');

css = css.replace(/\.site-header \{\s*background-color: var\(--color-bg\);/, '.site-header {\\n  background-color: rgba(255, 255, 255, 0.9);\\n  backdrop-filter: blur(12px);\\n  -webkit-backdrop-filter: blur(12px);');
css = css.replace(/\.nav-links \.dropdown-menu \{\s*position: absolute;\s*top: calc\(100% \+ 0\.5rem\);\s*left: 50%;\s*transform: translateX\(-50%\);\s*background: var\(--color-bg\);/, '.nav-links .dropdown-menu {\\n  position: absolute;\\n  top: calc(100% + 0.5rem);\\n  left: 50%;\\n  transform: translateX(-50%);\\n  background: rgba(255, 255, 255, 0.95);\\n  backdrop-filter: blur(12px);\\n  -webkit-backdrop-filter: blur(12px);');

css = css.replace(/border-radius: 4px;/g, 'border-radius: 2px;');
css = css.replace(/border-radius: 8px;/g, 'border-radius: 2px;');
css = css.replace(/border-radius: 12px;/g, 'border-radius: 2px;');

css = css.replace(/box-shadow: var\(--shadow-sm\);/g, 'box-shadow: 0 4px 12px rgba(0,0,0,0.02);');
css = css.replace(/box-shadow: var\(--shadow-md\);/g, 'box-shadow: 0 10px 30px rgba(0,0,0,0.04);');
css = css.replace(/\.card:hover \{\s*transform: translateY\(-5px\);\s*box-shadow: var\(--shadow-lg\);\s*\}/g, '.card:hover {\\n  transform: translateY(-4px);\\n  box-shadow: 0 20px 40px rgba(0,0,0,0.08);\\n}');
css = css.replace(/\.card-thumbnail img \{\s*width: 100%;\s*height: 100%;\s*object-fit: cover;\s*\}/, '.card-thumbnail img {\\n  width: 100%;\\n  height: 100%;\\n  object-fit: cover;\\n  transition: var(--transition-slow);\\n}\\n.card-thumbnail:hover img {\\n  transform: scale(1.05);\\n}');

const scrollRevealCSS = "\\n/* ========== SCROLL REVEAL ========== */\\n.reveal {\\n  opacity: 0;\\n  transform: translateY(30px);\\n  transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1), transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);\\n  will-change: opacity, transform;\\n}\\n.reveal.active {\\n  opacity: 1;\\n  transform: translateY(0);\\n}\\n.reveal-delay-1 { transition-delay: 0.1s; }\\n.reveal-delay-2 { transition-delay: 0.2s; }\\n.reveal-delay-3 { transition-delay: 0.3s; }\\n";
if (!css.includes('.reveal.active')) {
  css += scrollRevealCSS;
}

fs.writeFileSync(cssPath, css, 'utf8');
console.log('CSS updated successfully');
