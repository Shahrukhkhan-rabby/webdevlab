<template>
    <header class="sticky top-0 z-50 glass-effect shadow-lg">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Logo -->
          <div class="flex-shrink-0">
            <NuxtLink to="/" class="flex items-center space-x-2">
              <div class="w-8 h-8 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-lg flex items-center justify-center">
                <span class="text-white font-bold text-lg">L</span>
              </div>
              <span class="text-xl font-bold text-gray-900">WebDevLab</span>
            </NuxtLink>
          </div>
  
          <!-- Desktop Navigation -->
          <div class="hidden md:block">
            <div class="ml-10 flex items-baseline space-x-8">
              <NuxtLink to="/" class="nav-link">Home</NuxtLink>
              <NuxtLink to="/blog" class="nav-link">Blog</NuxtLink>
              <NuxtLink to="/courses" class="nav-link">Courses</NuxtLink>
              <NuxtLink to="/careers" class="nav-link">Careers</NuxtLink>
              <NuxtLink to="/forum" class="nav-link">Forum</NuxtLink>
              <NuxtLink to="/shorts" class="nav-link">Shorts</NuxtLink>
            </div>
          </div>
  
          <!-- CTA Button -->
          <div class="hidden md:block">
            <button class="btn-primary">
              Get Started
            </button>
          </div>
  
          <!-- Mobile menu button -->
          <div class="md:hidden">
            <button @click="toggleMobileMenu" class="text-gray-500 hover:text-gray-900 focus:outline-none">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>
  
        <!-- Mobile Navigation -->
        <div v-show="isMobileMenuOpen" class="md:hidden">
          <div class="px-2 pt-2 pb-3 space-y-1 bg-white rounded-lg mt-2 shadow-lg">
            <NuxtLink to="/" class="mobile-nav-link">Home</NuxtLink>
            <NuxtLink to="/blog" class="mobile-nav-link">Blog</NuxtLink>
            <NuxtLink to="/courses" class="mobile-nav-link">Courses</NuxtLink>
            <NuxtLink to="/careers" class="mobile-nav-link">Careers</NuxtLink>
            <NuxtLink to="/forum" class="mobile-nav-link">Forum</NuxtLink>
            <NuxtLink to="/shorts" class="mobile-nav-link">Shorts</NuxtLink>
            <div class="pt-3">
              <button class="btn-primary w-full">Get Started</button>
            </div>
          </div>
        </div>
      </nav>
    </header>
  </template>
  
  <script setup>
  const isMobileMenuOpen = ref(false)
  
  const toggleMobileMenu = () => {
    isMobileMenuOpen.value = !isMobileMenuOpen.value
  }
  </script>
  
  <style scoped>
  .nav-link {
    @apply text-gray-700 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200;
  }
  
  .nav-link.router-link-active {
    @apply text-primary-600 bg-primary-50;
  }
  
  .mobile-nav-link {
    @apply text-gray-700 hover:text-primary-600 block px-3 py-2 rounded-md text-base font-medium transition-colors duration-200;
  }
  </style>