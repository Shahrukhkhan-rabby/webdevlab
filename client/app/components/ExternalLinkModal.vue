<template>
    <div class="fixed inset-0 z-50 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <!-- Background overlay -->
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" @click="$emit('close')"></div>
  
        <!-- Modal panel -->
        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-blue-100 sm:mx-0 sm:h-10 sm:w-10">
                <svg class="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </div>
              <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left w-full">
                <h3 class="text-lg leading-6 font-medium text-gray-900">
                  You're leaving WebDevLab
                </h3>
                <div class="mt-2">
                  <p class="text-sm text-gray-500">
                    You're about to visit an external site. Stay connected with us by subscribing to our newsletter.
                  </p>
                  <p class="text-xs text-gray-400 mt-1 break-all">{{ url }}</p>
                </div>
                
                <!-- Form -->
                <form @submit.prevent="handleSubmit" class="mt-4">
                  <div class="mb-4">
                    <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email Address</label>
                    <input
                      id="email"
                      v-model="formData.email"
                      type="email"
                      required
                      class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-primary-500 focus:border-primary-500"
                      placeholder="your@email.com"
                    >
                  </div>
                  
                  <div class="mb-4">
                    <label class="flex items-center">
                      <input
                        v-model="formData.agreedToTerms"
                        type="checkbox"
                        required
                        class="rounded border-gray-300 text-primary-600 shadow-sm focus:border-primary-300 focus:ring focus:ring-primary-200 focus:ring-opacity-50"
                      >
                      <span class="ml-2 text-sm text-gray-600">
                        I agree to receive emails from this website
                      </span>
                    </label>
                  </div>
                  
                  <div class="flex gap-3">
                    <button
                      type="submit"
                      class="flex-1 btn-primary"
                      :disabled="!isFormValid"
                    >
                      Continue to Site
                    </button>
                    <button
                      type="button"
                      @click="$emit('close')"
                      class="flex-1 btn-outline"
                    >
                      Cancel
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    url: {
      type: String,
      required: true
    }
  })
  
  const emit = defineEmits(['close', 'proceed'])
  
  const formData = reactive({
    email: '',
    agreedToTerms: false
  })
  
  const isFormValid = computed(() => {
    return formData.email && formData.agreedToTerms
  })
  
  const handleSubmit = () => {
    if (isFormValid.value) {
      emit('proceed', { ...formData })
    }
  }
  </script>