document.addEventListener("DOMContentLoaded", () => {
    const grid = document.getElementById('pixelGrid');
    const output = document.getElementById('editorOutput');
    const inR = document.getElementById('input-r'), inG = document.getElementById('input-g'), inB = document.getElementById('input-b');
    let isDrawing = false, currentW = 8, currentH = 8, currentColor = "#F44336";

    const colorPicker = new iro.ColorPicker("#iroPicker", {
        width: 220, color: currentColor,
        layout: [{ component: iro.ui.Box }, { component: iro.ui.Slider, options: { sliderType: 'hue' } }]
    });

    colorPicker.on(['color:init', 'color:change'], (color) => {
        currentColor = color.hexString;
        inR.value = color.rgb.r; inG.value = color.rgb.g; inB.value = color.rgb.b;
    });

    [inR, inG, inB].forEach(el => {
        el.addEventListener('input', () => {
            colorPicker.color.set({ r: inR.value, g: inG.value, b: inB.value });
        });
    });

    window.setEditorMode = (w, h) => {
        currentW = w; currentH = h;
        grid.style.gridTemplateColumns = `repeat(${w}, 1fr)`;
        grid.innerHTML = '';
        for (let i = 0; i < w * h; i++) {
            const cell = document.createElement('div');
            cell.className = 'pixel-cell';
            cell.style.backgroundColor = '#000000';
            cell.addEventListener('mousedown', (e) => { isDrawing = true; paint(e); });
            cell.addEventListener('mouseover', (e) => { if (isDrawing) paint(e); });
            grid.appendChild(cell);
        }
        updateOutput();
    };

    function paint(e) { e.target.style.backgroundColor = currentColor; updateOutput(); }
    window.addEventListener('mouseup', () => isDrawing = false);

    window.clearEditor = () => {
        document.querySelectorAll('.pixel-cell').forEach(c => c.style.backgroundColor = '#000000');
        updateOutput();
    };

    window.copyEditorCode = (btn) => {
        output.select(); document.execCommand('copy');
        const old = btn.textContent; btn.textContent = "✅ Copied!";
        btn.classList.add('md-button--primary');
        setTimeout(() => { btn.textContent = old; btn.classList.remove('md-button--primary'); }, 2000);
    };

    function updateOutput() {
        const cells = document.querySelectorAll('.pixel-cell');
        const rgb565 = Array.from(cells).map(c => {
            const rgb = c.style.backgroundColor.match(/\d+/g).map(Number);
            const val = ((rgb[0] >> 3) << 11) | ((rgb[1] >> 2) << 5) | (rgb[2] >> 3);
            return `0x${val.toString(16).toUpperCase().padStart(4, '0')}`;
        });
        output.value = `const uint16_t drawn_${currentW}x${currentH}[] = {\n    ${rgb565.join(', ')}\n};`;
    }

    output.addEventListener('input', () => {
        const matches = output.value.match(/0x[0-9A-Fa-f]{4}/g);
        if (matches) {
            const cells = document.querySelectorAll('.pixel-cell');
            matches.forEach((hex, i) => {
                if (cells[i]) {
                    const v = parseInt(hex, 16);
                    cells[i].style.backgroundColor = `rgb(${Math.round(((v>>11)&31)*255/31)},${Math.round(((v>>5)&63)*255/63)},${Math.round((v&31)*255/31)})`;
                }
            });
        }
    });

    window.setEditorMode(8, 8);
});
