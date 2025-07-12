<script setup>
import {
  AppHeader,
  AppFooter,
} from "@/components";
</script>

<template>
  <div class="flex flex-col min-h-screen font-sans text-[#111827]">
    <AppHeader />
    <main class="flex-1 px-10 pt-30 custom-bg">
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<style>
</style>
