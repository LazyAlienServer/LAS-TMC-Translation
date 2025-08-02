<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { registerUser } from '@/api'
import { useToast } from "vue-toastification";

const router = useRouter();
const toast = useToast();

const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const loading = ref(false);

async function handleRegister() {
  loading.value = true;

  try {
    await registerUser(email.value, password.value, confirmPassword.value);
    toast.success('Successfully signed up!');
    await router.push({ name: 'login' });

  } catch (error) {
    const msg = error.response.data.toast_error
    toast.error(msg)
    console.error("Register failed, ", error)

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

    <p class="text-[12px]">Your password must contain at least 8 characters.</p>
    <p class="text-[12px]">Your password can’t be entirely numeric.</p>
    <p class="text-[12px]">Your password can’t be a commonly used password.</p>
    <p class="text-[12px]">Your password can’t be too similar to your other personal information.</p>

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

    <button type="submit" :disabled="loading">
      Sign up
    </button>

  </form>

</template>

<style scoped>

</style>