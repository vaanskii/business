<template>
<template v-if="userStore.user.isAuthenticated">
<nav class="border-gray-900 bg-transparent shadow-lg border-b-2">
  <div class="max-w-screen-2xl flex flex-wrap items-center justify-between mx-auto p-4">
      <a href="#" class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Business</a>
  <div class="flex items-center md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
      <button type="button" class="flex text-sm bg-gray-800 rounded-full md:me-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600" id="user-menu-button" aria-expanded="false" data-dropdown-toggle="user-dropdown" data-dropdown-placement="bottom">
        <span class="sr-only">Open user menu</span>
        <img class="w-8 h-8 rounded-full" src="" alt="user photo">
      </button>
      <!-- Dropdown menu -->
      <div class="z-50 hidden my-4 text-base list-none bg-white divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-700 dark:divide-gray-600" id="user-dropdown">
        <div class="px-4 py-3">
          <span class="block text-sm text-gray-900 dark:text-white">Bonnie Green</span>
          <span class="block text-sm  text-gray-500 truncate dark:text-gray-400">name@flowbite.com</span>
        </div>
        <ul class="py-2" aria-labelledby="user-menu-button">
          <li>
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Dashboard</a>
          </li>
          <li>
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Settings</a>
          </li>
          <li>
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Earnings</a>
          </li>
          <li>
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white">Sign out</a>
          </li>
        </ul>
      </div>
      <button @click="logout()">Logout</button>
  </div>
  <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-user">
    <ul class="flex flex-col font-medium p-4 md:p-0 mt-4 border rounded-lg md:space-x-10 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0">
      <li>
        <a href="#" class="block py-2 px-3 text-white bg-blue-900 rounded md:bg-transparent md:p-0 dark:text-white antialiased font-light " aria-current="page">Home</a>
      </li>
      <li>
        <a href="#" class="block py-2 px-3 text-gray-900 rounded  md:p-0 dark:text-white antialiased font-light">About</a>
      </li>
      <li>
        <a href="#" class="block py-2 px-3 text-gray-900 rounded  md:p-0 dark:text-white antialiased font-light ">Services</a>
      </li>
      <li>
        <a href="#" class="block py-2 px-3 text-gray-900 rounded  md:p-0 dark:text-white antialiased font-light ">Pricing</a>
      </li>
      <li>
        <a href="#" class="block py-2 px-3 text-gray-900 rounded  md:p-0 dark:text-white antialiased font-light ">Contact</a>
      </li>
    </ul>
  </div>
  </div>
</nav>
</template>
<template v-else>
    <nav class="border-gray-900 bg-transparent shadow-lg border-b-2 ">
  <div class="max-w-screen-2xl flex flex-wrap items-center justify-between mx-auto p-4">
      <a href="#" class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Business</a>
  <div class="flex items-center md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
      
    <button><a class="w-full shadow-lg text-gray-100 border bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 hover:bg-black hover:text-white transition ease-in-out hover:-translate-y-1 hover:scale-100" href="/signup">Sign up</a></button>
    <button><a class="w-full ml-5 shadow-lg text-gray-100 border bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800 hover:bg-black hover:text-white transition ease-in-out hover:-translate-y-1 hover:scale-100" href="/login">Login</a></button>
     
        
  </div>
  <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-user">
    <ul class="flex flex-col font-medium p-4 md:p-0 mt-4 border rounded-lg md:space-x-10 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0">
      <li>
        <RouterLink to="#" class="block py-2 px-3 text-gray-900 rounded  md:p-0 dark:text-white antialiased font-light">Home</RouterLink>
      </li>
      <li>
        <RouterLink to="#" class="block py-2 px-3 text-gray-900 rounded  md:p-0 dark:text-white antialiased font-light">About</RouterLink>
      </li>
      <li>
        <RouterLink to="#" class="block py-2 px-3 text-gray-900 rounded  md:p-0 dark:text-white antialiased font-light ">Services</RouterLink>
      </li>
      <li>
        <RouterLink to="#" class="block py-2 px-3 text-gray-900 rounded  md:p-0 dark:text-white antialiased font-light ">Pricing</RouterLink>
      </li>
      <li>
        <RouterLink to="#" class="block py-2 px-3 text-gray-900 rounded  md:p-0 dark:text-white antialiased font-light ">Contact</RouterLink>
      </li>
    </ul>
  </div>
  </div>
</nav>
</template>
</template>

<script>
import { useUserStore } from '@/stores/user'
export default{
    setup() {
          const userStore = useUserStore()

          return {
              userStore
          }
      },
      methods: {
        logout() {
            this.userStore.removeToken()
            this.$router.push('/login')
      }
  },
}
</script>