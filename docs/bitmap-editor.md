## Bitmap editor

<script src="../js/bitmap-editor.js"></script>

<div id="app">
  <v-app id="bitmap-app">
    <v-main>
      <bitmap-editor></bitmap-editor>
    </v-main>
  </v-app>
</div>

<style>
  #bitmap-app { background-color: transparent !important; }
  .v-application--wrap { min-height: auto !important; }
</style>

<script>
  window.addEventListener('load', function () {
    new Vue({
      el: '#app',
      vuetify: new Vuetify(),
    })
  })
</script>
