<script setup lang="ts">
import type { NuxtError } from '#app';

// During the lifespan of your application, some errors may appear unexpectedly at runtime. In such case, we can use the error.vue file to override the default error files and display the error nicely.

const props = defineProps({
  error: Object as () => NuxtError
})
</script>

<template>
  <div>
    <h1>{{ error.statusCode }}</h1>
    <NuxtLink to="/">Go back home</NuxtLink>
  </div>
</template>