<script setup>
import { computed } from "vue"
import { RouterLink } from "vue-router";
import { useUserStore } from "@/stores";

const userStore = useUserStore();
const userInfo = computed(() => userStore.userInfo);
</script>

<template>
  <header class="fixed top-0 left-0 z-50 w-full flex flex-row items-center justify-between gap-6 px-10 py-4 shadow-md custom-bg">
    <router-link :to="{ name: 'home' }" class="flex items-center">
      <img src="@/assets/logo.svg" alt="logo" class="w-auto h-10" />
    </router-link>
    <div class="flex font-medium justify-end gap-10">

      <router-link
          v-if="userInfo"
          :to="{ name: 'profile'}"
          class="link"
      >
        Profile
      </router-link>
      <router-link
          v-else
          :to="{ name: 'login' }"
          class="link"
      >
        Login
      </router-link>

      <a href="https://lazyalienserver.top" target="_blank" rel="noopener" class="link">
        About Our Server
      </a>

      <router-link :to="{ name: 'contact' }" class="link">
        Contact Us
      </router-link>

    </div>
  </header>
</template>
<style scoped>

</style>
