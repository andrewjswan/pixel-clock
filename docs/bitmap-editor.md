<script src="https://cdn.jsdelivr.net/npm/@jaames/iro@5"></script>
<script src="../js/bitmap-editor.js"></script>

<div class="admonition info">
<p class="admonition-title">Bitmap Editor</p>
<div class="ehmtx-tool-container">
    <div class="editor-layout">
        <div class="picker-sidebar">
            <div id="iroPicker"></div>
            <div class="color-inputs">
                <div class="input-group"><input type="number" id="input-r"><span>R</span></div>
                <div class="input-group"><input type="number" id="input-g"><span>G</span></div>
                <div class="input-group"><input type="number" id="input-b"><span>B</span></div>
            </div>
            <div class="md-button" onclick="window.clearEditor()" style="background-color: #ff5252; color: white; width: 100%; margin-top: 20px;">Clear Canvas</div>
        </div>
        <div class="canvas-area">
            <div class="md-button-group" style="margin-bottom: 15px;">
                <div class="md-button md-button--primary" onclick="window.setEditorMode(32, 8)">32 x 8 Mode</div>
                <div class="md-button md-button--primary" onclick="window.setEditorMode(8, 8)">8 x 8 Mode</div>
            </div>
            <div id="pixelGrid" class="editor-grid-surface"></div>
            <textarea id="editorOutput" spellcheck="false" style="margin-top:20px;"></textarea>
            <button class="md-button md-button--small" onclick="window.copyEditorCode(this)">Copy Array</button>
        </div>
    </div>
</div>
</div>
