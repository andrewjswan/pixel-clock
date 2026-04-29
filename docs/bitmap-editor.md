<script src="https://cdn.jsdelivr.net/npm/@jaames/iro@5"></script>
<script src="../js/bitmap-editor.js"></script>

<div class="admonition info">
<p class="admonition-title">Bitmap Editor</p>
<div class="ehmtx-tool-container">
    
    <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 20px; justify-content: center;">
        <button class="md-button md-button--primary" onclick="window.setEditorMode(8, 8)">8 x 8</button>
        <button class="md-button md-button--primary" onclick="window.setEditorMode(32, 8)">32 x 8</button>
        <button class="md-button" onclick="window.clearEditor()" style="background-color: #ff5252; color: white; border: none;">Clear</button>
    </div>

    <div class="editor-layout" style="display: flex; gap: 15px; flex-wrap: wrap; justify-content: center; flex-direction: row-reverse;">
        <div class="picker-sidebar">
            <div id="iroPicker"></div>
            <div class="color-inputs">
                <div class="input-group">
                    <input type="number" id="input-r" value="0">
                    <span>R</span>
                </div>
                <div class="input-group">
                    <input type="number" id="input-g" value="0">
                    <span>G</span>
                </div>
                <div class="input-group">
                    <input type="number" id="input-b" value="0">
                    <span>B</span>
                </div>
            </div>
        </div>

        <div style="flex: 1; min-width: 300px;">
            <div style="background: #111; padding: 20px; border-radius: 4px; display: flex; justify-content: center; overflow-x: auto; border: 1px solid #333;">
                <div id="pixelGrid" class="editor-grid-surface"></div>
            </div>
            
            <p style="margin: 15px 0 5px 0; font-weight: bold; font-size: 0.8em; color: #666;">Output Array:</p>
            <textarea id="editorOutput" spellcheck="false" style="width: 100%; height: 90px; background: #1e1e1e; color: #ccc; border: 1px solid #333; padding: 12px; font-family: 'Roboto Mono', monospace; font-size: 11px; resize: none; border-radius: 4px;"></textarea>
            
            <button class="md-button md-button--small" onclick="window.copyEditorCode(this)" style="width: 100%; margin-top: 10px; border: 1px solid #3f51b5; background: transparent; color: #3f51b5;">Copy Array</button>
        </div>
    </div>
</div>
</div>
