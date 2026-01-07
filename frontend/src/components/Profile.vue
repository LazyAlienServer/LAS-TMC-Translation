<script setup>
import { useUserStore } from "@/stores";
import { RouterLink } from "vue-router";
import { computed } from 'vue'

const userStore = useUserStore();
const userInfo = computed(() => userStore.userInfo);
</script>

<template>
  <div class="flex flex-col gap-y-3">

    <h2>Hello, {{ userInfo?.username }}!</h2>

    <router-link
        :to="{ name: 'pending-articles' }"
        v-if="userInfo?.is_moderator"
        class="link text-[20px] font-semibold"
    >
      Moderate Articles
    </router-link>

  </div>
</template>
