document.addEventListener("DOMContentLoaded", () => {
    const grid = document.getElementById('pixelGrid');
    const output = document.getElementById('editorOutput');
    const colorPicker = document.getElementById('editorColorPicker');
    let isDrawing = false;
    let currentW = 8;
    let currentH = 8;

    window.setEditorMode = (w, h) => {
        currentW = w;
        currentH = h;
        initGrid();
    };

    window.clearEditor = () => {
        document.querySelectorAll('.pixel-cell').forEach(c => c.style.backgroundColor = '#000000');
        updateOutput();
    };

    window.copyEditorCode = (btn) => {
        output.select();
        document.execCommand('copy');
        
        const originalText = btn.textContent;
        btn.textContent = "✅ Copied!";
        btn.classList.add('md-button--primary');
        
        setTimeout(() => {
            btn.textContent = originalText;
            btn.classList.remove('md-button--primary');
        }, 2000);
    };

    function initGrid() {
        grid.style.gridTemplateColumns = `repeat(${currentW}, 1fr)`;
        grid.innerHTML = '';
        for (let i = 0; i < currentW * currentH; i++) {
            const cell = document.createElement('div');
            cell.className = 'pixel-cell';
            cell.style.backgroundColor = '#000000';
            cell.addEventListener('mousedown', (e) => { isDrawing = true; paint(e); });
            cell.addEventListener('mouseover', (e) => { if (isDrawing) paint(e); });
            grid.appendChild(cell);
        }
        updateOutput();
    }

    function paint(e) {
        e.target.style.backgroundColor = colorPicker.value;
        updateOutput();
    }

    window.addEventListener('mouseup', () => isDrawing = false);

    function rgb565ToRgb(val) {
        val = parseInt(val, 16);
        const r = Math.round(((val >> 11) & 0x1F) * 255 / 31);
        const g = Math.round(((val >> 5) & 0x3F) * 255 / 63);
        const b = Math.round((val & 0x1F) * 255 / 31);
        return `rgb(${r}, ${g}, ${b})`;
    }

    function updateOutput() {
        const cells = document.querySelectorAll('.pixel-cell');
        const rgb565Array = Array.from(cells).map(cell => {
            const rgb = cell.style.backgroundColor.match(/\d+/g).map(Number);
            const r5 = (rgb[0] >> 3) & 0x1F;
            const g6 = (rgb[1] >> 2) & 0x3F;
            const b5 = (rgb[2] >> 3) & 0x1F;
            const rgb565 = (r5 << 11) | (g6 << 5) | b5;
            return `0x${rgb565.toString(16).toUpperCase().padStart(4, '0')}`;
        });
        output.value = `const uint16_t drawn_${currentW}x${currentH}[] = {\n    ${rgb565Array.join(', ')}\n};`;
    }

    output.addEventListener('input', () => {
        const matches = output.value.match(/0x[0-9A-Fa-f]{4}/g);
        if (matches) {
            const cells = document.querySelectorAll('.pixel-cell');
            matches.forEach((hex, index) => {
                if (cells[index]) {
                    cells[index].style.backgroundColor = rgb565ToRgb(hex);
                }
            });
        }
    });

    initGrid();
});
