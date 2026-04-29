<script src="../js/bitmap-editor.js"></script>

Create and edit custom bitmaps for your LED matrix displays.

<div class="admonition info">
<p class="admonition-title">Bitmap Editor</p>
<div class="ehmtx-tool-container">
    <div class="upload-section" style="padding: 15px; cursor: default; margin-bottom: 20px;">
        <div style="display: flex; gap: 10px; justify-content: center; align-items: center; flex-wrap: wrap;">
            <div class="md-button md-button--primary" onclick="window.setEditorMode(32, 8)">32 x 8 Mode</div>
            <div class="md-button md-button--primary" onclick="window.setEditorMode(8, 8)">8 x 8 Mode</div>
            <input type="color" id="editorColorPicker" value="#F44336" style="height: 38px; width: 60px; border: 2px solid #fff; border-radius: 4px; cursor: pointer;">
            <div class="md-button" onclick="window.clearEditor()" style="background-color: #ff5252; color: white; border: none;">Clear Canvas</div>
        </div>
    </div>

    <div class="converter-grid" style="display: block;">
        <div class="ehmtx-card" style="max-width: 100%; margin: 0 auto;">
            <div class="ehmtx-card-title">Drawing Canvas</div>
            
            <div class="preview-container" style="background: #111; padding: 20px; display: flex; justify-content: center; overflow-x: auto;">
                <div id="pixelGrid" class="editor-grid-surface"></div>
            </div>

            <div class="ehmtx-card-title" style="margin-top: 20px;">RGB565 Code Array</div>
            <div class="code-wrapper">
                <pre id="editorOutput"></pre>
            </div>

            <button class="md-button md-button--small copy-btn" onclick="window.copyCode('editorOutput', this)">Copy Array</button>
        </div>
    </div>
</div>
</div>

<style>
    .editor-grid-surface {
        display: grid;
        gap: 1px;
        background: #333;
        border: 2px solid #333;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    .pixel-cell {
        width: 22px;
        height: 22px;
        cursor: crosshair;
    }
    .pixel-cell:hover {
        filter: brightness(1.4);
        outline: 1px solid #fff;
        z-index: 2;
    }
    #editorOutput {
        color: #e6db74;
        font-size: 0.85em;
    }
</style>
