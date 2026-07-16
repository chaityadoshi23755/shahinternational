const fs = require('fs');
const cssPath = 'C:/Users/chait/OneDrive/Desktop/shahinternational/full_site/shahinternational.in/style.css';
let css = fs.readFileSync(cssPath, 'utf8');

const modalCSS = 
/* ========== DECOR REPEAT MODAL ========== */
.decor-repeat-modal {
  position: fixed;
  top: 0; left: 0; width: 100vw; height: 100vh;
  z-index: 99999;
  background-color: #fff;
  background-repeat: repeat;
  background-position: top left;
  display: none;
  opacity: 0;
  transition: opacity 0.4s ease;
}
.decor-repeat-modal.is-open {
  display: block;
}
.decor-repeat-modal.is-visible {
  opacity: 1;
}
.decor-repeat-close {
  position: absolute;
  top: 2rem; right: 2rem;
  background: var(--color-brand-red);
  color: #fff;
  border: none;
  border-radius: 50%;
  width: 50px; height: 50px;
  font-size: 24px;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  transition: transform 0.3s ease;
}
.decor-repeat-close:hover {
  transform: scale(1.1);
}
;

if (!css.includes('.decor-repeat-modal')) {
  css += '\n' + modalCSS;
  fs.writeFileSync(cssPath, css, 'utf8');
}
