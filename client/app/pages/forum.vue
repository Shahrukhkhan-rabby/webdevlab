<template>
    <div class="py-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Header -->
        <div class="text-center mb-12">
          <h1 class="text-4xl font-bold text-gray-900 mb-4">Community Forum</h1>
          <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Connect with fellow learners, share knowledge, ask questions, and be part of our vibrant community.
          </p>
        </div>
  
        <!-- Quick Actions -->
        <div class="flex flex-col sm:flex-row gap-4 mb-8">
          <button class="btn-primary flex items-center justify-center">
            <span class="mr-2">+</span>
            Start New Discussion
          </button>
          <input
            type="text"
            placeholder="Search discussions..."
            class="flex-1 px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
          >
        </div>
  
        <!-- Categories -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          <div v-for="category in categories" :key="category.name" class="card p-6 text-center hover:border-primary-200">
            <div class="w-12 h-12 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-lg flex items-center justify-center mx-auto mb-4">
              <span class="text-white font-bold">{{ category.name.charAt(0) }}</span>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ category.name }}</h3>
            <p class="text-gray-600 text-sm mb-3">{{ category.description }}</p>
            <div class="text-sm text-gray-500">
              {{ category.posts }} posts • {{ category.members }} members
            </div>
          </div>
        </div>
  
        <!-- Recent Discussions -->
        <div>
          <h2 class="text-2xl font-bold text-gray-900 mb-6">Recent Discussions</h2>
          <div class="space-y-4">
            <div v-for="discussion in discussions" :key="discussion.id" class="card p-6">
              <div class="flex items-start space-x-4">
                <div class="w-12 h-12 bg-gradient-to-r from-gray-400 to-gray-600 rounded-full flex items-center justify-center text-white font-bold">
                  {{ discussion.author.charAt(0) }}
                </div>
                <div class="flex-1">
                  <div class="flex items-center justify-between mb-2">
                    <h3 class="text-lg font-semibold text-gray-900 hover:text-primary-600 cursor-pointer">
                      {{ discussion.title }}
                    </h3>
                    <div class="flex items-center space-x-4 text-sm text-gray-500">
                      <span>{{ discussion.replies }} replies</span>
                      <span>{{ discussion.views }} views</span>
                    </div>
                  </div>
                  <p class="text-gray-600 mb-3">{{ discussion.excerpt }}</p>
                  <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-4 text-sm text-gray-500">
                      <span>by {{ discussion.author }}</span>
                      <span>•</span>
                      <span>{{ discussion.posted }}</span>
                      <span class="bg-primary-100 text-primary-800 px-2 py-1 rounded">
                        {{ discussion.category }}
                      </span>
                    </div>
                    <div class="flex items-center space-x-2">
                      <button class="text-gray-400 hover:text-red-500 transition-colors duration-200">
                        ♥ {{ discussion.likes }}
                      </button>
                      <button class="text-primary-600 hover:text-primary-700 font-medium">
                        Reply
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
  
        <!-- Load More Button -->
        <div class="text-center mt-12">
          <button class="btn-outline">Load More Discussions</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const categories = ref([
    {
      name: 'General',
      description: 'General discussions and introductions',
      posts: 1240,
      members: 3200
    },
    {
      name: 'Web Development',
      description: 'HTML, CSS, JavaScript, and frameworks',
      posts: 890,
      members: 2100
    },
    {
      name: 'Career Advice',
      description: 'Job hunting, interviews, and career tips',
      posts: 650,
      members: 1800
    },
    {
      name: 'Data Science',
      description: 'Python, R, machine learning, and analytics',
      posts: 420,
      members: 1200
    },
    {
      name: 'Design',
      description: 'UI/UX design, graphics, and creativity',
      posts: 380,
      members: 950
    },
    {
      name: 'Business',
      description: 'Entrepreneurship, marketing, and strategy',
      posts: 290,
      members: 720
    }
  ])
  
  const discussions = ref([
    {
      id: 1,
      title: 'Best practices for React component architecture?',
      excerpt: 'I\'m working on a large React application and looking for advice on how to structure components effectively...',
      author: 'Alex Chen',
      category: 'Web Development',
      posted: '2 hours ago',
      replies: 15,
      views: 234,
      likes: 8
    },
    {
      id: 2,
      title: 'How to transition from junior to senior developer?',
      excerpt: 'I\'ve been working as a junior developer for 2 years now and wondering what skills I need to develop to move up...',
      author: 'Sarah Kim',
      category: 'Career Advice',
      posted: '4 hours ago',
      replies: 23,
      views: 456,
      likes: 12
    },
    {
      id: 3,
      title: 'Machine Learning resources for beginners',
      excerpt: 'Can anyone recommend good resources for someone just starting with machine learning? Looking for both theory and practical...',
      author: 'Mike Johnson',
      category: 'Data Science',
      posted: '1 day ago',
      replies: 31,
      views: 678,
      likes: 18
    },
    {
      id: 4,
      title: 'Design system implementation tips',
      excerpt: 'Our team is starting to implement a design system across multiple products. Any tips or lessons learned from your experience?',
      author: 'Emma Wilson',
      category: 'Design',
      posted: '2 days ago',
      replies: 19,
      views: 345,
      likes: 14
    }
  ])
  
  useHead({
    title: 'Forum - WebDevLab',
    meta: [
      { name: 'description', content: 'Join our community forum to connect with fellow learners, share knowledge, and get help.' }
    ]
  })
  </script>