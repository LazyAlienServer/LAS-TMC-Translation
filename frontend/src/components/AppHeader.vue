<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <header class="w-full flex items-center justify-between gap-6 px-6 py-4 shadow-md mb-10">
    <router-link :to="{name: 'home'}" class="flex items-center">
      <img src="@/assets/logo.svg" alt="logo" class="w-auto h-10" />
    </router-link>
    <div class="flex font-medium justify-end gap-10">
      <a href="https://lazyalienserver.top" target="_blank" rel="noopener" class="navbar-link">
        About Our Server ↗
      </a>
      <router-link :to="{name: 'contact'}" class="navbar-link">
        Contact Us
      </router-link>
      <router-link :to="{name: 'donate'}" class="navbar-link">
        Donate
      </router-link>
      <router-link :to="{name: 'profile', params: {username: 'typo'}}" class="navbar-link">
        Profile
      </router-link>
    </div>
  </header>
</template>

<style scoped>

</style>
