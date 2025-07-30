<script setup>
import { computed } from "vue";
import { useUserStore } from "@/stores";


const userStore = useUserStore();
const userInfo = computed(() => userStore.userInfo);
const avatarUrl = computed(() => import.meta.env.VITE_API_BASE_URL + userStore.userInfo.avatar)
</script>

<template>
  <div v-if="userInfo" class="flex flex-col gap-y-6 self-center items-center border border-gray-500 w-100 h-150 rounded-[20px]">

    <div>
      <img
          :src="avatarUrl"
          alt="User Avatar"
          class="w-50 h-50 rounded-full object-cover border border-gray-300"
      />
    </div>

    <p><b>Username: </b>{{ userInfo.username }}</p>
    <p><b>Email: </b>{{ userInfo.email }}</p>

  </div>
</template>