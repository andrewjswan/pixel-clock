## Bitmap editor

<link href="https://cdn.jsdelivr.net/npm/vuetify@2.6.10/dist/vuetify.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/@mdi/font@latest/css/materialdesignicons.min.css" rel="stylesheet">

<script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vuetify@2.6.10/dist/vuetify.min.js"></script>

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
