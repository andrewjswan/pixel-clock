## Bitmap Converter

A tool for converting images to the RGB565 format.

<div class="ehmtx-tool-container">
    <header class="ehmtx-header">
        <p class="subtitle">Convert images to RGB565 arrays</p>
    </header>

    <div class="upload-section" id="dropZone">
        <span class="upload-icon">🖼️</span>
        <p>Drag and drop your image here, or click to browse</p>
        <span class="btn-upload">Select Image</span>
        <input type="file" id="fileInput" accept="image/*">
    </div>

    <div class="results-grid" id="results" style="display: none;">
        <!-- 32x8 Card -->
        <div class="ehmtx-card">
            <h2>32 x 8 <small>Full Screen</small></h2>
            <div class="preview-container preview-32x8">
                <img id="img32x8" class="scaled-image" alt="32x8 preview">
            </div>
            <div class="code-block">
                <pre id="code32x8"></pre>
            </div>
            <button class="copy-btn" onclick="copyCode('code32x8', this)">
                <span>📋 Copy Array</span>
            </button>
        </div>

        <!-- 8x8 Card -->
        <div class="ehmtx-card">
            <h2>8 x 8 <small>Icon / Small Bitmap</small></h2>
            <div class="preview-container preview-8x8">
                <img id="img8x8" class="scaled-image" alt="8x8 preview">
            </div>
            <div class="code-block">
                <pre id="code8x8"></pre>
            </div>
            <button class="copy-btn" onclick="copyCode('code8x8', this)">
                <span>📋 Copy Array</span>
            </button>
        </div>
    </div>
</div>

<div id="toast">Copied to clipboard!</div>
<canvas id="hiddenCanvas" style="display:none;"></canvas>
