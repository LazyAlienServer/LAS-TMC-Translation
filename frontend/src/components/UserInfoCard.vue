<script setup>
import { computed } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores";
import { logger } from "@/utils";


const router = useRouter();
const userStore = useUserStore();
const userInfo = computed(() => userStore.userInfo);

function handleLogout() {
  // Handle Logout Request
  logger.info("User logout successfully")

  userStore.logout();

  router.push({ name: 'home' });
}
</script>

<template>
  <div v-if="userInfo" class="flex flex-col gap-y-6 self-center">
    <p><b>Username: </b>{{ userInfo.username }}</p>
    <p><b>Email: </b>{{ userInfo.email }}</p>

    <button @click="handleLogout">
      Log Out
    </button>
  </div>
</template>

<style scoped>

</style>