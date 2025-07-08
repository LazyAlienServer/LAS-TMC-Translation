<script setup>
import AppHeader from "@/components/AppHeader.vue";
</script>

<template>
  <div class="min-h-screen bg-gradient-to-br from-purple-300 to-pink-200 backdrop-blur-sm bg-opacity-70 text-gray-900">
    <AppHeader />
    <router-view />
  </div>
</template>

<style>
</style>
