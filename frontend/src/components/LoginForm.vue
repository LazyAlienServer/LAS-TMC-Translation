<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores';
import { useToast } from "vue-toastification";

const toast = useToast();
const router = useRouter();
const userStore = useUserStore();

const email = ref('');
const password = ref('');
const loading = ref(false);

async function handleLogin() {
  loading.value = true;

  try {
    await userStore.login(email.value, password.value);
    await router.push({ name: 'home' });

  } catch (error) {
    const msg = error.response?.data?.toast_error
    toast.error(msg);
    console.error("Login failed", error);

  } finally {
    loading.value = false;
  }

}
</script>

<template>
  <form @submit.prevent="handleLogin">
    <h2 class="text-2xl font-bold text-center">Login</h2>

    <div>
      <label for="email" class="block mb-1 font-medium">Email</label>
      <input
          v-model="email"
          id="email"
          type="email"
          required
      />
    </div>

    <div>
      <label for="password" class="block mb-1 font-medium">Password</label>
      <input
          v-model="password"
          id="password"
          type="password"
          required
      />
    </div>

    <button type="submit" :disabled="loading">
      Sign in
    </button>
    <router-link :to="{ name: 'register' }" class="link">
      Do not have an account? Register here
    </router-link>
  </form>
</template>
