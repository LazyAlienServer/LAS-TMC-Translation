<script setup>
import { ref, computed } from "vue";
import { useUserStore } from "@/stores";
import { uploadAvatar, updateUsername } from "@/api";
import { useToast } from "vue-toastification";

const toast = useToast();
const userStore = useUserStore();
const userInfo = computed(() => userStore.userInfo);
const avatarUrl = computed(() => import.meta.env.VITE_API_BASE_URL + userStore.userInfo.avatar)

const fileInput = ref(null);

// Open File Select Window
function triggerFileSelect() {
  fileInput.value.click();
}

// Handle File Upload
async function handleFile(event) {
  const file = event.target.files[0];
  if (!file) return;

  try {
    await uploadAvatar(file);
    await userStore.loadUserInfo();
    toast.success('Avatar updated successfully!');

  } catch (error) {
    const msg = error.response?.data?.toast_error
    toast.error(msg);
    console.error('Avatar update failed:', error);
  }
}

// Edit Username
const isInputOpen = ref(false);
const newUsername = ref("");
const loading = ref(false);

function toggleInput() {
  isInputOpen.value = !isInputOpen.value;
}

async function handleUsernameUpdate() {
  loading.value = true;

  try {
    await updateUsername(newUsername.value)
    toast.success('Username updated successfully!');
    await userStore.loadUserInfo()

  } catch (error) {
    const msg = error.response?.data?.toast_error
    toast.error(msg);
    console.error('Update username failed', error)

  } finally {
    toggleInput()
    loading.value = false;
  }
}
</script>

<template>
  <div v-if="userInfo" class="flex flex-col gap-5 pl-3 pr-15 pt-3 h-auto mb-20">
    <div class="flex flex-col gap-y-7 items-center relative">

      <img
          :src="avatarUrl"
          alt="User Avatar"
          class="w-55 h-55 rounded-full object-cover border border-gray-300"
      />

      <img
          src="@/assets/icons/pencil-16.svg"
          alt="edit"
          @click="triggerFileSelect"
          class="absolute top-0 right-0 bg-white rounded-full p-1 shadow-md transform -translate-x-2 translate-y-2"
      />
      <input
          ref="fileInput"
          type="file"
          accept="image/*"
          class="hidden"
          @change="handleFile"
      />

    </div>

    <!-- Edit username -->
    <div
        v-if="isInputOpen"
        class="flex flex-col items-center gap-3"
    >

      <input
          v-model="newUsername"
          type="text"
          placeholder="        New Username"
      />

      <div class="flex flex-row items-center gap-3">
        <button @click="handleUsernameUpdate" :disabled="loading">Save</button>
        <button @click="toggleInput" :disabled="loading" class="bg-gray-400 hover:bg-gray-500">Cancel</button>
      </div>

    </div>

    <div v-else class="flex flex-col items-center gap-4">

      <!-- username & edit toggle button-->
      <p class="text-2xl font-bold">{{ userInfo.username }}</p>

      <div
          class="flex flex-row items-center gap-x-2 rounded-lg border border-gray-400 hover:bg-gray-300 px-4 py-1"
          @click="toggleInput"
      >

        <img src="@/assets/icons/pencil-16.svg" alt="edit"/>
        <p class="text-[16px]">Edit Your Username</p>

      </div>

      <!-- Other user info -->
      <div class="flex flex-col pl-2 mt-2 gap-2">

        <div class="flex flex-row items-center gap-1">
          <img src="@/assets/icons/person-16.svg" alt="id"/>
          <p class="text-[16px]">ID: {{ userInfo.id }}</p>
        </div>

        <div class="flex flex-row items-center gap-1">
          <img src="@/assets/icons/mail-16.svg" alt="email"/>
          <p class="text-[16px]">Email: {{ userInfo.email }}</p>
        </div>

      </div>

    </div>

  </div>
</template>