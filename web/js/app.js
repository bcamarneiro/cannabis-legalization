// Regulação da Cannabis em Portugal — Interactive Web JS

// ============ CITATION POPOVER ============
function showCitationPopover(el) {
    closePopover();
    const refData = el.getAttribute('data-ref');
    if (!refData) return;
    
    let ref;
    try {
        ref = JSON.parse(refData.replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>'));
    } catch(e) {
        try { ref = JSON.parse(el.getAttribute('data-ref')); } catch(e2) { return; }
    }
    
    const popover = document.getElementById('citation-popover');
    const overlay = document.getElementById('popover-overlay');
    
    let html = '<span class="pop-close" onclick="closePopover()">&times;</span>';
    
    if (ref.title) html += '<div class="pop-title">' + escapeHtml(ref.title) + '</div>';
    if (ref.author) html += '<div class="pop-author">' + escapeHtml(ref.author.replace(/[{}]/g, '')) + '</div>';
    if (ref.year) html += '<div class="pop-year">' + escapeHtml(ref.year) + '</div>';
    if (ref.url) html += '<div class="pop-url"><a href="' + escapeHtml(ref.url) + '" target="_blank">' + escapeHtml(ref.url) + '</a></div>';
    if (ref.note) html += '<div class="pop-note">' + escapeHtml(ref.note) + '</div>';
    if (ref.urldate) html += '<div class="pop-year">Acedido: ' + escapeHtml(ref.urldate) + '</div>';
    
    popover.innerHTML = html;
    
    // Position near the clicked element
    const rect = el.getBoundingClientRect();
    popover.style.top = (rect.bottom + 8) + 'px';
    popover.style.left = Math.max(16, Math.min(rect.left, window.innerWidth - 420)) + 'px';
    
    popover.classList.add('active');
    overlay.classList.add('active');
}

function closePopover() {
    document.getElementById('citation-popover').classList.remove('active');
    document.getElementById('popover-overlay').classList.remove('active');
}

function escapeHtml(str) {
    if (!str) return '';
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

// ============ FULL-TEXT SEARCH (Fuse.js-like) ============
let searchData = [];
let searchIndex = null;

function initSearch() {
    searchData = window.__SEARCH_DATA || [];
    const input = document.getElementById('search-input');
    const results = document.getElementById('search-results');
    
    if (!input) return;
    
    let debounceTimer;
    input.addEventListener('input', function() {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => performSearch(this.value), 200);
    });
    
    input.addEventListener('focus', function() {
        if (this.value.length >= 2) results.classList.add('active');
    });
    
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.search-container')) {
            results.classList.remove('active');
        }
    });
}

function performSearch(query) {
    const results = document.getElementById('search-results');
    if (query.length < 2) {
        results.classList.remove('active');
        return;
    }
    
    const terms = query.toLowerCase().split(/\s+/).filter(t => t.length >= 2);
    const matches = [];
    
    searchData.forEach(item => {
        const titleLower = item.title.toLowerCase();
        const contentLower = item.content.toLowerCase();
        let score = 0;
        let snippet = '';
        
        terms.forEach(term => {
            // Title match (higher weight)
            if (titleLower.includes(term)) score += 10;
            // Content match
            const idx = contentLower.indexOf(term);
            if (idx !== -1) {
                score += 1;
                if (!snippet) {
                    const start = Math.max(0, idx - 40);
                    const end = Math.min(item.content.length, idx + 80);
                    snippet = (start > 0 ? '...' : '') + item.content.substring(start, end) + (end < item.content.length ? '...' : '');
                }
            }
        });
        
        if (score > 0) {
            matches.push({ ...item, score, snippet });
        }
    });
    
    matches.sort((a, b) => b.score - a.score);
    
    let html = '';
    matches.slice(0, 10).forEach(m => {
        let highlightedSnippet = m.snippet;
        terms.forEach(term => {
            const regex = new RegExp('(' + term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
            highlightedSnippet = highlightedSnippet.replace(regex, '<mark>$1</mark>');
        });
        html += '<div class="search-result-item" onclick="navigateToSection(\'' + m.id + '\', \'' + query + '\')">';
        html += '<div class="result-title">' + escapeHtml(m.title) + '</div>';
        html += '<div class="result-snippet">' + highlightedSnippet + '</div>';
        html += '</div>';
    });
    
    if (matches.length === 0) {
        html = '<div class="search-result-item"><div class="result-snippet">Sem resultados para "' + escapeHtml(query) + '"</div></div>';
    }
    
    results.innerHTML = html;
    results.classList.add('active');
}

function navigateToSection(sectionId, query) {
    document.getElementById('search-results').classList.remove('active');
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
        // Highlight matches in the section
        if (query) highlightInSection(section, query);
    }
}

function highlightInSection(section, query) {
    // Remove previous highlights
    document.querySelectorAll('mark.search-highlight').forEach(m => {
        m.outerHTML = m.textContent;
    });
    
    const terms = query.toLowerCase().split(/\s+/).filter(t => t.length >= 2);
    const walker = document.createTreeWalker(section, NodeFilter.SHOW_TEXT, null, false);
    const textNodes = [];
    while (walker.nextNode()) textNodes.push(walker.currentNode);
    
    textNodes.forEach(node => {
        if (node.parentElement.classList.contains('citation')) return;
        const text = node.textContent;
        let hasMatch = false;
        terms.forEach(term => {
            if (text.toLowerCase().includes(term)) hasMatch = true;
        });
        if (!hasMatch) return;
        
        const span = document.createElement('span');
        let html = text;
        terms.forEach(term => {
            const regex = new RegExp('(' + term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
            html = html.replace(regex, '<mark class="search-highlight">$1</mark>');
        });
        span.innerHTML = html;
        node.parentNode.replaceChild(span, node);
    });
    
    // Remove highlights after 5 seconds
    setTimeout(() => {
        document.querySelectorAll('mark.search-highlight').forEach(m => {
            m.outerHTML = m.textContent;
        });
    }, 5000);
}

// ============ GLOSSARY TOOLTIPS ============
function initGlossaryTooltips() {
    const glossaryTerms = window.__GLOSSARY || {};
    const termKeys = Object.keys(glossaryTerms).sort((a, b) => b.length - a.length);
    
    // Find text nodes in main content and wrap glossary terms
    const content = document.querySelector('.main-content');
    if (!content) return;
    
    const walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT, null, false);
    const textNodes = [];
    while (walker.nextNode()) {
        const parent = walker.currentNode.parentElement;
        if (parent && !parent.closest('.citation') && !parent.closest('h1') && !parent.closest('h2') && 
            !parent.closest('h3') && parent.tagName !== 'CODE' && parent.tagName !== 'A' && 
            parent.tagName !== 'STRONG' && parent.tagName !== 'EM') {
            textNodes.push(walker.currentNode);
        }
    }
    
    textNodes.forEach(node => {
        let text = node.textContent;
        let modified = false;
        
        termKeys.forEach(term => {
            if (text.toLowerCase().includes(term.toLowerCase()) && term.length > 3) {
                const regex = new RegExp('\\b(' + term.replace(/[.*+?^${}()|[\\]\\]/g, '\\$&') + ')\\b', 'gi');
                const definition = glossaryTerms[term];
                text = text.replace(regex, '<span class="glossary-term" data-definition="' + 
                    definition.replace(/"/g, '&quot;').replace(/'/g, '&#39;') + 
                    '" onmouseenter="showGlossaryTooltip(event, this)" onmouseleave="hideGlossaryTooltip()">$1</span>');
                modified = true;
            }
        });
        
        if (modified) {
            const span = document.createElement('span');
            span.innerHTML = text;
            node.parentNode.replaceChild(span, node);
        }
    });
}

function showGlossaryTooltip(event, el) {
    const tooltip = document.getElementById('glossary-tooltip');
    const definition = el.getAttribute('data-definition');
    tooltip.textContent = definition;
    
    const rect = el.getBoundingClientRect();
    tooltip.style.top = (rect.bottom + 8) + 'px';
    tooltip.style.left = Math.max(16, Math.min(rect.left, window.innerWidth - 320)) + 'px';
    tooltip.classList.add('active');
}

function hideGlossaryTooltip() {
    document.getElementById('glossary-tooltip').classList.remove('active');
}

// ============ SIDEBAR ACTIVE STATE ============
function initSidebarTracking() {
    const sections = document.querySelectorAll('.chapter-section');
    const links = document.querySelectorAll('.sidebar a');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                links.forEach(l => l.classList.remove('active'));
                const link = document.querySelector('.sidebar a[href="#' + entry.target.id + '"]');
                if (link) link.classList.add('active');
            }
        });
    }, { rootMargin: '-20% 0px -60% 0px' });
    
    sections.forEach(s => observer.observe(s));
}

// ============ MOBILE MENU ============
function toggleMobileMenu() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('mobile-open');
}

// ============ INIT ============
document.addEventListener('DOMContentLoaded', function() {
    initSearch();
    initGlossaryTooltips();
    initSidebarTracking();
    
    // Close popover on overlay click
    document.getElementById('popover-overlay').addEventListener('click', closePopover);
    
    // Escape key closes popover
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closePopover();
    });
});
