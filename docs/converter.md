## Bitmap Converter

A tool for converting images to the RGB565 format.

!!! info "Upload Image"
    <div class="upload-section" id="dropZone">
        <span class="upload-icon">🖼️</span>
        <p>Drag and drop image here, or click to browse</p>
        <label for="fileInput" class="md-button md-button--primary">Select Image</label>
        <input type="file" id="fileInput" accept="image/*" style="display:none">
    </div>

<div class="results-grid" id="results" style="display: none;">
  <div class="grid cards" markdown>

-   ### 32 x 8 (Full Screen)
    <div class="preview-container preview-32x8">
        <img id="img32x8" class="scaled-image" alt="32x8 preview">
    </div>
    <div class="code-wrapper">
        <pre id="code32x8"></pre>
    </div>
    <button class="md-button copy-btn" onclick="copyCode('code32x8', this)">Copy Array</button>

-   ### 8 x 8 (Icon)
    <div class="preview-container preview-8x8">
        <img id="img8x8" class="scaled-image" alt="8x8 preview">
    </div>
    <div class="code-wrapper">
        <pre id="code8x8"></pre>
    </div>
    <button class="md-button copy-btn" onclick="copyCode('code8x8', this)">Copy Array</button>

  </div>
</div>

<div id="toast">Copied to clipboard!</div>
<canvas id="hiddenCanvas" style="display:none;"></canvas>
