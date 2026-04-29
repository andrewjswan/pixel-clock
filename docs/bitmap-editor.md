<script src="https://cdn.jsdelivr.net/npm/@jaames/iro@5"></script>
<script src="../js/bitmap-editor.js"></script>

<div class="admonition info">
<p class="admonition-title">Bitmap Editor</p>
<div class="ehmtx-tool-container">
    
    <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap; margin-bottom: 20px; justify-content: center;">
        <button class="md-button md-button--primary" onclick="window.setEditorMode(8, 8)">8 x 8</button>
        <button class="md-button md-button--primary" onclick="window.setEditorMode(32, 8)">32 x 8</button>
        <button class="md-button" onclick="window.clearEditor()" style="background-color: #ff5252; color: white; border: none;">Clear</button>
        <input type="color" id="editorColorPicker" value="#F44336" style="width: 60px; height: 32px; border: 2px solid #fff; border-radius: 4px; cursor: pointer; padding: 0;">
    </div>

    <div class="editor-layout" style="display: flex; gap: 20px; flex-wrap: wrap; justify-content: center;">
        <div class="picker-sidebar">
            <div id="iroPicker"></div>
            <div class="color-inputs" style="display: flex; gap: 5px; margin-top: 10px;">
                <div class="input-group"><input type="number" id="input-r" style="width: 45px;"><span style="font-size: 10px;">R</span></div>
                <div class="input-group"><input type="number" id="input-g" style="width: 45px;"><span style="font-size: 10px;">G</span></div>
                <div class="input-group"><input type="number" id="input-b" style="width: 45px;"><span style="font-size: 10px;">B</span></div>
            </div>
        </div>

        <div style="flex: 1; min-width: 300px;">
            <div style="background: #111; padding: 15px; border-radius: 4px; display: flex; justify-content: center; overflow-x: auto;">
                <div id="pixelGrid" class="editor-grid-surface"></div>
            </div>
            
            <p style="margin: 15px 0 5px 0; font-weight: bold; font-size: 0.8em;">Output Array:</p>
            <textarea id="editorOutput" spellcheck="false" style="width: 100%; height: 80px; background: #222; color: #ccc; border: 1px solid #444; padding: 10px; font-family: monospace; font-size: 12px; resize: none; overflow: hidden;"></textarea>
            
            <button class="md-button md-button--small" onclick="window.copyEditorCode(this)" style="width: 100%; margin-top: 10px;">Copy Array</button>
        </div>
    </div>
</div>
</div>
