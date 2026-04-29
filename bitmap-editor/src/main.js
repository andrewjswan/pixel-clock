import Vue from 'vue'
import Vuetify from 'vuetify'
import Creator from './views/Creator.vue'

Vue.use(Vuetify)

Vue.component('bitmap-editor', Creator)

export default Creator
