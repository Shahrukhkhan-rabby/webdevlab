<template>
  <div>
    <!-- Hero Section -->
    <section
      class="relative overflow-hidden bg-gradient-to-br from-primary-50 via-white to-secondary-50 py-20 sm:py-32"
    >
      <div class="absolute inset-0">
        <div
          class="absolute top-20 left-10 w-72 h-72 bg-primary-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"
        ></div>
        <div
          class="absolute top-40 right-10 w-72 h-72 bg-secondary-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"
          style="animation-delay: 2s"
        ></div>
        <div
          class="absolute bottom-20 left-1/2 w-72 h-72 bg-accent-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-pulse"
          style="animation-delay: 4s"
        ></div>
      </div>

      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h1
            class="text-4xl sm:text-6xl font-bold text-gray-900 mb-6 animate-fade-in"
          >
            Your Gateway to
            <span
              class="text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-secondary-600"
            >
              Knowledge
            </span>
          </h1>
          <p
            class="text-xl text-gray-600 mb-8 max-w-3xl mx-auto animate-slide-up"
          >
            Discover insightful articles, master new skills through expert
            courses, explore exciting career opportunities, and connect with a
            vibrant learning community.
          </p>
          <div
            class="flex flex-col sm:flex-row gap-4 justify-center animate-slide-up"
            style="animation-delay: 0.3s"
          >
            <button class="btn-primary text-lg px-8 py-4">
              Start Learning Today
            </button>
            <button class="btn-outline text-lg px-8 py-4">
              Explore Features
            </button>
          </div>
        </div>

        <!-- Feature Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mt-20">
          <div
            v-for="feature in features"
            :key="feature.title"
            class="card p-6 animate-slide-up"
            :style="`animation-delay: ${feature.delay}s`"
          >
            <div
              class="w-12 h-12 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-lg flex items-center justify-center mb-4"
            >
              <component :is="feature.icon" class="h-6 w-6 text-white" />
            </div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">
              {{ feature.title }}
            </h3>
            <p class="text-gray-600 mb-4">{{ feature.description }}</p>
            <NuxtLink
              :to="feature.link"
              class="text-primary-600 font-medium hover:text-primary-700 transition-colors duration-200"
            >
              Explore {{ feature.title }} →
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900">
            Join Thousands of Learners
          </h2>
          <p class="text-gray-600 mt-4">
            Be part of our growing community of knowledge seekers
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div v-for="stat in stats" :key="stat.label" class="text-center">
            <div class="text-4xl font-bold text-primary-600 mb-2">
              {{ stat.value }}
            </div>
            <div class="text-gray-600">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Content -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-900">Featured Content</h2>
          <p class="text-gray-600 mt-4">Discover our most popular resources</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <!-- Latest Blog Post -->
          <div class="card p-6">
            <div
              class="aspect-video bg-gradient-to-r from-primary-400 to-secondary-400 rounded-lg mb-4"
            ></div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">
              Latest from Our Blog
            </h3>
            <p class="text-gray-600 mb-4">
              Stay updated with the latest insights, tutorials, and industry
              trends.
            </p>
            <NuxtLink to="/blog" class="btn-outline">Read Articles</NuxtLink>
          </div>

          <!-- Featured Course -->
          <div class="card p-6">
            <div
              class="aspect-video bg-gradient-to-r from-accent-400 to-primary-400 rounded-lg mb-4"
            ></div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">
              Featured Course
            </h3>
            <p class="text-gray-600 mb-4">
              Master new skills with our comprehensive, expert-led courses.
            </p>
            <NuxtLink to="/courses" class="btn-primary">View Courses</NuxtLink>
          </div>

          <!-- Career Opportunities -->
          <div class="card p-6">
            <div
              class="aspect-video bg-gradient-to-r from-secondary-400 to-accent-400 rounded-lg mb-4"
            ></div>
            <h3 class="text-xl font-semibold text-gray-900 mb-2">
              Career Portal
            </h3>
            <p class="text-gray-600 mb-4">
              Discover exciting career opportunities from top companies.
            </p>
            <NuxtLink to="/careers" class="btn-secondary">Find Jobs</NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <!-- Newsletter CTA -->
    <section class="py-16 bg-gradient-to-r from-primary-600 to-secondary-600">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl font-bold text-white mb-4">Stay in the Loop</h2>
        <p class="text-primary-100 text-lg mb-8">
          Get the latest articles, course updates, and career opportunities
          delivered to your inbox.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 max-w-lg mx-auto">
          <input
            type="email"
            placeholder="Enter your email"
            class="flex-1 px-4 py-3 rounded-lg border-0 focus:outline-none focus:ring-2 focus:ring-primary-300"
          />
          <button
            class="bg-white text-primary-600 font-semibold px-8 py-3 rounded-lg hover:bg-gray-50 transition-colors duration-200"
          >
            Subscribe
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// Feature icons - using simple div elements to avoid dependency issues
const features = [
  {
    title: "Blog",
    description: "Insightful articles and tutorials from industry experts.",
    link: "/blog",
    icon: "div", // In production, use proper icons
    delay: 0.5,
  },
  {
    title: "Courses",
    description: "Comprehensive online courses to master new skills.",
    link: "/courses",
    icon: "div",
    delay: 0.7,
  },
  {
    title: "Careers",
    description: "Discover exciting job opportunities from top companies.",
    link: "/careers",
    icon: "div",
    delay: 0.9,
  },
  {
    title: "Forum",
    description: "Connect and discuss with fellow learners and experts.",
    link: "/forum",
    icon: "div",
    delay: 1.1,
  },
  {
    title: "Shorts",
    description: "Quick, bite-sized learning content for busy schedules.",
    link: "/shorts",
    icon: "div",
    delay: 1.3,
  },
  {
    title: "Community",
    description: "Join a vibrant community of knowledge seekers.",
    link: "/forum",
    icon: "div",
    delay: 1.5,
  },
];

const stats = [
  { value: "10K+", label: "Active Learners" },
  { value: "500+", label: "Courses Available" },
  { value: "1M+", label: "Articles Read" },
  { value: "95%", label: "Success Rate" },
];

useHead({
  title: "WebDevLab - Your Gateway to Knowledge",
  meta: [
    {
      name: "description",
      content:
        "Discover articles, courses, career opportunities, and connect with our community.",
    },
  ],
});
</script>