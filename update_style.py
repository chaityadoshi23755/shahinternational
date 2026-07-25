css_code = """
/* Banner Scroll Indicator */
.banner-scroll-indicator {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  color: #ffffff;
  font-size: 2rem;
  cursor: pointer;
  z-index: 10;
  animation: banner-bounce 2s infinite;
  opacity: 0.8;
  transition: opacity 0.3s ease;
}
.banner-scroll-indicator:hover {
  opacity: 1;
}
@keyframes banner-bounce {
  0%, 20%, 50%, 80%, 100% { transform: translate(-50%, 0); }
  40% { transform: translate(-50%, -15px); }
  60% { transform: translate(-50%, -7px); }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_code)

print("Added banner-scroll-indicator to style.css")
