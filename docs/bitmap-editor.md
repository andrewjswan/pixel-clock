<script src="https://cdn.jsdelivr.net/npm/@jaames/iro@5"></script>
<script src="../js/bitmap-editor.js"></script>

<div class="admonition info">
<p class="admonition-title">Bitmap Editor</p>
<div class="ehmtx-tool-container">
    <div class="editor-layout">
        <div class="picker-sidebar">
            <div id="iroPicker"></div>
            
            <div class="color-inputs" style="display: flex; gap: 5px;">
                <div class="input-group"><input type="number" id="input-r"><span>R</span></div>
                <div class="input-group"><input type="number" id="input-g"><span>G</span></div>
                <div class="input-group"><input type="number" id="input-b"><span>B</span></div>
            </div>

            <div style="display: flex; gap: 5px; width: 100%; margin-top: 10px;">
                <button class="md-button md-button--primary" style="flex: 1; padding: 0;" onclick="window.setEditorMode(8, 8)">8x8</button>
                <button class="md-button md-button--primary" style="flex: 1; padding: 0;" onclick="window.setEditorMode(32, 8)">32x8</button>
            </div>
            <button class="md-button" onclick="window.clearEditor()" style="background-color: #ff5252; color: white; border: none; width: 100%; height: 32px;">Clear Canvas</button>
        </div>

        <div style="flex: 1; min-width: 300px;">
            <div class="preview-container-editor">
                <div id="pixelGrid" class="editor-grid-surface"></div>
            </div>
            
            <p style="margin: 10px 0 5px 0; font-weight: bold; font-size: 0.8em;">Output Array:</p>
            <textarea id="editorOutput" spellcheck="false"></textarea>
            
            <div style="display: flex; gap: 10px; margin-top: 10px;">
                <button class="md-button md-button--small" onclick="window.copyEditorCode(this)" style="flex: 1; border: 1px solid #3f51b5; background: transparent; color: #3f51b5;">Copy Array</button>
            </div>
        </div>
    </div>
</div>
</div>
