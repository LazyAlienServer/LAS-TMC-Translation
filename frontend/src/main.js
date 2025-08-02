import { createApp } from 'vue'
import { createPinia } from "pinia";
import App from './App.vue'
import router from "@/router";
import "@/assets/css/app.css"
import { setupGlobalErrorHandler } from "@/utils";
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";


const app = createApp(App);

app.use(router);
app.use(createPinia());
app.use(Toast, {
    position: "top-center",
    timeout: 3500,
    closeOnClick: true,
})

setupGlobalErrorHandler(app);

app.mount('#app');
