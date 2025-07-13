<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { registerUser } from '@/api'
import { logger, extractErrorMessage } from '@/utils';


const router = useRouter();

const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const loading = ref(false);
const error = ref('');  /* the error message to user */

function isValidEmail(value) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(value);
}

async function handleRegister() {
  // Handle Register Request
  error.value = '';
  loading.value = true;

  if (!isValidEmail(email.value)) {
    error.value = 'Please enter a valid email';
    loading.value = false;
    return;
  }

  if (password.value !== confirmPassword.value) {
    error.value = 'Passwords do not match';
    loading.value = false;
    return;
  }

  try {
    await registerUser(email.value, password.value);

    logger.info('User registered successfully', {
      email: email.value,
    });

    await router.push({ name: 'login' });

  } catch (error) {
    const error_msg = extractErrorMessage(error);

    logger.error('User registered failed', {
      email: email.value,
      error: error_msg,
    });

    error.value = 'Register failed. Please try again';

  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <form @submit.prevent="handleRegister">
    <h2 class="text-2xl font-bold text-center">Register</h2>

    <div>
      <label for="email" class="block mb-1 font-medium">Email</label>
      <input
          v-model="email"
          id="email"
          type="email"
          required
          autocomplete="off"
      />
    </div>

    <div>
      <label for="password" class="block mb-1 font-medium">Password</label>
      <input
          v-model="password"
          id="password"
          type="password"
          required
          autocomplete="new-password"
      />
    </div>

    <div>
      <label for="confirmPassword" class="block mb-1 font-medium">Confirm Password</label>
      <input
          v-model="confirmPassword"
          id="confirmPassword"
          type="password"
          required
          autocomplete="new-password"
      />
    </div>

    <div v-if="error" class="text-red-500 text-sm text-center">
      {{ error }}
    </div>

    <button
        type="submit"
        :disabled="loading"
    >
      {{ loading ? "Signing up..." : "Sign up" }}
    </button>
  </form>
</template>

<style scoped>

</style>