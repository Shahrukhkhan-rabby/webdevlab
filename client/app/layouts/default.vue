<template>
    <div class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-blue-50">
      <AppHeader />
      <main>
        <slot />
      </main>
      <AppFooter />
      <ExternalLinkModal 
        v-if="showExternalModal" 
        :url="externalUrl" 
        @close="closeExternalModal" 
        @proceed="handleExternalProceed" 
      />
      <Toast />
    </div>
  </template>
  
  <script setup>
  const showExternalModal = ref(false)
  const externalUrl = ref('')
  
  // Copy text enhancement
  onMounted(() => {
    document.addEventListener('copy', handleCopy)
    document.addEventListener('click', handleExternalLink)
  })
  
  onBeforeUnmount(() => {
    document.removeEventListener('copy', handleCopy)
    document.removeEventListener('click', handleExternalLink)
  })
  
  const handleCopy = async () => {
    try {
      const selection = window.getSelection().toString()
      if (selection.trim()) {
        const websiteUrl = window.location.origin
        const textWithUrl = `${selection}\n\nSource: ${websiteUrl}`
        await navigator.clipboard.writeText(textWithUrl)
      }
    } catch (err) {
      console.log('Copy enhancement failed:', err)
    }
  }
  
  const handleExternalLink = (event) => {
    const link = event.target.closest('a[href^="http"]')
    if (link && !link.href.includes(window.location.hostname)) {
      event.preventDefault()
      externalUrl.value = link.href
      showExternalModal.value = true
    }
  }
  
  const closeExternalModal = () => {
    showExternalModal.value = false
    externalUrl.value = ''
  }
  
  const handleExternalProceed = (data) => {
    // Here you would typically send the email data to your backend
    console.log('User email:', data.email, 'Agreed to terms:', data.agreedToTerms)
    
    // Proceed to external link
    window.open(externalUrl.value, '_blank')
    closeExternalModal()
  }
  </script>