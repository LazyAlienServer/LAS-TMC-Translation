import { createApp } from 'vue'
import { createPinia } from "pinia";
import App from './App.vue'
import router from "@/router";
import "@/assets/css/app.css"
import { setupGlobalErrorHandler } from "@/utils";


const app = createApp(App);

app.use(router);
app.use(createPinia());

setupGlobalErrorHandler(app);

app.mount('#app');
