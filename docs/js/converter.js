document.addEventListener("DOMContentLoaded", () => {
    const fileInput = document.getElementById('fileInput');
    const dropZone = document.getElementById('dropZone');
    const results = document.getElementById('results');
    const toast = document.getElementById('toast');
    const canvas = document.getElementById('hiddenCanvas');
    const ctx = canvas.getContext('2d', { willReadFrequently: true });

    dropZone.addEventListener('click', () => fileInput.click());

    ['dragover', 'dragleave', 'drop'].forEach(evt => {
        dropZone.addEventListener(evt, e => {
            e.preventDefault();
            e.stopPropagation();
        });
    });

    dropZone.addEventListener('dragover', () => dropZone.classList.add('dragover'));
    dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
    dropZone.addEventListener('drop', (e) => {
        dropZone.classList.remove('dragover');
        handleFile(e.dataTransfer.files[0]);
    });

    fileInput.addEventListener('change', (e) => handleFile(e.target.files[0]));

    function handleFile(file) {
        if (!file || !file.type.startsWith('image/')) return;

        const reader = new FileReader();
        reader.onload = (e) => {
            const img = new Image();
            img.onload = () => {
                processImage(img, 32, 8, 'img32x8', 'code32x8');
                processImage(img, 8, 8, 'img8x8', 'code8x8');
                results.style.display = 'block';
            };
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }

    function processImage(img, targetW, targetH, imgId, codeId) {
        canvas.width = targetW;
        canvas.height = targetH;
        
        ctx.clearRect(0, 0, targetW, targetH);
        ctx.drawImage(img, 0, 0, targetW, targetH);

        document.getElementById(imgId).src = canvas.toDataURL();

        const imageData = ctx.getImageData(0, 0, targetW, targetH).data;
        let rgb565Array = [];

        for (let i = 0; i < imageData.length; i += 4) {
            const r = imageData[i];
            const g = imageData[i + 1];
            const b = imageData[i + 2];

            const r5 = (r >> 3) & 0x1F;
            const g6 = (g >> 2) & 0x3F;
            const b5 = (b >> 3) & 0x1F;

            const rgb565 = (r5 << 11) | (g6 << 5) | b5;
            
            rgb565Array.push(`0x${rgb565.toString(16).toUpperCase().padStart(4, '0')}`);
        }

        const formattedCode = `const uint16_t bitmap_${targetW}x${targetH}[] = {\n    ${rgb565Array.join(', ')}\n};`;
        document.getElementById(codeId).textContent = formattedCode;
    }

    window.copyCode = (elementId, btn) => {
        const text = document.getElementById(elementId).textContent;
        navigator.clipboard.writeText(text).then(() => {
            const originalText = btn.textContent;
            btn.textContent = "✅ Copied!";
            btn.classList.add('md-button--primary');
            
            setTimeout(() => {
                btn.textContent = originalText;
                btn.classList.remove('md-button--primary');
            }, 2000);
        });
    };

});
