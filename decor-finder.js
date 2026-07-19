document.addEventListener('DOMContentLoaded', () => {
  const grid = document.getElementById('decor-grid');
  const resultCount = document.getElementById('result-count');
  const checkboxes = document.querySelectorAll('.filter-checkbox');
  const clearBtn = document.getElementById('clear-filters');

  function renderDecors(decors) {
    grid.innerHTML = '';
    resultCount.textContent = decors.length;
    
    if (decors.length === 0) {
      grid.innerHTML = '<p style="grid-column: 1 / -1; text-align: center; padding: 2rem;">No decors match your selected filters. Try removing some.</p>';
      return;
    }

    decors.forEach(decor => {
      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <div class="card-img-wrap">
          <img src="${decor.image}" alt="${decor.name}" class="card-img">
        </div>
        <div class="card-body">
          <h3 class="card-title">${decor.name}</h3>
          <p style="margin: 0.5rem 0 1rem 0; font-size: 0.85rem; color: var(--color-text-light); text-transform: uppercase; letter-spacing: 1px;">
            ${decor.principal} &bull; ${decor.color} &bull; ${decor.application}
          </p>
          <a href="#" class="btn btn-secondary" style="font-size:0.8rem; padding: 5px 10px; border-radius: 0; border: 1px solid var(--color-text);">Request Sample</a>
        </div>
      `;
      grid.appendChild(card);
    });
  }

  function filterDecors() {
    const activeFilters = {
      principal: [],
      color: [],
      application: []
    };

    checkboxes.forEach(cb => {
      if (cb.checked) {
        activeFilters[cb.dataset.filterType].push(cb.value);
      }
    });

    const filtered = decorData.filter(decor => {
      const matchPrincipal = activeFilters.principal.length === 0 || activeFilters.principal.includes(decor.principal);
      const matchColor = activeFilters.color.length === 0 || activeFilters.color.includes(decor.color);
      const matchApplication = activeFilters.application.length === 0 || activeFilters.application.includes(decor.application);
      
      return matchPrincipal && matchColor && matchApplication;
    });

    renderDecors(filtered);
  }

  checkboxes.forEach(cb => {
    cb.addEventListener('change', filterDecors);
  });

  clearBtn.addEventListener('click', () => {
    checkboxes.forEach(cb => cb.checked = false);
    filterDecors();
  });

  // Initial render
  if (typeof decorData !== 'undefined') {
    renderDecors(decorData);
  }
});
