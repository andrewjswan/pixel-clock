<link href="https://cdn.jsdelivr.net/npm/vuetify@2.6.10/dist/vuetify.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/@mdi/font@latest/css/materialdesignicons.min.css" rel="stylesheet">

<script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vuetify@2.6.10/dist/vuetify.min.js"></script>

<script src="../js/bitmap-editor.js"></script>

<div id="app" data-app="true">
  <v-app id="bitmap-app" class="v-application v-application--is-ltr theme--light">
    <v-main>
      <bitmap-editor></bitmap-editor>
    </v-main>
  </v-app>
</div>

<style>
  #app .v-application {
      font-family: inherit !important;
  }
  
  html, body {
      font-size: initial !important; 
  }

  #bitmap-app {
      background: transparent !important;
      min-height: auto !important;
  }
  .v-application--wrap {
      min-height: auto !important;
  }
  
  .v-application table {
      display: inline-table !important;
      border: none !important;
  }
  .v-application td, .v-application th {
      border: none !important;
      padding: 0 !important;
  }
</style>

<script>
  new Vue({
    el: '#app',
    vuetify: new Vuetify({
        theme: { disable: true },
    }),
  })
</script>
