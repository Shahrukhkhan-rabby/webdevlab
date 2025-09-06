<template>
    <div class="py-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Header -->
        <div class="text-center mb-12">
          <h1 class="text-4xl font-bold text-gray-900 mb-4">Career Portal</h1>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Discover exciting career opportunities from top companies. 
            Find your next role and take the next step in your professional journey.
          </p>
        </div>
  
        <!-- Search and Filters -->
        <div class="glass-effect rounded-xl p-6 mb-8">
          <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div class="md:col-span-2">
              <input
                type="text"
                placeholder="Search jobs, companies, or keywords..."
                class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
              >
            </div>
            <div>
              <select class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500">
                <option>All Locations</option>
                <option>Remote</option>
                <option>New York</option>
                <option>San Francisco</option>
                <option>London</option>
              </select>
            </div>
            <div>
              <select class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500">
                <option>Job Type</option>
                <option>Full-time</option>
                <option>Part-time</option>
                <option>Contract</option>
                <option>Internship</option>
              </select>
            </div>
          </div>
          <div class="mt-4">
            <button class="btn-primary">Search Jobs</button>
          </div>
        </div>
  
        <!-- Featured Jobs -->
        <div class="mb-12">
          <h2 class="text-2xl font-bold text-gray-900 mb-6">Featured Opportunities</h2>
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div v-for="job in featuredJobs" :key="job.id" class="card p-6 border-l-4 border-primary-500">
              <div class="flex items-start justify-between mb-4">
                <div class="flex items-center space-x-3">
                  <div class="w-12 h-12 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-lg flex items-center justify-center text-white font-bold">
                    {{ job.company.charAt(0) }}
                  </div>
                  <div>
                    <h3 class="text-xl font-semibold text-gray-900">{{ job.title }}</h3>
                    <p class="text-gray-600">{{ job.company }}</p>
                  </div>
                </div>
                <span class="inline-block bg-accent-100 text-accent-800 text-sm font-medium px-3 py-1 rounded-full">
                  Featured
                </span>
              </div>
              
              <div class="flex flex-wrap gap-2 mb-4">
                <span class="bg-gray-100 text-gray-700 text-sm px-3 py-1 rounded">{{ job.location }}</span>
                <span class="bg-gray-100 text-gray-700 text-sm px-3 py-1 rounded">{{ job.type }}</span>
                <span class="bg-primary-100 text-primary-800 text-sm px-3 py-1 rounded">${{ job.salary }}</span>
              </div>
              
              <p class="text-gray-600 mb-4">{{ job.description }}</p>
              
              <div class="flex items-center justify-between">
                <span class="text-sm text-gray-500">{{ job.posted }}</span>
                <button class="btn-primary">Apply Now</button>
              </div>
            </div>
          </div>
        </div>
  
        <!-- All Jobs -->
        <div class="mb-8">
          <h2 class="text-2xl font-bold text-gray-900 mb-6">All Opportunities</h2>
          <div class="space-y-4">
            <div v-for="job in allJobs" :key="job.id" class="card p-6 hover:shadow-xl transition-all duration-300">
              <div class="flex items-center justify-between">
                <div class="flex items-center space-x-4">
                  <div class="w-12 h-12 bg-gradient-to-r from-gray-400 to-gray-600 rounded-lg flex items-center justify-center text-white font-bold">
                    {{ job.company.charAt(0) }}
                  </div>
                  <div>
                    <h3 class="text-lg font-semibold text-gray-900">{{ job.title }}</h3>
                    <p class="text-gray-600">{{ job.company }} • {{ job.location }}</p>
                    <div class="flex gap-2 mt-1">
                      <span class="text-sm text-gray-500">{{ job.type }}</span>
                      <span class="text-sm text-gray-500">•</span>
                      <span class="text-sm text-gray-500">${{ job.salary }}</span>
                    </div>
                  </div>
                </div>
                <div class="text-right">
                  <button class="btn-outline mb-2">Apply</button>
                  <p class="text-sm text-gray-500">{{ job.posted }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
  
        <!-- Load More Button -->
        <div class="text-center">
          <button class="btn-outline">Load More Jobs</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const featuredJobs = ref([
    {
      id: 1,
      title: 'Senior Full Stack Developer',
      company: 'TechCorp',
      location: 'Remote',
      type: 'Full-time',
      salary: '120k-150k',
      description: 'Join our innovative team and work on cutting-edge web applications using React, Node.js, and cloud technologies.',
      posted: '2 days ago'
    },
    {
      id: 2,
      title: 'Product Manager',
      company: 'InnovateInc',
      location: 'San Francisco, CA',
      type: 'Full-time',
      salary: '140k-180k',
      description: 'Lead product strategy and development for our flagship SaaS platform serving millions of users worldwide.',
      posted: '3 days ago'
    }
  ])
  
  const allJobs = ref([
    {
      id: 3,
      title: 'Frontend Developer',
      company: 'WebSolutions',
      location: 'New York, NY',
      type: 'Full-time',
      salary: '90k-110k',
      posted: '1 week ago'
    },
    {
      id: 4,
      title: 'Data Scientist',
      company: 'DataDriven',
      location: 'Remote',
      type: 'Full-time',
      salary: '130k-160k',
      posted: '1 week ago'
    },
    {
      id: 5,
      title: 'UX Designer',
      company: 'DesignStudio',
      location: 'Los Angeles, CA',
      type: 'Contract',
      salary: '80k-100k',
      posted: '2 weeks ago'
    },
    {
      id: 6,
      title: 'Marketing Manager',
      company: 'GrowthCo',
      location: 'Chicago, IL',
      type: 'Full-time',
      salary: '70k-85k',
      posted: '2 weeks ago'
    }
  ])
  
  useHead({
    title: 'Careers - WebDevLab',
    meta: [
      { name: 'description', content: 'Find exciting career opportunities from top companies. Discover your next role.' }
    ]
  })
  </script>