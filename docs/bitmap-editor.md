<script src="../js/bitmap-editor.js"></script>

<div class="admonition info">
<p class="admonition-title">Bitmap Editor</p>
<div class="ehmtx-tool-container">
    <div class="upload-section" style="padding: 15px; cursor: default; margin-bottom: 20px;">
        <div style="display: flex; gap: 10px; justify-content: center; align-items: center; flex-wrap: wrap;">
            <div class="md-button md-button--primary" onclick="window.setEditorMode(32, 8)">32 x 8 Mode</div>
            <div class="md-button md-button--primary" onclick="window.setEditorMode(8, 8)">8 x 8 Mode</div>
            <input type="color" id="editorColorPicker" value="#F44336">
            <div class="md-button" onclick="window.clearEditor()" style="background-color: #ff5252; color: white; border: none;">Clear Canvas</div>
        </div>
    </div>

    <div class="converter-grid" style="display: block;">
        <div class="ehmtx-card" style="max-width: 100%; margin: 0 auto;">
            <div class="ehmtx-card-title">Drawing Canvas</div>
            <div class="preview-container-editor">
                <div id="pixelGrid" class="editor-grid-surface"></div>
            </div>

            <div class="ehmtx-card-title" style="margin-top: 20px;">RGB565 Code Array</div>
            <div class="code-wrapper" style="padding: 0;">
                <textarea id="editorOutput" spellcheck="false"></textarea>
            </div>
            <button class="md-button md-button--small copy-btn" onclick="window.copyEditorCode(this)">Copy Array</button>
        </div>
    </div>
</div>
</div>
