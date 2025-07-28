<script setup>
import { computed, ref } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores";
import { logger } from "@/utils";


const router = useRouter();
const userStore = useUserStore();
const userInfo = computed(() => userStore.userInfo);
const avatarUrl = computed(() => import.meta.env.VITE_API_BASE_URL + userStore.userInfo.avatar)

function handleLogout() {
  // Handle Logout Request
  logger.info("User logout successfully")

  userStore.logout();

  router.push({ name: 'home' });
}
</script>

<template>
  <div v-if="userInfo" class="flex flex-col gap-y-6 self-center">
    <div class="flex justify-center">
      <img
          :src="avatarUrl"
          alt="User Avatar"
          class="w-24 h-24 rounded-full object-cover border border-gray-300"
      />
    </div>
    <p><b>Username: </b>{{ userInfo.username }}</p>
    <p><b>Email: </b>{{ userInfo.email }}</p>

    <button @click="handleLogout">
      Log Out
    </button>
  </div>
</template>

<style scoped>

</style>