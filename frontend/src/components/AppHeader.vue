<script setup>
import { ref, computed } from "vue";
import { RouterLink } from "vue-router";
import { useUserStore } from "@/stores";

const userStore = useUserStore();
const userInfo = computed(() => userStore.userInfo);
const avatarUrl = computed(() => import.meta.env.VITE_API_BASE_URL + userStore.userInfo.avatar)

const isSidebarOpen = ref(false);
function toggleSidebar() {
  isSidebarOpen.value = !isSidebarOpen.value;
}
</script>

<template>
  <header class="fixed top-0 left-0 z-50 w-full flex flex-row items-center justify-between gap-6 px-10 py-4 shadow-md custom-bg">
    <div class="flex flex-row items-center gap-8">
      <router-link :to="{ name: 'home' }">
        <img src="@/assets/logo.svg" alt="logo" class="w-auto h-10" />
      </router-link>

      <a href="https://lazyalienserver.top/" target="_blank" rel="noopener" class="w-13">
        <img src="@/assets/las.svg" alt="logo" />
      </a>
    </div>

    <div class="flex font-medium items-center justify-center gap-3">

      <a href="https://www.youtube.com/@redstonevideotranslation5478" target="_blank" rel="noopener" class="header-icon">
        <img src="@/assets/icons/youtube-black.svg" alt="logo" class="w-6 h-6" />
      </a>

      <a href="https://github.com/LazyAlienServer" target="_blank" rel="noopener" class="header-icon">
        <img src="@/assets/icons/mark-github-16.svg" alt="logo" class="w-6 h-6" />
      </a>

      <img
          v-if="userInfo"
          :src="avatarUrl"
          alt="User Avatar"
          class="w-10 h-10 rounded-full object-cover border-2 border-gray-400 ml-4"
          @click="toggleSidebar"
      />

      <img
          v-else
          src="@/assets/icons/person-fill-16.svg"
          alt="logo"
          class="header-icon ml-4 w-10 h-10"
          @click="toggleSidebar"
      />

    </div>

    <!-- Mask -->
    <div
        v-if="isSidebarOpen"
        class="fixed inset-0 z-40 bg-gray-100 opacity-50"
        @click="toggleSidebar"
    >
    </div>

    <!-- Side Bar -->
    <div
        class="fixed top-0 right-0 z-50 h-full w-80 rounded-l-3xl bg-white shadow-lg transform transition-transform duration-300"
        :class="isSidebarOpen ? 'translate-x-0' : 'translate-x-full'"
    >
      <!-- If user has login -->
      <div v-if="userInfo">
        <div class="absolute top-0 right-0 mt-8 mr-9 p-1 rounded-md hover:cursor-pointer hover:bg-gray-200 " @click="toggleSidebar">
          <img src="@/assets/icons/x-16.svg" alt="logo" />
        </div>

        <div class="flex flex-col gap-5 p-6">
          <div class="flex flex-row items-center gap-2">
            <img
                :src="avatarUrl"
                alt="User Avatar"
                class="w-10 h-10 rounded-full object-cover border-2 border-gray-400"
            />
            <p
                class="text-[15px] font-bold"
            >{{ userInfo.username }}
            </p>
          </div>

          <hr>

          <ul class="space-y-3">
            <li>
              <router-link to="/profile" class="header-sidebar-link" @click="toggleSidebar">
                <img src="@/assets/icons/person-16.svg" alt="logo" />
                Your Profile
              </router-link>
              <router-link to="/settings" class="header-sidebar-link" @click="toggleSidebar">
                <img src="@/assets/icons/gear-16.svg" alt="logo" />
                Your Settings
              </router-link>
              <router-link to="/bookmarks" class="header-sidebar-link" @click="toggleSidebar">
                <img src="@/assets/icons/bookmark-16.svg" alt="logo" />
                Your Bookmarks
              </router-link>
            </li>

            <hr>

            <li>
              <router-link to="/logout" class="header-sidebar-link" @click="toggleSidebar">
                <img src="@/assets/icons/sign-out-16.svg" alt="logo" />
                Sign Out
              </router-link>
            </li>
          </ul>
        </div>
      </div>

      <!--If user has not login-->
      <div v-else>
        <div class="flex flex-col gap-5 p-6">
          <div class="flex flex-row items-center gap-2">
            <img
                src="@/assets/icons/person-fill-24.svg"
                alt="Anonymous User Logo"
            />
            <p class="text-[15px] font-bold">Anonymous User</p>
          </div>

          <hr>

          <ul class="space-y-3">
            <li>
              <router-link to="/login" class="header-sidebar-link" @click="toggleSidebar">
                <img src="@/assets/icons/sign-in-16.svg" alt="logo" />
                Sign In
              </router-link>
            </li>
          </ul>

        </div>

      </div>

    </div>

  </header>
</template>

