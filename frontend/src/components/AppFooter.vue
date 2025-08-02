<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <footer class="flex flex-col px-4 pt-20 pb-8 justify-between items-center gap-1 custom-bg">
    <p class="text-[14px]"> © 2025 Lazy Alien Server</p>
    <router-link to="/cookie-policy" class="link">This site uses cookies to enhance your experience. Learn more</router-link>
  </footer>
</template>
