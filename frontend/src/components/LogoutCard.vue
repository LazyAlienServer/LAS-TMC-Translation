<script setup>
import { computed } from "vue";
import { useUserStore } from "@/stores";
import { handleLogout } from "@/utils";
import { useRouter } from "vue-router";

const userStore = useUserStore();
const router = useRouter();
const userInfo = computed(() => userStore.userInfo);
const avatarUrl = computed(() => import.meta.env.VITE_API_BASE_URL + userStore.userInfo.avatar)

function onLogout() {
  handleLogout();
  router.push({name: "home"});
}
</script>

<template>
  <div v-if="userInfo" class="flex flex-col gap-y-6 self-center items-center">

    <h2>Are you sure?</h2>

    <div>
      <img
          :src="avatarUrl"
          alt="User Avatar"
          class="w-24 h-24 rounded-full object-cover border border-gray-300"
      />
    </div>

    <p><b>Username: </b>{{ userInfo.username }}</p>
    <p><b>Email: </b>{{ userInfo.email }}</p>

    <button @click="onLogout">Sign out</button>

  </div>
</template>
