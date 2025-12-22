<script setup>
import { useUserStore } from "@/stores";
import { RouterLink } from "vue-router";

const userStore = useUserStore();

</script>

<template>
  <div class="flex flex-col gap-y-3">
    <h2>Hello, {{ userStore.userInfo.username }}!</h2>
    <router-link :to="`/pending-articles`">
      Moderate Articles
    </router-link>
  </div>
</template>
