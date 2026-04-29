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
        currentColor = color.hexString.toUpperCase();
        inR.value = color.rgb.r; inG.value = color.rgb.g; inB.value = color.rgb.b;
    });

    [inR, inG, inB].forEach(el => {
        el.addEventListener('input', () => {
            colorPicker.color.set({ r: inR.value, g: inG.value, b: inB.value });
        });
    });

    window.setEditorMode = (w, h) => {
        currentW = w; currentH = h;
        grid.style.gridTemplateColumns = `repeat(${w}, 18px)`;
        grid.innerHTML = '';
        for (let i = 0; i < w * h; i++) {
            const cell = document.createElement('div');
            cell.className = 'pixel-cell';
            cell.style.backgroundColor = 'rgb(0, 0, 0)';
            cell.addEventListener('mousedown', (e) => { isDrawing = true; handlePaint(e, true); });
            cell.addEventListener('mouseover', (e) => { if (isDrawing) handlePaint(e, false); });
            grid.appendChild(cell);
        }
        updateOutput();
    };

    function handlePaint(e, isClick) {
        const cell = e.target;
        const cellRgb = cell.style.backgroundColor.match(/\d+/g).map(Number);
        const cellHex = "#" + cellRgb.map(x => x.toString(16).padStart(2, '0')).join('').toUpperCase();

        if (isClick && cellHex === currentColor) {
            cell.style.backgroundColor = 'rgb(0, 0, 0)';
        } else {
            cell.style.backgroundColor = currentColor;
        }
        updateOutput();
    }

    window.addEventListener('mouseup', () => isDrawing = false);

    window.clearEditor = () => {
        document.querySelectorAll('.pixel-cell').forEach(c => c.style.backgroundColor = 'rgb(0, 0, 0)');
        updateOutput();
    };

    window.copyEditorCode = (btn) => {
        output.select(); document.execCommand('copy');
        const old = btn.textContent; btn.textContent = "✅ Copied!";
        setTimeout(() => { btn.textContent = old; }, 2000);
    };

    function updateOutput() {
        const cells = document.querySelectorAll('.pixel-cell');
        const rgb565 = Array.from(cells).map(c => {
            const rgb = c.style.backgroundColor.match(/\d+/g).map(Number);
            return ((rgb[0] >> 3) << 11) | ((rgb[1] >> 2) << 5) | (rgb[2] >> 3);
        });
        output.value = `[${rgb565.join(',')}]`;
    }

    output.addEventListener('input', () => {
        const rawValues = output.value.replace(/[\[\]\s]/g, '').split(',');
        const cells = document.querySelectorAll('.pixel-cell');
        rawValues.forEach((val, i) => {
            if (cells[i] && val !== "") {
                const v = parseInt(val);
                cells[i].style.backgroundColor = `rgb(${Math.round(((v >> 11) & 31) * 255 / 31)},${Math.round(((v >> 5) & 63) * 255 / 63)},${Math.round((v & 31) * 255 / 31)})`;
            }
        });
    });

    window.setEditorMode(8, 8);
});
