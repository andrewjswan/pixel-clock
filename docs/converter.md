<script src="../js/converter.js"></script>

## Bitmap Converter

Convert any image to RGB565 arrays for your LED matrix displays.

<div class="admonition info">
<p class="admonition-title">Image Converter</p>
<div class="ehmtx-tool-container">
    <div class="upload-section" id="dropZone">
        <span class="upload-icon">🖼️</span>
        <p>Drag and drop image here, or click to browse</p>
        <div class="md-button md-button--primary">Select Image</div>
        <input type="file" id="fileInput" accept="image/*" style="display:none">
    </div>

    <div id="results" style="display: none;">
        <div class="converter-grid">
            <div class="ehmtx-card">
                <div class="ehmtx-card-title">32 x 8 <small>(Full Screen)</small></div>
                <div class="preview-container">
                    <img id="img32x8" class="scaled-image preview-32x8" alt="">
                </div>
                <div class="code-wrapper">
                    <pre id="code32x8"></pre>
                </div>
                <button class="md-button md-button--small copy-btn" onclick="window.copyCode('code32x8', this)">Copy Array</button>
            </div>

            <div class="ehmtx-card">
                <div class="ehmtx-card-title">8 x 8 <small>(Icon)</small></div>
                <div class="preview-container">
                    <img id="img8x8" class="scaled-image preview-8x8" alt="">
                </div>
                <div class="code-wrapper">
                    <pre id="code8x8"></pre>
                </div>
                <button class="md-button md-button--small copy-btn" onclick="window.copyCode('code8x8', this)">Copy Array</button>
            </div>
        </div>
    </div>
</div>
</div>

<div id="toast">Copied to clipboard!</div>
<canvas id="hiddenCanvas" style="display:none;"></canvas>
