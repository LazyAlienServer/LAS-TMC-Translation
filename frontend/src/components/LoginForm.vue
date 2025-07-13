<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores';
import { logger, extractErrorMessage } from '@/utils';


const router = useRouter();
const userStore = useUserStore();

const email = ref('');
const password = ref('');
const loading = ref(false);
const error = ref('');  /* the error message to user */

async function handleLogin() {
  // Handle Login Request
  error.value = '';
  loading.value = true;

  try {
    await userStore.login(email.value, password.value);

    logger.info('User logged in successfully', {
      email: email.value,
    });

    await router.push({ name: 'home' });

  } catch (error) {
    const error_msg = extractErrorMessage(error);

    logger.error('User login failed', {
      email: email.value,
      error: error_msg,
    });

    error.value = 'Login failed. Please try again';

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

    <div v-if="error" class="text-red-500 text-sm text-center">
      {{ error }}
    </div>

    <button
        type="submit"
        :disabled="loading"
    >
      {{ loading ? "Logging in..." : "Login" }}
    </button>
    <router-link :to="{ name: 'register' }" class="link">
      Do not have an account? Register here
    </router-link>
  </form>
</template>

<style scoped>

</style>