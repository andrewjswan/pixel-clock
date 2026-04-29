<div class="editor-container">
    <div class="controls">
        <button onclick="setMode(8)">8x8</button>
        <button onclick="setMode(32, 8)">8x32</button>
        <input type="color" id="colorPicker" value="#ff4433">
    </div>
    
    <div id="pixelCanvas" class="canvas-grid"></div>
    
    <textarea id="outputCode" readonly placeholder="RGB565 Array"></textarea>
    <button onclick="copyCode()" class="copy-btn">Copy</button>
</div>

<style>
    .editor-container { display: flex; flex-direction: column; gap: 15px; max-width: 600px; margin: 20px 0; }
    .controls { display: flex; gap: 10px; align-items: center; }
    .canvas-grid { 
        display: grid; 
        gap: 1px; 
        background: #444; 
        border: 1px solid #444; 
        width: fit-content;
    }
    .pixel { width: 25px; height: 25px; background: #000; cursor: crosshair; }
    .pixel:hover { filter: brightness(1.5); }
    #outputCode { width: 100%; height: 100px; font-family: monospace; font-size: 12px; margin-top: 10px; padding: 10px; border-radius: 4px; }
    button { padding: 8px 15px; cursor: pointer; background: #2196F3; color: white; border: none; border-radius: 4px; }
    button:hover { background: #1976D2; }
    input[type="color"] { width: 50px; height: 35px; border: none; cursor: pointer; }
</style>

<script>
    let currentWidth = 8;
    let currentHeight = 8;
    const canvas = document.getElementById('pixelCanvas');
    const output = document.getElementById('outputCode');
    const colorPicker = document.getElementById('colorPicker');

    function setMode(w, h = 8) {
        currentWidth = w;
        currentHeight = h;
        initCanvas();
    }

    function initCanvas() {
        canvas.style.gridTemplateColumns = `repeat(${currentWidth}, 1fr)`;
        canvas.innerHTML = '';
        for (let i = 0; i < currentWidth * currentHeight; i++) {
            const div = document.createElement('div');
            div.className = 'pixel';
            div.dataset.index = i;
            div.style.backgroundColor = '#000000';
            div.onmousedown = (e) => { paint(e); };
            div.onmouseover = (e) => { if(e.buttons === 1) paint(e); };
            canvas.appendChild(div);
        }
        updateCode();
    }

    function paint(e) {
        e.target.style.backgroundColor = colorPicker.value;
        updateCode();
    }

    function hexToRgb565(hex) {
        const r = parseInt(hex.slice(1, 3), 16);
        const g = parseInt(hex.slice(3, 5), 16);
        const b = parseInt(hex.slice(5, 7), 16);
        return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3);
    }

    function updateCode() {
        const pixels = document.querySelectorAll('.pixel');
        const code = Array.from(pixels).map(p => {
            const rgb = p.style.backgroundColor;
            const hex = "#" + p.style.backgroundColor.match(/\d+/g).map(x => parseInt(x).toString(16).padStart(2, '0')).join('');
            return hexToRgb565(hex);
        });
        output.value = '[' + code.join(',') + ']';
    }

    function copyCode() {
        output.select();
        document.execCommand('copy');
        alert('Copied to the clipboard!');
    }

    initCanvas();
</script>
