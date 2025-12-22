<script setup>
import { ref, computed } from "vue";
import { RouterLink, useRouter } from "vue-router";
import { useUserStore, useThemeStore } from "@/stores";
import {
    YouTubeBlackIcon,
    GithubIcon,
    SunIcon,
    XIcon,
    PersonIcon,
    PersonIconFillLarge,
    GearIcon,
    BookmarkIcon,
    SignInIcon,
    SignOutIcon,
    RocketIcon,
    PlusIcon,
    BookIcon,
} from "@/assets/icons";
import { WebsiteIcon, LasLogo } from "@/assets";

import { useToast } from "vue-toastification";
import { useArticleStore } from "@/stores"

const articleStore = useArticleStore();
const toast = useToast();
const router = useRouter();
const userStore = useUserStore();
const themeStore = useThemeStore();
const userInfo = computed(() => userStore.userInfo);
const avatarUrl = computed(() => import.meta.env.VITE_API_BASE_URL + userStore.userInfo.avatar)

const isSidebarOpen = ref(false);
function toggleSidebar() {
  isSidebarOpen.value = !isSidebarOpen.value;
}

function toggleTheme() {
  themeStore.toggleTheme();
}

const loading = ref(false)

async function createArticle() {
  loading.value = true
  try {
    const response = await articleStore.create()
    const id = response.data.id
    console.log("Article successfully created!")
    await router.push({
      name: "article-editor",
      params: { id }
    })
  } catch (error) {
    toast.error(error.response?.data?.toast_error);
    console.error("Failed to create a new article", error)
  } finally {
    loading.value = false
  }
}

</script>

<template>
  <header class="fixed top-0 left-0 z-50 w-full flex flex-row items-center justify-between gap-6 px-10 py-4 shadow-md backgrounds-auto no-select">
    <div class="flex flex-row items-center gap-9">
      <router-link :to="{ name: 'home' }">
        <WebsiteIcon class="w-auto h-10"/>
      </router-link>

      <a href="https://lazyalienserver.top/" target="_blank" rel="noopener" class="w-13">
        <LasLogo />
      </a>
    </div>

    <div class="flex font-medium items-center gap-3">

      <div @click="createArticle" class="header-icon flex flex-row gap-x-1 font-semibold">
        <PlusIcon class="w-6 h-6 fill-current" /> Create
      </div>

      <a href="https://www.youtube.com/@redstonevideotranslation5478" target="_blank" rel="noopener" class="header-icon">
        <YouTubeBlackIcon class="w-6 h-6 fill-current" />
      </a>

      <a href="https://github.com/LazyAlienServer" target="_blank" rel="noopener" class="header-icon">
        <GithubIcon class="w-6 h-6 fill-current" />
      </a>

      <div @click="toggleTheme" class="header-icon">
        <SunIcon class="w-6 h-6 fill-current" />
      </div>

      <img
          v-if="userInfo"
          :src="avatarUrl"
          alt="User Avatar"
          class="w-10 h-10 rounded-full object-cover ml-4 border border-gray-300"
          @click="toggleSidebar"
      />

      <div v-else class="header-icon">
        <PersonIconFillLarge class="w-6 h-6 fill-current" @click="toggleSidebar" />
      </div>

    </div>

    <!-- Mask -->
    <div
        v-if="isSidebarOpen"
        class="fixed inset-0 z-40 bg-gray-200 opacity-50"
        @click="toggleSidebar"
    >
    </div>

    <!-- Side Bar -->
    <div
        class="fixed top-0 right-0 z-50 h-full w-80 rounded-l-3xl shadow-lg transform transition-transform duration-300 backgrounds-auto"
        :class="isSidebarOpen ? 'translate-x-0' : 'translate-x-full'"
    >
      <!-- If user has signed in -->
      <div v-if="userInfo">
        <div class="absolute top-0 right-0 mt-8 mr-9 p-1 rounded-md hover:cursor-pointer hover:bg-gray-200 dark:hover:bg-[#2C2C2C]" @click="toggleSidebar">
          <XIcon class="sidebar-icon"/>
        </div>

        <div class="flex flex-col gap-4 p-6">
          <div class="flex flex-row items-center gap-3">
            <img
                :src="avatarUrl"
                alt="User Avatar"
                class="w-10 h-10 rounded-full object-cover border border-gray-300"
            />
            <p
                class="text-[15px] font-bold"
            >{{ userInfo.username }}
            </p>
          </div>

          <hr>

          <ul class="gap-y-3">
            <li>
              <router-link to="/profile" class="sidebar-link" @click="toggleSidebar">
                <PersonIcon class="sidebar-icon" />
                Your Profile
              </router-link>
              <router-link to="/my-articles" class="sidebar-link" @click="toggleSidebar">
                <BookIcon class="sidebar-icon" />
                Your Articles
              </router-link>
              <router-link to="/settings/appearance" class="sidebar-link" @click="toggleSidebar">
                <GearIcon class="sidebar-icon" />
                Your Settings
              </router-link>
              <router-link to="/bookmarks" class="sidebar-link" @click="toggleSidebar">
                <BookmarkIcon class="sidebar-icon" />
                Your Bookmarks
              </router-link>
            </li>

            <hr class="my-3">

            <li>
              <router-link to="/logout" class="sidebar-link" @click="toggleSidebar">
                <SignOutIcon class="sidebar-icon" />
                Sign Out
              </router-link>
            </li>
          </ul>
        </div>
      </div>

      <!-- If user has not signed in -->
      <div v-else>
        <div class="flex flex-col gap-5 p-6">
          <div class="flex flex-row items-center gap-2">
            <PersonIconFillLarge class="w-8 h-8 fill-current" />
            <p class="text-[15px] font-bold">Anonymous User</p>
          </div>

          <hr>

          <ul class="space-y-3">
            <li>
              <router-link to="/login" class="sidebar-link" @click="toggleSidebar">
                <SignInIcon class="sidebar-icon" />
                Sign In
              </router-link>
              <router-link to="/register" class="sidebar-link" @click="toggleSidebar">
                <RocketIcon class="sidebar-icon" />
                Sign up
              </router-link>
            </li>
          </ul>

        </div>

      </div>

    </div>

  </header>
</template>

