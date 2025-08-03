<script setup>
import { AppHeader, AppFooter } from "@/components";
</script>

<template>
  <div class="flex flex-col min-h-screen font-sans text-light dark:text-dark backgrounds-auto">
    <AppHeader />
    <main class="flex-1 pt-30">
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<style>
</style>
