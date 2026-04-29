<link href="https://cdn.jsdelivr.net/npm/vuetify@2.6.10/dist/vuetify.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/@mdi/font@latest/css/materialdesignicons.min.css" rel="stylesheet">

<script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vuetify@2.6.10/dist/vuetify.min.js"></script>

<script src="../js/bitmap-editor.js"></script>

<div id="app">
  <v-app id="bitmap-app" class="v-application">
    <v-main>
      <v-container>
        <bitmap-editor></bitmap-editor>
      </v-container>
    </v-main>
  </v-app>
</div>

<style>
  .v-application {
      font-family: Roboto, sans-serif !important;
      line-height: 1.5 !important;
  }
  .v-application--wrap {
      min-height: auto !important;
      display: block !important;
  }
  #bitmap-app {
      background-color: transparent !important;
  }
  .v-btn {
      height: auto !important;
      letter-spacing: normal !important;
      text-transform: none !important;
  }
  .v-application table {
      display: table !important;
      margin: 0 !important;
      word-break: normal !important;
  }
</style>

<script>
  window.addEventListener('load', function () {
    new Vue({
      el: '#app',
      vuetify: new Vuetify({
          theme: { dark: false }
      }),
    })
  })
</script>
